# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));

input_File= currentpath +   "/input.txt"

fisch=[0]*9
days=256

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            for e in l.split(','):
                fisch[int(e)]+=1

for i in range(1,days+1):
    newFisch=[0]*9
    for fi in range(0,len(fisch)): 
        if fi == 0:
            newFisch[8]+=fisch[0]
            newFisch[6]+=fisch[0]
        else:
            newFisch[fi-1]+=fisch[fi]
    fisch=newFisch

# do stuff
elapsed = time.time() - t
 
print(sum(fisch))
print("time: " + str(elapsed) )