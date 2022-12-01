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

karte=[]
x=0
y=0

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            karte.append([])
            for e in l.split('\n')[:-1]:
                for z in e: 
                    #print(z)
                    karte[x].append(int(z))
                y+=1
            x+=1
    
# do stuff
elapsed = time.time() - t
 

Loesung_1 = 0;

for i in range(0,len(karte)):
    for j in range (0, len(karte[0])):
        #print(i,j)
        if (i == 0 or karte[i][j] < karte[i-1][j]) :
            if (i == len(karte)-1 or karte[i][j] < karte[i+1][j]):
                if (j == 0  or karte[i][j] < karte[i][j-1]):
                    if (j == len(karte[i])-1 or karte[i][j] < karte[i][j+1]):
                        print(i,j,karte[i][j])
                        Loesung_1 += 1 + karte[i][j]

print(Loesung_1)

print("")
print("time: " + str(elapsed) )



with open(input_File) as f:
    heightmap = []
    for line in f.read().splitlines():
        heightmap.append([int(i) for i in line])

h = len(heightmap)
w = len(heightmap[0])

def adjacent(j, i):
    return set([(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(h-1)), i), (j, i+1 - 2*(i==(w-1)))])

r1 = 0
low_points = []
for j in range(h):
    for i in range(w):
        if all([heightmap[j][i] < heightmap[y][x] for y, x in adjacent(j, i)]):
            r1 += 1 + heightmap[j][i]
            low_points.append((j, i))

print(r1)

def size(j, i, visited):
    if (j, i) not in visited:
        visited.append((j, i))
        return 1 + sum([size(y, x, visited) if 9 > heightmap[y][x] > heightmap[j][i] else 0 for y, x in adjacent(j, i)])
    else:
        return 0

sizes = []
for p in low_points:
    sizes.append(size(p[0], p[1], []))

sizes = sorted(sizes)[-3:]
print(sizes[0] * sizes[1] * sizes[2])