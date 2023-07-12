#!/usr/bin/env python3

import os
import sys
import json
import argparse
import numpy as np


class HotPixelMask:
    '''
    Class to read hitmap and create a mask of hot pixels.
    '''

    def __init__(self, run_parameters, data_dir="fhrana/", noise_cut=10, ntrg=1e6, verbose=True):
        self.filename = run_parameters
        self.data_directory = data_dir
        self.verbose = verbose
        self.noise_cut = noise_cut
        self.ntrg = ntrg
        if self.data_directory[-1] != '/':
            self.data_directory += '/'
        # self.hitmaps = []
        # read list of .dat files from data_dir
        self.hitmaps = [f'{data_dir}{f}' for f in os.listdir(data_dir) if f.endswith('.dat')]
        with open(run_parameters) as f:
            self.params = json.load(f)
        self.ladders = self.params['_cable_resistance']
        self.staveids = [f'L{((int(lstr[1]) << 12) | int(lstr[3:]) | (0 << 8)) >> 12:01d}_{((int(lstr[1]) << 12) | int(lstr[3:]) | (0 << 8)) & 0x1F:02d}' for lstr in self.ladders]
        if self.verbose:
            for staveid in self.staveids:
                print(f'Stave {staveid} found.')

    def read_stave_data(self, staveid):
        feeids = sorted([(int(staveid[1]) << 12) | int(staveid[3:]) | (gbt << 8) for gbt in range(3)])
        data = np.zeros((9, 512, 1024), dtype=np.uint32)
        for gbt_channel in range(3):
            filename = next((f for f in self.hitmaps if f.endswith(f'_{feeids[gbt_channel]}.dat')), None)
            feeid = feeids[gbt_channel]
            print(f'Processing stave {staveid} feeid {feeid} gbt_channel {gbt_channel}')
            # check if file exists
            print(f'Opening file {filename}')
            fin = open(filename, 'r')
            hitdata = np.fromfile(fin, dtype=np.uint32)
            for j in range(512):
                for k in range(1024*3):
                    i = k // 1024
                    data[gbt_channel*3 + i][j][k - i*1024] = hitdata[j*3*1024 + k]
            fin.close()
        return data

    def create_hot_pixel_mask(self):
        hot_pixel_map = {}
        for stave in self.staveids:
            stave_hot_pixel_map = {}
            stave_data = self.read_stave_data(stave)
            for chip in range(0, stave_data.shape[0]):
                chip_hot_pixels = []
                # chip_data = stave_data[chip]
                # print(stave_data[chip])
                totalnoisy = np.count_nonzero(stave_data[chip][stave_data[chip] >= self.noise_cut])
                noisy_pixels = np.argwhere(stave_data[chip] >= self.noise_cut)
                if len(noisy_pixels) > 0:
                    for i in noisy_pixels:
                        chip_hot_pixels.append(f"[{i[1]},{i[0]}]")
                print(f'Found {totalnoisy} noisy pixels on chip {chip} of stave {stave}.')
                stave_hot_pixel_map[f"{chip}"] = chip_hot_pixels
            hot_pixel_map[stave] = stave_hot_pixel_map

        return hot_pixel_map

    def save_hot_pixel_mask(self, outputfile):
        hot_pixel_map = self.create_hot_pixel_mask()
        with open(outputfile, 'w') as f:
            json.dump(hot_pixel_map, f, indent=4)
        print(f'Hot pixel mask saved to {outputfile}.')
        if self.verbose:
            print(hot_pixel_map)


def print_args(args):
    print('Json file: ', args.i)
    print('Data directory: ', args.d)
    print('Output prefix: ', args.p)
    print('Noise cut: ', args.noise_cut)
    print('Number of triggers: ', args.ntrg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Threshold analysis.",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument("-thr", help="Threshold file", required=True)
    parser.add_argument("-i", help="Run parameters json file", required=True)
    parser.add_argument("-d", help="Data directory", required=False, default="./fhrana/")
    parser.add_argument("-p", help="Output file prefix", required=False, default='./fhrana/')
    parser.add_argument("-n", "--noise_cut", required=False, type=int, help="Noise cut", default=10)
    parser.add_argument("-t", "--ntrg", required=False, type=int, help="Number of triggers", default=1e6)
    parser.add_argument("-v", "--verbose", required=False, action="store_true", help="Verbose output")
    args = parser.parse_args()

    # load arguments
    run_parameter_file = args.i
    data_directory = args.d
    output_prefix = args.p
    noise_cut = args.noise_cut
    ntrigger = args.ntrg
    verbose = args.verbose

    # check that the run parameter file exists and is json
    if not run_parameter_file.endswith(".json") or not os.path.exists(run_parameter_file):
        print("Please provide a valid run parameters file.")
        sys.exit(1)
    #check if data directory exists
    if not os.path.exists(data_directory):
        print("Please provide a valid data directory.")
        sys.exit(1)

    if verbose:
        print_args(args)

    HotPixelMap = HotPixelMask(run_parameters= run_parameter_file,
                               data_dir= data_directory,
                               noise_cut= noise_cut,
                               ntrg= ntrigger,
                               verbose= verbose)

    outputfile = f'{output_prefix}hot_pixel_mask.json'

    # create hot pixel mask
    HotPixelMap.save_hot_pixel_mask(outputfile)
