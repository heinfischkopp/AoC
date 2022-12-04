import MyTools

puzzle = MyTools.AoC(1)
a=0
b=[0]
for line in puzzle.readLines():
    a+=int(line)
    if a in b:
        puzzle.solution(b)
    else:
        b.append(a)
puzzle.solution(a)
f=0
while not f:
    for line in puzzle.readLines():
        a+=int(line)
        if a in b:
            puzzle.solution(a)
            f = 1
            break
puzzle.solution(a)
