# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
tic = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
input_File= os.path.join(currentpath, "input.txt")
#input_File= os.path.join(currentpath, "Example_input.txt")

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            l = list(map(int, l.split(',')))
            felder = [0]*(int(max(l)+1)) 
            for e in l:
                felder[int(e)]+=1

print("time1: " + str(time.time() - tic) )
                
for tiefe in range(0, len(felder)):
    kraftstoff=0
    #print("time2: " + str(time.time() - tic) )
    for i in range(0, len(felder)): 
        
        if felder[i] > 0:
            #part a
            #kraftstoff+= felder[i] * abs(i-tiefe)
            # part b
            kraftstoff+= felder[i] * (abs(i-tiefe)+1)*2/1

    if tiefe == 0 or kraftstoff < m_kraftstoff:
        m_kraftstoff = kraftstoff
        m_tiefe = tiefe
    
                

# do stuff
print(m_kraftstoff)
print(m_tiefe)
 
print("")
print("time: " + str(time.time() - tic) )