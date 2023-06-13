#!/usr/bin/env python3

import argparse
import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Plot bad pixel map",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file", type=str, default="thr_map_0.dat", help="Input file")
    parser.add_argument("-p", "--print", action="store_true", help="Print bad pixels")
    args = parser.parse_args()
    infile = args.file
    with open(infile, "rb") as fin:
        indata = fin.read()
    # fin = open(infile, "rb")
    thrdata = np.frombuffer(indata, dtype=np.int32)
    data = np.zeros((thrdata.shape[0],2))
    print("Number of pixels: ",thrdata.shape[0])
    for i in range(thrdata.shape[0]):
        xy = np.cast[np.int32](thrdata[i])
        data[i][0] = (xy >> 9) & 0x7FF
        data[i][1] = xy & 0x1FF
    fin.close()
    data = data[data[:,0].argsort()]

    x = data[:,0]
    y = data[:,1]

    if args.print:
        outfile = infile.replace(".dat",".txt")
        with open(outfile, "w") as fout:
            fout.write("x y\n")
            fout.write("-----\n")
            for i in range(x.shape[0]):
                fout.write(f"{x[i]:.0f} {y[i]:.0f}\n")

        fout.close()


    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y, s=10, c='red', marker='o')
    ax.set_xlim(0, 3*1024)
    ax.set_ylim(0, 512)
    ax.plot([1024,1024],[0,512],c='black',ls='--')
    ax.plot([2*1024,2*1024],[0,512],c='black',ls='--')

    plt.show()
