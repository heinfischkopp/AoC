# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
import collections
from collections import Counter
tic = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
input_File= os.path.join(currentpath, "input.txt")
#input_File= os.path.join(currentpath, "Example_input.txt")




with open(input_File) as file:
        lines = file.readlines()
        polymer =  lines[0].replace('\n',"")
        print(polymer)
        pairs = {}
        for l in lines[2:]:
            l = l.replace('\n',"").split(' -> ')
            pairs[l[0]]=l[1]
        
        
        
        ##Part A - Doofe Lösung
        for i in range(0,10):
            newPolymer = ""
            for t in range(0,len(polymer)-1):
                splice = polymer[t:t+2]
                if splice in pairs:
                    #print(pairs[splice])
                    newPolymer+=splice[0]+(pairs[splice])
            polymer = newPolymer + splice[1]
            #print("Gen " + str(i) + " :" + polymer)
            #print(len(polymer))
            
            
FILE_NAME = input_File

rules = {}

first = 1
frequencies = Counter()

with open(FILE_NAME, 'r') as file:
    for line in file:
        if first == 1:
            start = line.strip()
            first += 1
        elif first == 2:
            first += 1
        else:
            f, s = line.strip().split(" -> ")
            rules[f] = s

for i in range(len(start)-1):
    frequencies[f'{start[i]}{start[i+1]}'] += 1

STEPS = 40  #change to 10 for part 1

for i in (range(STEPS)):
    new_freqs = frequencies.copy()
    for key, value in frequencies.items():
        if value > 0:
            change = rules[key]
            new_freqs[f'{key[0]}{change}'] += value
            new_freqs[f'{change}{key[1]}'] += value
            new_freqs[key] -= value
    frequencies = new_freqs

letters = Counter()
for key, value in frequencies.items():
    for character in key:
        letters[character] += value

letters[start[0]] += 1
letters[start[-1]] += 1

for key in letters.keys():
    letters[key] //= 2

print(max(letters.values()) - min(letters.values()))    
        
            
            
print(collections.Counter(polymer).most_common(1)[0])            
print(collections.Counter(polymer).most_common()[-1])      
           
# do stuff
elapsed = time.time() - tic
 
print("")
print("time: " + str(elapsed) )