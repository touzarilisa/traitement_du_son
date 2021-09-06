#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:43:32 2021
@author: boutin
"""

import numpy as np

#%% Fonction
def quantif(X, A, N):#(input sig, full-scall value, Number of bites)
    X = np.float64(X)
    high = A
    low = -1*A
    q = (high-low)/(2**N)
    Q = np.max(np.array([np.min(np.array([np.floor((X-low)/q), np.ones_like(X)*(2**N-1)]), axis = 0), np.zeros_like(X)]), axis = 0)
    low = low + q/2
    Y = low + q*Q
    return Y, q, Q #(quantization output, quant step, quantizd value (between 0 and 2^log2(N)-1))
