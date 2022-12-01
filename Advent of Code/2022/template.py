import MyTools

puzzle = MyTools.AoC(1)

for line in puzzle.readLines():
    print(line)
    puzzle.toc(line)

puzzle.solution("A")
puzzle.solution("B")