import MyTools
import itertools
import numpy as np

puzzle = MyTools.AoC(8)
bäume=[]
i=0
for line in puzzle.readLines():
    bäume.append([])
    for t in line:
        bäume[i].append(int(t))
    i+=1    
dx=len(bäume)
dy=len(line)
bäume=np.array(bäume)

solution_a =0
for x,y in itertools.product(range(dx),range(dy)):
    if x == 0 or y==0 or x == dx-1 or y == dy-1:
        solution_a +=1 
        continue
    
    if np.all(bäume[x,:y] < bäume[x,y]) or np.all(bäume[:x,y] < bäume[x,y]) or np.all(bäume[x+1:,y] < bäume[x,y]) or np.all(bäume[x,y+1:] < bäume[x,y]) :
        solution_a +=1 
puzzle.solution(solution_a)

solution_b =0
for x,y in itertools.product(range(1,dx-1),range(1,dy-1)):
    up=0
    down=0
    left=0
    right=0

    for yi in range (y-1,-1,-1):
        up+=1
        if bäume[x,yi]>=bäume[x,y]:
            break

    for yi in range (y+1,dy):
        down+=1
        if bäume[x,yi]>=bäume[x,y]:
            break

    for xi in range (x-1,-1,-1):
        left+=1
        if bäume[xi,y]>=bäume[x,y]:
            break

    for xi in range (x+1,dy):
        right+=1
        if bäume[xi,y]>=bäume[x,y]:
            break

    if up*down*left*right > solution_b:
        solution_b = up*down*left*right

puzzle.solution(solution_b)