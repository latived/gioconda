"""
This file contains utility methods that I have used or I am using for deep learning,
more especifically medical imagem segmentation.

Qua, 31 Out 2018
"""

import os
import zipfile
import functools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl

from PIL import Image

mpl.rcParams['axes.grid'] = False
mpl.rcParams['figure.figsize'] = (12, 12)

proj_root = None
db_folder = None
raw_train_dir = None
raw_label_dir = None
p1_train_dir = None
p1_label_dir = None

def set_imgs_dirs():
    # Change to directory with dataset (this notebook location)
    proj_root = '/content/drive/My Drive/Projetos/Colab/polyp_segmentation/'

    # Defining actual folder and new folder where only useful images will go
    db_folder = os.path.join(proj_root, "CVC-ColonDB/CVC-ColonDB/CVC-ColonDB/")

    # Raw
    raw_train_dir = os.path.join(proj_root, "raw/train")
    raw_label_dir = os.path.join(proj_root, "raw/train_masks")

    # Processed: cropped
    p1_train_dir = os.path.join(proj_root, "proc_1/train")
    p1_label_dir = os.path.join(proj_root, "proc_1/train_masks")

    dirs = {'raw': [raw_train_dir, raw_label_dir], 'processed' : [p1_train_dir, p1_label_dir] }

    return dirs

def _create_check_dirs(dirs):
    for k in dirs.keys():
        for d in dirs[k]:
            if not os.path.exists(d):
                os.makedirs()
            else:
                print("{} already created.".format(d))


def unzip_colondb(filename):
    if os.path.exists(filename) and not os.path.exists(db_folder):
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            unzipped_file = zip_ref.namelist()[0]
            zip_ref.extractall(unzipped_file)
    else:
        print("{} already extracted.".format(filename))

    # Wait?
    assert os.path.exists(db_folder), "{} doesn't exists.".format(db_folder)
    # Originals, mask and contour images + .DStore = 1141 files
    assert len(os.listdir(db_folder)) == 1141, "Not all files have been extracted!"


"""
 Defining frames full names:
     Original images have <id>.tiff
     Mask images have p<id>.tiff
"""
def get_img_names(extension):

    filenames_original = dict()
    filenames_mask = dict()

    # Each interval from i to s defines a sequence of frames
    # For example: sequence 1 goes from 1.tiff to 39.tiff (same for its polyp masks)
    sequences = [1, 2, 3, 5, 6, 7, 9, 10, 11, 14, 15]
    inf_limits = [1, 39, 61, 77, 98, 149, 156, 204, 209, 264, 274]
    sup_limits = [39, 61, 77, 98, 149, 156, 204, 209, 264, 274, 301]
    limits = [(i, s) for (i, s) in zip(inf_limits, sup_limits)]

    # Actually, the images are in .tiff format, but soon we will have to use .jpeg

    for (seq, lim) in zip(sequences, limits):
        filenames_original[seq] = ['.'.join([str(id), extension])
                                   for id in range(lim[0], lim[1])]
        filenames_mask[seq] = ['.'.join(['p' + str(id), extension])
                                   for id in range(lim[0], lim[1])]

    # Checking the corretude of the file names
    assert filenames_original[1][0] == "{}.{}".format(1, extension)
    assert filenames_mask[1][0] == 'p{}.{}'.format(1, extension)

    return filenames_original, filenames_mask


