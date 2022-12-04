import MyTools
from collections import Counter
import re

puzzle = MyTools.AoC(2)

dreier = 0
zweier = 0
boxes = []
for line in puzzle.readLines():
    Num = {} 
    boxID=Counter(line)
    for c in line:
        Num[c]= boxID[c]
    if 2 in Num.values():
        zweier +=1
    if 3 in Num.values():
        dreier +=1

    for i in range(0,len(line)):
        s = line[:i] + "." + line[i+1:]
        if s in boxes:
            puzzle.solution(line[:i] + line[i+1:])
            break
        else:
            boxes.append(s)
puzzle.solution(zweier * dreier)
