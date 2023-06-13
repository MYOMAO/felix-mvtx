#!/usr/bin/env python3

import sys
import subprocess
import os
import json
from multiprocessing import Pool

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))+'/'
DECODER = SCRIPT_PATH+'../../../cpp/decoder/mvtx-decoder'
if not os.path.isfile(DECODER):
    print('decoder executable not found, is it compiled?')
    sys.exit(1)

if len(sys.argv) > 2:
    # FLX0
    if sys.argv[2] == "FLX0":
        PACKETS = [2001, 2002]
        INPUTS = [(0, 256, 512, 4099, 4355, 4611, 8198, 8199, 8454, 8455, 8710, 8711),
                  (1, 257, 513, 4100, 4356, 4612, 8200, 8201, 8456, 8457, 8712, 8713)]
    elif sys.argv[2] == "FLX1":
        # FLX1
        PACKETS = [2011, 2012]
        INPUTS = [(2, 258, 514, 4101, 4102, 4357, 4358, 4613, 4614, 8202, 8458, 8714),
                  (3, 259, 515, 4103, 4359, 4615, 8203, 8204, 8459, 8460, 8715, 8716)]
    elif sys.argv[2] == "FLX2":
        # FLX2
        PACKETS = [2021, 2022]
        INPUTS = [(4, 260, 516, 4104, 4105, 4360, 4361, 4616, 4617, 8205, 8461, 8717),
                  (5, 261, 517, 4106, 4362, 4618, 8206, 8207, 8462, 8463, 8718, 8719)]
    elif sys.argv[2] == "FLX3":
        # FLX3
        PACKETS = [2031, 2032]
        INPUTS = [(6, 262, 518, 4107, 4363, 4619, 8208, 8209, 8464, 8465, 8720, 8721),
                  (7, 263, 519, 4108, 4364, 4620, 8210, 8211, 8466, 8467, 8722, 8723)]
    elif sys.argv[2] == "FLX4":
        # FLX4
        PACKETS = [2041, 2042]
        INPUTS = [(8, 264, 520, 4109, 4110, 4365, 4366, 4621, 4622, 8192, 8448, 8704),
                  (9, 265, 521, 4111, 4367, 4623, 8193, 8194, 8449, 8450, 8705, 8706)]
    elif sys.argv[2] == "FLX5":
        # FLX5
        PACKETS = [2051, 2052]
        INPUTS = [(10, 266, 522, 4096, 4097, 4352, 4353, 4608, 4609, 8195, 8451, 8707),
                  (11, 267, 523, 4098, 4354, 4610, 8196, 8197, 8452, 8453, 8708, 8709)]
    else:
        # Telescope
        PACKETS = [2001, 2002]
        INPUTS = [(8212, 8213, 8214, 8215, 8468, 8469, 8470, 8471, 8724, 8725, 8726, 8727),
                  (8216, 8217, 8218, 8219, 8472, 8473, 8474, 8475, 8728, 8729, 8730, 8731)]
else:
    # Telescope
    PACKETS = [2001, 2002]
    INPUTS = [(8212, 8213, 8214, 8215, 8468, 8469, 8470, 8471, 8724, 8725, 8726, 8727),
              (8216, 8217, 8218, 8219, 8472, 8473, 8474, 8475, 8728, 8729, 8730, 8731)]


def thrana(path, packet, feeid, cwd):
    subprocess.run(f'source /home/mvtx/software/setup.sh > /dev/null && ddump -s -g -p {packet}  -n 0 {path} | {DECODER} -t 1 -f {feeid} -n 1 > /dev/null', cwd=cwd, shell=True)


def process(path):
    dir = os.path.dirname(path)
    n = None
    print('Processing "%s"...'%path)

    outdir = dir+'/thrana/'
    try:
        os.mkdir(outdir)
    except FileExistsError:
        pass
    print(f'  ... decoding to "{outdir}"...')
    with Pool(None) as pool:
        if os.path.isfile(path):
            for i, packet in enumerate(PACKETS):
                for feeid in INPUTS[i]:
                    pool.apply_async(thrana, (path, packet, feeid, outdir))
        pool.close()
        pool.join()


path = sys.argv[1]
process(path)
