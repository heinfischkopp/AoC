import MyTools

puzzle = MyTools.AoC(10)

for line in puzzle.readLines():
    newinput = line
    for u in range(0,50):
        print(u)
        inp = newinput
        newinput = ""
        while len(inp)>0:
            nextchar = inp[0]
            inp = inp[1:]
            anz = 1
            while len(inp)>0 and inp[0] == nextchar:
                inp = inp[1:]
                anz +=1
            newinput += str(anz)
            newinput += str(nextchar)

puzzle.solution(len(newinput))
puzzle.solution("B")