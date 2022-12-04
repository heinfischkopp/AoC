import MyTools
import itertools
import numpy as np

puzzle = MyTools.AoC(9,1)

dist={}
cities={}
bestcase_a = float('inf') 
bestcase_b = 0
for line in puzzle.readLines():
    [c1,t,c2,g,distance] = line.split()
    for c in [c1,c2]:
        if c not in cities:
            cities[c]=len(cities)
    dist[c1,c2] = int(distance)
    dist[c2,c1] = int(distance)

for i in itertools.permutations(cities,len(cities)):
    trip=0
    n=0
    while len(i)-n>1 :
        trip+= dist[i[n+0],i[n+1]]
        n+=1
    if trip < bestcase_a:
        bestcase_a = trip
    if trip > bestcase_b:
        bestcase_b = trip

puzzle.solution(bestcase_a)
puzzle.solution(bestcase_b)