# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import re
currentpath = os.path.dirname(os.path.realpath(__file__));

input_File= currentpath +   "\\input.txt"


with open(input_File) as file:
    lines = file.readlines()
    n=1000
    feld= [ [0]*n for i in range(n)]
           
    for l in lines:
        l = re.sub('\n', '', l)
        p = l.split(" -> ")
        x1,y1  = p[0].split(",")
        x2,y2  = p[1].split(",")
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)

        dx=x2-x1
        if dx != 0:
            dx=int(dx/abs(dx))
    
        dy=y2-y1        
        if dy != 0:
            dy=int(dy/abs(dy))
            
        x=x1
        y=y1
        while x !=x2 or y != y2:
            feld[x][y] += 1
            x=x+dx
            y=y+dy
            
        feld[x][y] += 1
        
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in feld]))
      
l=0;
for a in feld:
    for b in a: 
        if b >= 2:
            l+=1
print(l)