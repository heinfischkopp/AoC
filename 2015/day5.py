import MyTools

puzzle = MyTools.AoC(5)

solutions = 0

for line in puzzle.readLines():
    nice_1 = 0
    nice_2 = 0
    naugthy = 0
    for notnice in {"ab","cd","pq","xy"}:
        if notnice in line:
            naugthy = 1

    if not naugthy:
        for z in range(len(line[:-1])):
            if line[z] == line[z+1]:
                nice_1=1
            if line[z] in "aeiou":
                nice_2 +=1
        if line[z+1] in "aeiou":
                nice_2 +=1
        if nice_2>=3 and nice_1:
            solutions +=1

puzzle.solution(solutions)

solutions = 0

for line in puzzle.readLines():
    nice_1 = 0
    nice_2 = 0
    
    for i in range(len(line)-1):
        if line[i:i+2] in line[:i] or line[i:i+2] in line[i+2:]:
            nice_1 = 1
        
        if i+2 < len(line) and line[i] == line[i+2]:
            nice_2 = 1
        if nice_1 and nice_2:
            solutions+=1
            break

puzzle.solution(solutions)