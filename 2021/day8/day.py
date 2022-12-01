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

Loesung_A = 0
Loesung_A = 0

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            l = l.split('|')
            n=0
            for s in l[1].split():
                if len(s) == 2 or len(s) == 3  or len(s) == 4  or len(s) == 7 :
                    Loesung_A +=1
                    
print("Loesung_A " + str(Loesung_A))
print("Loesung_B " + str(n))
# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )

import itertools

with open("input.txt") as f:
    s = f.read().strip().split("\n")

c = 0
for line in s:
    a,b = line.split(" | ")
    b = b.split(" ")
    for x in b:
        if len(x) in (2,3,4,7):
            c += 1
print(c)

m = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7,
         "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}

m = {"".join(sorted(k)):v for k,v in m.items()}

ans = 0
for line in s:
    a,b = line.split(" | ")
    a = a.split(" ")
    b = b.split(" ")
    for perm in itertools.permutations("abcdefg"):
        pmap = {a:b for a,b in zip(perm,"abcdefg")}
        anew = ["".join(pmap[c] for c in x) for x in a]
        bnew = ["".join(pmap[c] for c in x) for x in b]
        if all("".join(sorted(an)) in m for an in anew):
            bnew = ["".join(sorted(x)) for x in bnew]
            ans += int("".join(str(m[x]) for x in bnew))
            break
print(ans)