import MyTools

puzzle = MyTools.AoC(6,1)


for line in puzzle.readLines():
    dic=[]
    dic_n=[]
    solution_a=0
    solution_b=0

    while len(list(set(sorted(line[solution_a:solution_a+4])))) !=4:
        solution_a+=1
    while len(list(set(sorted(line[solution_b:solution_b+14])))) !=14:
        solution_b+=1
    puzzle.solution(solution_a+4)
    puzzle.solution(solution_b+14)