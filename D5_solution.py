#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 18:27:46 2021

@author: walberto

Advent of Programing 2020 day 5
"""

# unpaking data
file = open('input.txt')
lines = file.readlines()
file.close()

passes = []

i = 0
while i < len(lines):
    passes.append(lines[i])
    i += 1


def Bin_to_decimal(binary):
    
    number = 0
    
    top = len(binary)
    i = 0
    while i < top:
        part = binary.pop()
        
        if (part == 'B') or (part == 'R'):
            number = number + 2**i
            # print(1,end=(''))
        # else:
            # print(0,end=(''))
        
        i += 1
    # print('')
    return number

def Decode(pass_number):
    code = list(pass_number)
    
    line = code[:-3]
    
    seat = code[-3:]
    
    a = Bin_to_decimal(line)
    b = Bin_to_decimal(seat)
    
    return a*8 + b

# Making a list of all  IDs

IDs = []

for ID in passes:
    a,b = ID.split('\n')
    IDs.append(Decode(a))
    
print(max(IDs))

