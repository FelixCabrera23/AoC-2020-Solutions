#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:25:32 2020

@author: walberto

Advent of Programing Day 1
"""

import numpy as np

# unpaking data

data = np.loadtxt('input.txt')

for x in data:
    for y in data:
        if (x+y)==2020:
            z = x*y
            
        
        for w in data:
            if (x+y+w)==2020:
                k = x*y*w
                
                
print('Part 1 =',z)
print('Part 2 =',k)