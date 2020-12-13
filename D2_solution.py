#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:23:43 2020

@author: walberto

Advent of Programing Day 2
"""
import numpy as np

# unpaking data

data = np.loadtxt('input.txt',dtype=str)

# valid_passwords = np.array([])

i = 0
j = 0

for line in data:
    # First need to determin the lims
    lims = line[0].split('-')
    low, up = int(lims[0]), int(lims[1])
    # then we dermin the key letter
    key = line[1].split(':')[0]
    # then we isolate the password
    password = line[2]
    
    # Validating: (part 1)
    x = password.count(key)
    if (x>=low) and (x<=up):
        i += 1
        # valid = True
        # valid_passwords = np.append(valid_passwords,list(line))
        
    # Validating: (part 2)
    valid = False
    letters = list(password)
    # Positions:
    a,b = low-1,up-1
    #Logic variables
    L1 = letters[a]==key
    L2 = letters[b]==key
    if not(L1 and L2):
        valid = L1 or L2
    if (valid):
        j+=1
    
        
print('valid passwords (part 1) = ',i)
print('valid passwords (part 2) = ',j)
    
    