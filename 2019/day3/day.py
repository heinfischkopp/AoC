# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
input_File= os.path.join(currentpath, "input.txt")
#input_File= os.path.join(currentpath, "Example_input.txt")

l=0
p=[]

crosspoint=[]

with open(input_File) as file:
        lines = file.readlines()
        
        P_LR=0
        P_UD=0

        p.append((P_LR,P_UD))
        for e in lines[0].split(','):

            if e[0]=="U":
                for i in range(0, int(e[1:])):
                    P_UD+=1
                    p.append((P_LR,P_UD))
            elif e[0]=="D":
                for i in range(0, int(e[1:])):
                    P_UD-=1
                    p.append((P_LR,P_UD))
            elif e[0]=="L":
                for i in range(0, int(e[1:])):
                    P_LR-=1
                    p.append((P_LR,P_UD))
            elif e[0]=="R":
                for i in range(0, int(e[1:])):
                    P_LR+=1
                    p.append((P_LR,P_UD))
                    
        P_LR=0
        P_UD=0
        
       # print(p)
        
        for e in lines[1].split(','):
            
            if e[0]=="U":
                for i in range(0, int(e[1:])):
                    P_UD+=1
                    x=(P_LR,P_UD)
                    if x in p:
                        crosspoint.append(abs(P_LR)+abs(P_UD))
                    
            elif e[0]=="D":
                for i in range(0, int(e[1:])):
                    P_UD-=1
                    x=(P_LR,P_UD)
                    if x in p:
                        crosspoint.append(abs(P_LR)+abs(P_UD))
            elif e[0]=="L":
                for i in range(0, int(e[1:])):
                    P_LR-=1
                    x=(P_LR,P_UD)
                    if x in p:
                        crosspoint.append(abs(P_LR)+abs(P_UD))
            elif e[0]=="R":
                for i in range(0, int(e[1:])):
                    P_LR+=1
                    x=(P_LR,P_UD)
                    if x in p:
                        crosspoint.append(abs(P_LR)+abs(P_UD))
print(crosspoint)

print(min(crosspoint)) 

                        
# do stuff
elapsed = time.time() - t
 

print("")
print("time: " + str(elapsed) )