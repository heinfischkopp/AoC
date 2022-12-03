import MyTools

puzzle = MyTools.AoC(3,1)
score_a = 0
score_b = 0

lines = puzzle.readLines()
for line in lines:
    comon = (set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()
    if comon.islower():
        score_a += ord(comon)-ord("a")+1
    else:
        score_a += ord(comon)-ord("A")+27

while len(lines) > 0:
    comon = (set(lines.pop()) & set(lines.pop())  & set(lines.pop())).pop()
    if comon.islower():
        score_b += ord(comon)-ord("a")+1
    else:
        score_b += ord(comon)-ord("A")+27

puzzle.solution(score_a)
puzzle.solution(score_b)