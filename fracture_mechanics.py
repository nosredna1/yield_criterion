#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:18:26 2020

@author: duong
"""

def trans_crack(Kc, sigma_o):
    import numpy as np
    
    at = (1 / np.pi) * (Kc / sigma_o)**2
    
    return at

if __name__ == "__main__":    
    
    Kc = 123
    sigma_o = 1310
    
    at = trans_crack(Kc, sigma_o)
    