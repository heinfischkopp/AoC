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

openingSymbols="{([<"
closingSymbols="})]>"

points={")":3, "]":57, "}":1197, ">":25137}
points_B={")":1, "]":2, "}":3, ">":4}

Pairs={"<":">","(":")","[":"]","{":"}"}


ErrorCounter=0
Part_B = []


with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            Stack=[]
            
            for e in l:
                #print(Stack, e )
                if e != "\n":
                    if e in openingSymbols:
                        Stack.append(e)
                        #print("open - " + e)
                    elif e in closingSymbols:
                        #print (Stack," - ",e)
                        #print("close - " + e)
                        if e == Pairs[Stack[-1]]:
                            #print("poped   -" + Pairs[Stack[-1]])
                            Stack.pop()
                            
                        else:
                            #print("Error - " + e)
                            ErrorCounter += points[e]
                            break
                    else:
                        print("ähm -" + e)
                else:
                    print("--")
                    print(Stack)
                    Score_B = 0
                    while Stack:
                        Score_B = Score_B*5 + points_B[Pairs[Stack[-1]]]
                        Stack.pop()
                    Part_B.append(Score_B)
                    print(Score_B)

Part_B=sorted(Part_B)
print(Part_B)
    
# do stuff
elapsed = time.time() - t
 
print("lösung A " + str(ErrorCounter))
print("lösung B " + str(Part_B[int((len(Part_B))/2)]))
print("")
print("time: " + str(elapsed) )

