#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:07:32 2020

@author: duong
"""
import numpy as np

def stress_conv(stress, SI=True):
    """
        Convert ksi to MPa if SI = True, vice versa if SI=False
    """
    if SI == True:
        conv_stress = stresses * 6.89
    else:
        conv_stress = stress / 6.89

    return conv_stress

def principal_stress(sigma_x, sigma_y, sigma_z=0, t_xy=0, t_yz=0, t_zx=0):
    """
       Sigma 1, first index always the greatest stress; sigma 3, last index always
       the smallest stress
    """
    
    I1 = 1
    I2 = -1 * (sigma_x + sigma_y + sigma_z)
    I3 = sigma_x * sigma_y + sigma_y * sigma_z + sigma_z * sigma_x - t_xy**2 \
        - t_yz**2 - t_zx **2
    I4 = -1 * (sigma_x * sigma_y * sigma_z + 2 * t_xy * t_yz * t_zx - sigma_x * \
        t_yz**2 - sigma_y * t_zx**2 - sigma_z * t_xy**2)
        
    coef = [I1, I2, I3, I4]
    
    principal_unsorted = np.roots(coef)
    principal_sorted = np.sort(principal_unsorted)[::-1]
    
    return principal_sorted

def mss(principal_stress, ultimate_strength):
    """
        Max Shear Criterion
    """

    effective_stress = max(abs(principal_stress[0]-principal_stress[1]), \
                           abs(principal_stress[1]-principal_stress[2]), \
                           abs(principal_stress[2]-principal_stress[0]))
    print(effective_stress)
    
    design_factor = ultimate_strength / effective_stress
    return design_factor

def distort_energy(principal_stress, ultimate_strength):
    """
        Distortion Energy, Von Mises
    """
    vonMises_stress = (((principal_stress[0]-principal_stress[1])**2 + \
                       (principal_stress[1]-principal_stress[2])**2 + \
                       (principal_stress[2]-principal_stress[0])**2) / 2)**(0.5)
    print(vonMises_stress)
    
    design_factor = ultimate_strength / vonMises_stress
    return design_factor

def coul_mohr(principal_stress, ultimate_tension, ultimate_compression):
    """
        Coloumb-Mohr Theory for Ductile Materials
    """
    
    design_factor = 1 / (principal_stress[0] / ultimate_tension - \
                         principal_stress[2] / ultimate_compression)
   
    
    return design_factor

if __name__ == "__main__":    
    Sy = 303
    
    sigma_x = -100
    sigma_y = -100
    sigma_z = -100
    t_xy = 60.6
        
    prince = principal_stress(sigma_x, sigma_y, sigma_z, t_xy, 0, 0)
    
    df_mss = mss(prince, Sy)

    
    













