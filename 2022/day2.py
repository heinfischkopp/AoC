import MyTools

puzzle = MyTools.AoC(2)

for line in puzzle.readLines():
    print(line)
    puzzle.toc(line)

puzzle.solution("A")
puzzle.solution("B")