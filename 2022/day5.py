import MyTools

puzzle = MyTools.AoC(5,1)
stacks_a =[]
stacks_b =[]
stackinput=[]
start= False
puzzle_a=""
puzzle_b = ""

for line in puzzle.readLines():
    
    if len(line) > 1 and not start:
        stackinput.append(line)
    elif start:
        l = line.split(" ")
        n=int(l[1])
        movefrom=int(l[3])-1
        moveto=int(l[5])-1
        for i in range(0,n):
            stacks_a[moveto].append(stacks_a[movefrom].pop())
        for i in stacks_b[movefrom][-n:]:
            stacks_b[moveto].append(i) 
        del(stacks_b[movefrom][-n:])
    else:
        print(stackinput)
        l=stackinput.pop() #wer bracuht schon indices
        for i in range(1,len(l),4):
            print(i)
            stacks_b.append([])
            stacks_a.append([])
            stacks_b[int(l[i])-1].append(l[i])
            stacks_a[int(l[i])-1].append(l[i])
            for j in range(len(stackinput)-1,-1,-1):
                if stackinput[j][i] != " ":
                    stacks_a[int(l[i])-1].append(stackinput[j][i])
                    stacks_b[int(l[i])-1].append(stackinput[j][i])
        start =True

for s in stacks_a:
    puzzle_a+=s.pop()
for s in stacks_b: 
    puzzle_b+=s.pop()

puzzle.solution(puzzle_a)
puzzle.solution(puzzle_b)