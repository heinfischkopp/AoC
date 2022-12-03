import MyTools
import numpy as np

puzzle = MyTools.AoC(7,1)
global operators 

class conector:
    def __init__(self,name,operatortype,input1,input2=None):
        self.name = name
        self.input1 = input1
        self.input2 = input2
        self.operator = operatortype
        self.Value = None

    def reset(self):
        self.Value = None

    def getValue(self):
        if not self.Value:
            if self.input1 in operators:
                input1 = operators[self.input1].getValue()
            else:
                input1 = self.input1
            if self.input2 in operators:
                input2 = operators[self.input2].getValue()
            else:
                input2=self.input2

            match self.operator:
                case "-":
                    self.Value = np.uint16(input1)
                case "NOT":
                    self.Value = np.invert(np.uint16(input1))
                case "AND":
                    self.Value = np.bitwise_and(np.uint16(input1),np.uint16(input2))
                case "OR" :
                    self.Value = np.bitwise_or(np.uint16(input1),np.uint16(input2))
                case "RSHIFT" :
                    self.Value = np.right_shift(np.uint16(input2),np.uint16(input1))
                case "LSHIFT" :
                    self.Value = np.left_shift(np.uint16(input2),np.uint16(input1))
        return self.Value

operators = {}          

for line in puzzle.readLines():
    l=line.split(" ")
    if len(l) == 3:
        operators[l[-1]] = conector(l[-1],"-",l[-3])
    elif "NOT" in line:
        operators[l[-1]] = conector(l[-1],l[-4],l[-3])
    else:
        operators[l[-1]] = conector(l[-1],l[-4],l[-3],l[-5])

t1=operators["a"].getValue()
puzzle.solution(t1)
 
for o in operators:
    operators[o].reset()
operators["b"] = conector("b","-",t1)

puzzle.solution(operators["a"].getValue())