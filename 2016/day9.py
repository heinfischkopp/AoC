import MyTools

puzzle = MyTools.AoC(9)

for line in puzzle.readLines():
    print(line)
    puzzle.toc(line)

puzzle.solution("A")
puzzle.solution("B")