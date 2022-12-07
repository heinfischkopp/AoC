import MyTools

puzzle = MyTools.AoC(22)

for line in puzzle.readLines():
    print(line)
    puzzle.toc(line)

puzzle.solution("A")
puzzle.solution("B")