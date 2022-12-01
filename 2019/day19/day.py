# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: Fischkopp
"""
import os
import time
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
#input_File= os.path.join(currentpath, "input.txt")
input_File= os.path.join(currentpath, "Example_input.txt")

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            for e in l.split(','):
                print(e)


    
# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )