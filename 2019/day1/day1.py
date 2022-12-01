# -*- coding: utf-8 -*-


"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
currentpath = os.path.dirname(os.path.realpath(__file__));

input_File= currentpath +   "\\input.txt"

b=False
inc=0;
with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            a=int(l) 
            if b:
                if a > b: 
                    inc+=1
            b = a
        print('part a ' + str(inc))
        
inc=0;  
c = False;
liste = []      
with open(input_File) as file:
        lines = file.readlines()
        for i in range(0,len(lines)-2):
            a=int(lines[i])+int(lines[i+1])+int(lines[i+2])
            if c:
                if a > c: 
                    inc+=1
            c = a
        print('part c ' + str(inc)) 