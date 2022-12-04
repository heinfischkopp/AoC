import MyTools

puzzle = MyTools.AoC(4)
part_a = 0
part_b = 0
for line in puzzle.readLines():
    [elv1,elv2] = line.split(",")
    [elv1x,elv1y]= elv1.split("-")
    [elv2x,elv2y]= elv2.split("-")
    if (int(elv1x)<=int(elv2x) and int(elv2y)<=int(elv1y))or(int(elv2x)<=int(elv1x) and int(elv1y)<=int(elv2y)):
        part_a +=1
    a=set(range(int(elv1x),int(elv1y)+1))
    b=set(range(int(elv2x),int(elv2y)+1))
    part_b += len(b.intersection(a))>0

puzzle.solution(part_a)
puzzle.solution(part_b)