# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
#input_File= os.path.join(currentpath, "input.txt")
input_File= os.path.join(currentpath, "Example_input.txt")

x=-1
karte=[]
with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            x+=1
            karte.append([])
            for e in l.split('\n')[0]:
                for z in e: 
                    ident= str(x) + " " + str(len(karte[x]))  
                    karte[x].append(z)

print(karte)
    


import heapq
import fileinput

# Ripped from day 9
def get_neighbors(x, y, grid):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            vals.append((nx, ny))
    return vals

def expand_grid(grid):
    rows, cols = len(grid), len(grid[0])
    big_grid = []
    for y in range(rows * 5):
        row = []
        for x in range(cols * 5):
            bx, by = x % cols, y % rows
            x_offset = x // cols
            y_offset = y // rows
            new_val = grid[y % cols][x % rows] + (x // cols) + (y // rows)
            while new_val > 9:
                new_val -= 9
            row.append(new_val)
        big_grid.append(row)
    return big_grid

def dijkstra(grid):
    start = (0, 0)
    end = (len(grid[0])-1, len(grid)-1)
    dist_heap = [(0, start)]
    visited = set()

    while dist_heap:
        dist, curr = heapq.heappop(dist_heap)
        if curr in visited:
            continue
        visited.add(curr)
        if curr == end:
            return dist

        for n in get_neighbors(curr[0], curr[1], grid):
            # Python's heapq can't update positions, so just push
            # everything and skip any repeats when popping
            n_cost = grid[n[1]][n[0]] + dist
            heapq.heappush(dist_heap, (n_cost, n))



print(dijkstra(karte))
big_grid = expand_grid(karte)
print(dijkstra(big_grid))



# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )