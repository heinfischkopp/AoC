import MyTools

puzzle = MyTools.AoC(3)

class santa:
    def __init__(self,Name):
        self.pos = (0,0)
        self.Name = Name

    def move(self,dir):
        self.pos = (self.pos[0]+dir[0], self.pos[1]+dir[1])
        return self.pos

def deliver(Drivers):
    visits = [(0,0)]
    step = 0 
    for line in puzzle.readLines():
        for d in line:
            step=(step+1)%len(Drivers)
            match d:
                case "v":
                    dir = [0,-1]
                case "^":
                    dir = [0,1]
                case "<":
                    dir = [-1,0]
                case ">":
                    dir = [1,0]
            pos = Drivers[step].move(dir)
            if pos not in visits:
                visits.append(pos)

    return len(visits)
puzzle.solution(deliver([santa("Santa")]))
puzzle.solution(deliver([santa("Santa"),santa("Rudolph")]))