import MyTools
import re

puzzle = MyTools.AoC(8,1)

strings = 0
characters = 0

for line in puzzle.readLines():
    characters += len(line)
    print(line)
    line =  line[1:-1]
    line = re.sub(r'\\"',r'_',line)
    line = re.sub(r'\\\\',r'_',line)
    line = re.sub(r'\\x[0-9a-fA-Z][0-9a-fA-Z]', '_', line)
    print(line)
    strings += len(line.strip())

puzzle.solution(characters-strings)
puzzle.solution("B")