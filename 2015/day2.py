import MyTools

puzzle = MyTools.AoC(2)

paper = 0
ribbon = 0

for line in puzzle.readLines():
    dim = line.split("x")
    dim = [int(d) for d in dim] 
    
    faces = [dim[0]*dim[2],dim[0]*dim[1],dim[1]*dim[2]]
    dim.sort()

    paper += min(faces)+ 2*sum(faces)
    ribbon += dim[0]*dim[1]*dim[2] + 2*(dim[0]+dim[1])

puzzle.solution(paper)
puzzle.solution(ribbon)