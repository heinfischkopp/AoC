import MyTools

puzzle = MyTools.AoC(2)

score_A = 0
score_B = 0
symbol_score = {"X":1, "Y":2, "Z":3}
w = {"A":2,"B":3,"C":1}
d = {"A":1,"B":2,"C":3}
l = {"A":3,"B":1,"C":2}

for line in puzzle.readLines():
    s = line.split(" ")
    if (s[0] == "A" and s[1] == "Y") or (s[0] == "B" and s[1] == "Z")  or (s[0] == "C" and s[1] == "X") :
        score_A += 6
    elif (s[0] == "A" and s[1] == "X") or (s[0] == "B" and s[1] == "Y")  or (s[0] == "C" and s[1] == "Z"):
        score_A += 3
    else:
        pass
    score_A+= symbol_score[s[1]]

    match s[1]:
        case "Z": #win
            score_B += 6 + w[s[0]]
        case "Y":#draw
            score_B += 3 + d[s[0]]
        case "X":#lose
            score_B += l[s[0]]
    
puzzle.solution(score_A)
puzzle.solution(score_B)