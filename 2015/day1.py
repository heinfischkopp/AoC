import MyTools

puzzle = MyTools.AoC(1)

floor = 0
instruction = 0
for line in puzzle.readLines():
    for i in line:
        instruction += 1 
        if i == "(":
            floor +=1
        elif i == ")":
            floor -=1
        if floor == -1 and not "found" in locals():
            puzzle.solution(instruction)
            found=1

puzzle.solution(floor)