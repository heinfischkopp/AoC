import MyTools

puzzle = MyTools.AoC(17)

for line in puzzle.readLines():
    print(line)
    puzzle.toc(line)

puzzle.solution("A")
puzzle.solution("B")