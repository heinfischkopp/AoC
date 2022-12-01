import MyTools

puzzle = MyTools.AoC(1,0)

elvkal = []
n = 0
for line in puzzle.readLines():
    if len(line)==0:
        elvkal.append(n)
        n = 0
    else:
        n += int(line)

elvkal.append(n) #Nur zur Sicherheit Danke Nils
elvkal.sort(reverse=True)

puzzle.solution(elvkal[0])
puzzle.solution(elvkal[0]+elvkal[1]+elvkal[2])