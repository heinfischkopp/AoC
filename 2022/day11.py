import MyTools
import copy
import math
import numpy as np

puzzle = MyTools.AoC(11,1)

Monkeys = []

class Monkey:
    def __init__(self,name):
        self.Name = name
        self.items = []
        self.numChecks = 0

    def addCheck(self,check):
        self.check=int(check)
        
    def addiftrue(self,iftrue):
        self.iftrue=int(iftrue)
        
    def addiffalse(self,iffalse):
        self.iffalse=int(iffalse)
    
    def addOperation(self,operation):
        o=operation.split("=")[1]
        self.Operation=o

    def addItem(self,item):
        self.items.append(item)

    def getItems(self):
        return self.items

    def hasItems(self):
        return len(self.items) >0
    
    def getNumChecks(self):
        return self.numChecks

    def performCheck(self,ggt,partB=False):
        if len(self.items) >=0:
            self.numChecks +=1
            i = self.items.pop()
            if self.Operation== " old * old":
                worry = i*i
            elif "+" in self.Operation:
                worry = i + int(self.Operation.split("+")[1])
            elif "*" in self.Operation:
                worry = i * int(self.Operation.split("*")[1])
        if not partB:
            worry=worry//3
        worry=worry%ggt
        if worry%self.check == 0:
            return [self.iftrue,worry]
        else:
            return [self.iffalse,worry]

kgv=1
for line in puzzle.readLines():
    if len(line.split()) ==2:
        M = Monkey(line.split()[-1])
        Monkeys.append(M)
    if "items" in line:
        for i  in line.split(":")[1].split(","):
            M.addItem(int(i))
    if "Operation" in line:
        M.addOperation(line.split(":")[1])
    if "Test" in line:
        M.addCheck(line.split()[-1])
        kgv=math.lcm(kgv,int(line.split()[-1]))
    if "true" in line:
        M.addiftrue(line.split()[-1])
    if "false" in line:
        M.addiffalse(line.split()[-1])


MonkyinitState = copy.deepcopy(Monkeys)
rounds=[20,10000]
for n in rounds:
    for r in range(n):
        #print("Round :" + str(r))
        for m in Monkeys:
            while m.hasItems():
                [toMonky,item]=m.performCheck(kgv,n==rounds[1])
                if item:
                    Monkeys[toMonky].addItem(item)

    puzzle_a =[]
    for m in Monkeys:
            puzzle_a.append(m.getNumChecks())
    puzzle_a.sort(reverse=True)
    puzzle.solution(puzzle_a[0]*puzzle_a[1])
    Monkeys=MonkyinitState    
