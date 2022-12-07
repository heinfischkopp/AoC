import MyTools

puzzle = MyTools.AoC(6,1)

for line in puzzle.readLines():
    solution_a=4
    solution_b=14

    while len(list(set(sorted(line[solution_a-4:solution_a])))) !=4:
        solution_a+=1
    while len(list(set(sorted(line[solution_b-14:solution_b])))) !=14:
        solution_b+=1
    puzzle.solution(solution_a)
    puzzle.solution(solution_b)