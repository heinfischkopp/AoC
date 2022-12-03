import MyTools
import numpy as np

puzzle = MyTools.AoC(6,1)

state_a = np.zeros((1000,1000), dtype=np.bool)
state_b = np.zeros((1000,1000), dtype=np.int)

for line in puzzle.readLines():
    l=line.split(" ")
    [p2x,p2y] = np.array(l[-1].split(","),dtype = np.int) 
    [p1x,p1y] = np.array(l[-3].split(","),dtype = np.int) 
    befehl= l[-4]
    dx=slice(p1x,p2x+1)
    dy=slice(p1y,p2y+1)
    match befehl:
        case 'on':
            state_a[dx,dy] = True
            state_b[dx,dy] += 1
        case 'off':
            state_a[dx,dy] = False
            state_b[dx,dy] -= 1
            state_b[state_b < 0] = 0
        case 'toggle':
            state_a[dx,dy] ^= True
            state_b[dx,dy] += 2
    
puzzle.solution(sum(sum(state_a)))
puzzle.solution(sum(sum(state_b)))