import MyTools

puzzle = MyTools.AoC(10)

solution_a=0
stack=[1]
x=1
Screen=""

def printScreen(S):
    for i in range(40,260,40):
        print(S[i-40:i])

for line in puzzle.readLines():
    l=line.split()
    match l[0]:
        case "noop":
            stack.append(x)

        case "addx":
            stack.append(x)
            stack.append(x)
            x+=int(l[1])

for i in range(20,221,40):
    solution_a+=i*stack[i]
puzzle.solution(solution_a)

for j in range(240):
    if abs(j%40-stack[j+1])<=1:
        Screen+="#"
    else:
        Screen+="."

printScreen(Screen)
puzzle.solution("Puzzle B")