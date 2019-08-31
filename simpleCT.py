#!/usr/bin/env python3
import numpy as np
import matplotlib as plt
import math

print('---Simple CT---')

x = 127 # 256/2 

# original grid of matter
F_orig = np.array(0 0 0 0\
                  0 x 0 0\
                  0 0 x 0\
                  0 0 0 0)

# projections captured. 4 at 45 deg incriments
P = np.array([0 x x 0     0 x x 0    0 x x 0    ? ? ? ?])    

# weights matrix 16x16

# Algebraic Reconstruction Technique
