#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:28:08 2020

@author: walberto

Advent of Programing Day 4
"""
# unpaking data
file = open('input.txt')
lines = file.readlines()
file.close()

Passports = [] #Empty list of passports

i = 0

while i < len(lines):
    passi = []
    while i < len(lines):
        if lines[i] == '\n':
            i += 1
            break
        passi.append(lines[i])
        i += 1
    Passports.append(passi)
    
# Validation:
    
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def Validate (Pass):
    
    """
    This function chechks if a passport is valid by comparing the list of
    required fields whit the filds contained in the passport
    
    Returns True or False
    """
    
    Valid = True
    # Getting items from a passport
    items = []
    for item in Pass:
        sublist = []
        x = item.split()
        for field in x:
            sublist.append(field)
        for part in sublist:
            y = part.split(':')
            items.append(y[0])
    
    # Validating
    
    for item in fields:
        Valid = item in items
        if not Valid:
            break
        
    return (Valid)

# Part 1, Counting valid passports

n = 0

# for passport in Passports:
#     valid = Validate(passport)
#     if valid:
#         n += 1
        
# print('Part 1: Number of valid passports =',n)


# Part 2

byr = [1920,2002] # limits
iyr = [2010,2020] # limits
eyr = [2020,2030] # limits
#hgt
cm = [150,193] #lims
inn = [59,76]
hcl = '1234567890abcdef'
ecl = ['amb','blu','brn','gry','grn','hzl','oth']
pid = '0123456789'
def Validate2 (Pass):
    
    """
    This function chechks if a passport is valid by comparing the list of
    required fields whit the filds contained in the passport
    
    Returns True or False
    """
    
    Valid = True
    # Getting items from a passport
    items = []
    for item in Pass:
        sublist = []
        x = item.split()
        for field in x:
            sublist.append(field)
        for part in sublist:
            y = part.split(':')
            y[1] = y[1].split('\n')[0]
            items.append(y[0])
    
            # Validating
            # works
            if y[0] == 'byr':
                z = int(y[1])
                Valid = (z>=byr[0] and z<=byr[1])
            # wokrs
            if y[0] == 'iyr':
                z = int(y[1])
                Valid = (z>=iyr[0] and z<=iyr[1])
            # works
            if y[0] == 'eyr':
                z = int(y[1])
                Valid = (z>=eyr[0] and z<=eyr[1])
            # works    
            if y[0] == 'hgt':
                z = list(y[1])
                if ('c'in z and 'm' in z):    
                    w = int(y[1].split('cm')[0])
                    Valid = (w>=cm[0] and w<=cm[1])
                elif ('i' in z and 'n' in z):
                    w = int(y[1].split('in')[0])
                    Valid = (w>=inn[0] and w<=inn[1])
                else:
                    Valid = False
            # works
            if y[0] == 'hcl':
                z = list(y[1])
                Valid = (z[0] == '#' and len(z) == 7)
                if Valid:
                    z.pop(0)
                    w = list(hcl)
                    for char in z:
                        Valid = char in w
                        if not Valid:
                            break
            # works
            if y[0] == 'ecl':
                Valid = y[1] in ecl
            # works
            if y[0] == 'pid':
                z = list(y[1])
                w = list(pid)
                if len(z) == 9:
                    for char in z:
                        Valid = char in w
                        if not Valid:
                            break
                else:
                    Valid = False
                
            if not Valid:
                break

        if not Valid:
            break
        
    # Rechecking for complitness
    for item in fields:
        Valid2 = item in items
        if not Valid2:
            break
    Valid = Valid and Valid2
        
    return (Valid)

n = 0
for passport in Passports:
    valid = Validate2(passport)
    if valid:
        n += 1
        
print('Part 2: Number of valid passports =',n)