# -*- coding: utf-8 -*-


"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import re

currentpath = os.path.dirname(os.path.realpath(__file__));

input_File= currentpath +   "\\input.txt"

class Found(Exception): pass
class bingosheet():
    def __init__(self):
        self.felder=[]
        self.won=False
    
    def addrow(self,row):
        r=row.split()
        l=[]
        for z in r:
            l.append(int(z))
        self.felder.append(l)
        #print(self.felder)
        self.orignialfelder = self.felder
        
    def checkwin(self, last):
        if self.won:
            return True
            
        for l in range(0,len(self.felder)):
            if self.felder[l][1] == 'X' and self.felder[l][2] == 'X' and self.felder[l][3] == 'X' and self.felder[l][4] == 'X' and self.felder[l][0] == 'X':
                self.won = True
                if last:
                    raise Found
                return True
                
        for k in range(0,len(self.felder[l])):
            if self.felder[0][k] == 'X' and self.felder[1][k] == 'X' and self.felder[2][k] == 'X' and self.felder[3][k] == 'X' and self.felder[4][k] == 'X':
                self.won = True
                if last:
                    raise Found
                return True 
                
        #if self.felder[0][0] == 'X' and self.felder[1][1] == 'X' and self.felder[2][2] == 'X' and self.felder[3][3] == 'X' and self.felder[4][4] == 'X':
          #  return True 
            
        #if self.felder[0][4] == 'X' and self.felder[1][3] == 'X' and self.felder[2][2] == 'X' and self.felder[3][1] == 'X' and self.felder[4][0] == 'X':
         #   return True 
            
        return False
        
    def printSheet(self):
        for l in self.felder:
            print (l)
        print("\n")
        
    def numberCall(self,number):
        for l in range(0,len(self.felder)):
            for k in range(0,len(self.felder[l])):
                if number == self.felder[l][k]:
                    self.felder[l][k] = "X"
                    
    def caclulateScore(self):
        n=0;
        for l in range(0,len(self.felder)):
            for k in range(0,len(self.felder[l])):
                if "X" != self.felder[l][k]:
                    n+=int(self.felder[l][k])
        print(' N ' + str(n))
        return n
                
with open(input_File) as file:
        lines = file.readlines()
        x=round(len(lines[1:])/6)
        print("Spielfelder:" + str(x))
        bingosheets=[]
        lastboard = False
        for i in range(0,x): 
            #print(lines[(i)*6+2])
            B = bingosheet()
            print(i)
            B.addrow(lines[(i)*6+2])
            B.addrow(lines[(i)*6+3])
            B.addrow(lines[(i)*6+4])
            B.addrow(lines[(i)*6+5])
            B.addrow(lines[(i)*6+6])
            
            bingosheets.append(B)         
        zahlen= lines[0].split(",")
        try:
            for z in zahlen[:-1]:
                print("ziehe " + str(z))
                wb=0;
                for b in bingosheets:
                     b.numberCall(int(z))
                     #b.printSheet()
                     
                     #Teil A
                     #if b.checkwin():
                         # print("Gewonne " + str(z))
                         #  raise Found Teil A
                     #Teil B
                     b.checkwin(lastboard)
                         # print("Gewonne " + str(z))
                        
                     
                     
                     if b.won:
                         wb+=1;
                         
                if wb == x-1:
                    lastboard = True;
                         
                         
        except Found:
            b.printSheet()
            score = b.caclulateScore() * int(z)
            print("Score " + str(score))