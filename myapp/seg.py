import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('images', nargs='+', help='input images')
parser.add_argument('--alpha', type=float, help="adjustment parameter for the automatic global threshold", default=1.0)
parser.add_argument('--method', choices=['otsu','gmm','grabcut'], help='segmentation method (global otsu threshold or GMM estimation)', default='otsu')
parser.add_argument('--border', type=int, default=0.1, help='relative border definition (used by GMM)')
parser.add_argument('--displaymode', choices=['disabled', 'pdf', 'png', 'screen'], help='whether to show the segmentation result (screen), to write it to a file (pdf, png), or to skip it (disabled)',
    default='screen')
parser.add_argument('--nocalibration', action='store_true', help='disable calibration')
parser.add_argument('--outstats', default='stats.json', help='output file for statistics')
parser.add_argument('--calibration_pattern', default='checkerboard', help='which calibration pattern should be assumed (checkerboard or black_bar)',
        choices=["checkerboard", "black_bar"])
parser.add_argument('--calibration_pos', default='bottom_left', help='where is the calibration pattern located (bottom_left, bottom_right, top_left, top_right)',
        choices=["bottom_left", "bottom_right", "top_left", "top_right"])
parser.add_argument("--calibration_relative_height", type=float, default=0.3)
parser.add_argument("--calibration_relative_width", type=float, default=0.1)

args = parser.parse_args()

from segtools import *
import numpy as np
# from scipy.misc import imread
import imageio

# image = imageio.imread('image_path.jpg')

if args.displaymode!='disabled':
    import matplotlib.pyplot as plt


import json
from os.path import basename, splitext

allstats = {}

np.random.seed(1)
for index,imgfn in enumerate(args.images):
    print("okkkkk")
    image = imageio.imread(imgfn)
    print ("{}/{} {}: {}".format( index+1, len(args.images), imgfn, (image.shape[1], image.shape[0]) ))
    stats, contour, binaryimage = seg_butterfly(image, method=args.method, alpha=args.alpha, gmmborder=args.border)

    if not args.nocalibration:
        cal_length = estimate_calibration_length(image, calibration_pattern=args.calibration_pattern, 
                crop_x=args.calibration_relative_width, crop_y=args.calibration_relative_height, pos=args.calibration_pos)
        if cal_length>0:
            stats['c-area-calibrated'] = stats['c-area']/cal_length**2
            stats['width-calibrated'] = (stats['c-xmax']-stats['c-xmin'])/cal_length
            stats['height-calibrated'] = (stats['c-ymax']-stats['c-ymin'])/cal_length
            stats['calibration-length'] = cal_length

    print ("Statistics in segmented region: {}".format( json.dumps(stats, indent=2) ))
    imgfn_base = basename(imgfn)
    allstats[imgfn_base] = stats
    res=str(round(float(stats['width-calibrated']),2))+"x"+str(round(float(stats['height-calibrated'])))
    f = open("resfile.txt", "w")
    f.write(res)
    f.close()

