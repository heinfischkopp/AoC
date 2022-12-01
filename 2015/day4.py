import MyTools
import hashlib
  
# encoding GeeksforGeeks using md5 hash
# function 


puzzle = MyTools.AoC(4,1)

for line in puzzle.readLines():
    print(line)
    i=0
    while 1:
        i +=1
        input = line+str(i)
        if puzzle.puzzle == 'A' and hashlib.md5(input.encode()).hexdigest()[:5] == '00000':
            puzzle.solution(i)
        elif hashlib.md5(input.encode()).hexdigest()[:6] == '000000':
            puzzle.solution(i)
            break

