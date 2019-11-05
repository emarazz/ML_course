# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np

def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    poly = np.ones((len(x),degree+1))
    poly[:,1] = x
    for j in range(2,degree+1):
        poly[:,j] = np.power(x,j)
    return poly
    # ***************************************************
    #raise NotImplementedError
