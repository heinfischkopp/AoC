# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
input_File= os.path.join(currentpath, "input.txt")
#input_File= os.path.join(currentpath, "Example_input.txt")


class squid():
    def __init__(self,ID="NA", initValue = 0):
        self.Energy= int(initValue)
        self.FlashedThisRound = False
        self.Nachbarn = []
        self.NumFlashes = 0
        
        self.ID = ID
    
    def AddNchbarn(self, Nachbarn):
        self.Nachbarn.append(Nachbarn)
        
    def HasFlashed(self):
         return self.FlashedThisRound
     
    def neueRunde(self):
        self.FlashedThisRound = False
        
    def IncreseEnergy(self):
            
        if not self.FlashedThisRound:
            self.Energy +=1
            
        if self.Energy > 9:
            self.Energy=0
            self.FlashedThisRound = True
            
            self.NumFlashes += 1
            for n in self.Nachbarn:
                n.IncreseEnergy()
                    
    def AnzNachbarn(self):
        return str(len(self.Nachbarn))
                
    def __str__(self):
        return str(self.Energy)
    
    def __repr__(self):
        return str(self.Energy)
        
karte= []     
x = -1        
with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            x+=1
            karte.append([])
            for e in l.split('\n')[:-1]:
                for z in e: 
                    ident= str(x) + " " + str(len(karte[x]))  
                    karte[x].append(squid(ident,z))
##
for i in range(0,len(karte)):
    for j in range (0, len(karte[0])):
        if (i != 0):
            if (j != 0):
                karte[i][j].AddNchbarn(karte[i-1][j-1])
            if (j != len(karte[i])-1):
                karte[i][j].AddNchbarn(karte[i-1][j+1])  
            karte[i][j].AddNchbarn(karte[i-1][j])
            
        if (i != len(karte)-1):
            if (j != 0):
                karte[i][j].AddNchbarn(karte[i+1][j-1])
            if (j != len(karte[i])-1):
                karte[i][j].AddNchbarn(karte[i+1][j+1])  
                
            karte[i][j].AddNchbarn(karte[i+1][j])
        if (j != 0):
            karte[i][j].AddNchbarn(karte[i][j-1])
        if (j != len(karte[i])-1):
            karte[i][j].AddNchbarn(karte[i][j+1]) 



Anzahlrunden = 100;

# print("#####\ninit")
# print('\n'.join([''.join([str(item) for item in row]) 
#   for row in karte]))
# print("#####")


i=0
allflashed = False
while not allflashed :
    i+=1
    allflashed = True
    for row in karte:
        for s in row:
            allflashed = allflashed and s.HasFlashed()
            s.neueRunde()
    for row in karte:
        for s in row:
            s.IncreseEnergy()

    # print("#####\nRunde " + str(i))
    
    # print('\n'.join([''.join([str(item) for item in row]) 
    #   for row in karte]))

    # print("#####")
    
    if i == 100:
        Lösung_A=0
        for row in karte:
            for s in row:
                Lösung_A += s.NumFlashes
        
print('Lösung A : ' + str(Lösung_A) )
print('Lösung B : ' + str(i-1) )
    
# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )