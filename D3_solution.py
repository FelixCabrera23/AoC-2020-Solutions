#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:53:00 2020

@author: walberto

Advent of Programing Day 3
"""

import numpy as np

# unpaking data
file = open('input.txt')
lines = file.readlines()
file.close()

# Number of chars that repeat per line
n1 = len(list(lines[0].split('\n')[0]))

# Setting the origing


trees = 0

# Proces
def test (xs,ys):
    
    x,y = 0,0
    trees = 0
    
    while y < len(lines)-ys:
        
        # moving
        x = x+xs
        y = y+ys
        
        # Selecting the current row
        row = list(lines[y].split('\n')[0])
        
        #if we get over the edge
        if x>(n1-1):
            x = x -n1

        # Chequing if there is a tree
        
        if (row[x] == '#'):
            trees += 1

    return(trees)

# Part 1
print('Part 1:',test(3,1))

