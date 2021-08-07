# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:53:20 2020

@author: 20200342
"""

import matplotlib.pyplot as plt
import numpy as np
import imageio as io

from registration import joint_histogram
from registration import image_transform
from registration import rotate
from registration_util import t2h
from registration import mutual_information


def translate(tx, ty):
    T=np.array([[1,0,tx],[0,1,ty],[0,0,1]])
    return T

# ---------------
# Load data

T1 = translate(0.5,0)
T2 = rotate(0.1)
T2 = t2h(T2, [0,0])

I = io.imread('../data/image_data/3_2_t1.tif')
#J = io.imread('../data/image_data/3_2_t2.tif')

A,_ = image_transform(I,T1)
B,_ = image_transform(I,T2)

# ----------------
# Make joint histograms

A = joint_histogram(I, A, num_bins=32)
B = joint_histogram(I, B, num_bins=32)

# -----------------
# Make figure

f = plt.figure(figsize=(10,5))
ax0 = f.add_subplot(121)
ax1 = f.add_subplot(122)

#A_flip = np.flip(A,0)
#B_flip = np.flip(B,0)

ax0.imshow(A, cmap='plasma', vmin=0, vmax=0.001)
ax1.imshow(B, cmap='plasma', vmin=0, vmax=0.001)

ax0.invert_yaxis()
ax1.invert_yaxis()

ax0.set_title('Transformation A', fontweight="bold")
ax1.set_title('Transformation B', fontweight="bold")

ax0.set(xlabel='Intensity in fixed image', ylabel='Intensity in transformed moving image')
ax1.set(xlabel='Intensity in fixed image', ylabel='Intensity in transformed moving image')

f.tight_layout()

f.savefig('joint_histograms_2.png')