# -*- coding: utf-8 -*-


"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
currentpath = os.path.dirname(os.path.realpath(__file__));

input_File= currentpath +   "\\input.txt"

horizontal=0
depth = 0
with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            l=l.split()
            print(l[0])
            if "forward" in l[0]:
                horizontal+= int(l[1])
            elif "down" in l[0]:
                depth+= int(l[1])
            elif "up" in l[0]:
                depth-= int(l[1])
            
print("A depht " + str(depth) + " hor: " + str(horizontal) + "Prod " + str(depth*horizontal))    
                
horizontal=0
depth = 0
aim=0
with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            l=l.split()
            print(l[0])
            if "forward" in l[0]:
                horizontal+= int(l[1])
                depth += aim * int(l[1]) 
            elif "down" in l[0]:
                aim+=int(l[1])
            elif "up" in l[0]:
                aim-=int(l[1])
            print (horizontal,depth,aim)
print("depht " + str(depth) + " hor: " + str(horizontal) + "Prod " + str(depth*horizontal))    