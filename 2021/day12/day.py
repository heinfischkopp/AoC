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



Lösung_A = 0
Lösung_B = 0

class Cave:
    def __init__(self,Name):
        self.Name = Name
        self.Wege=[]
        
        if Name == Name.lower():
            self.CaveIsSmall = True 
            #print("Neuen kleine Höhle " + self.Name)
        else:
            self.CaveIsSmall = False 
            #print("Neuen große Höhle " + self.Name)
            
    def addConnection(self, Target):
        self.Wege.append(Target)



def SucheDasEnde(Caves,Standort,Wegbisher):
    global Lösung_A 
    
    if Standort.Name == "end":
        Wegbisher+=Standort.Name
        #print("Lösung für A: " + Wegbisher)
        Lösung_A+=1
        return Wegbisher
    else:
        if Standort.Name in Wegbisher and Standort.CaveIsSmall:
            return 
        
        else:
            Wegbisher+= Standort.Name + ","
            for p in Standort.Wege:
                SucheDasEnde(Caves,p,Wegbisher)
            return
        
def SucheDasEnde2(Caves,Standort,Wegbisher,SmallcaveVisited):
    global Lösung_B 
    if Standort.Name == "end":
        Wegbisher+=Standort.Name
        #print("Lösung für B: " + Wegbisher)

        Lösung_B+=1
        return 
    
    elif Standort.Name == "start":
        if Standort.Name in Wegbisher:
            return
        Wegbisher+= Standort.Name + ","
        for p in Standort.Wege:
            SucheDasEnde2(Caves,p,Wegbisher,SmallcaveVisited)
        return
 
    if Standort.CaveIsSmall:
        if not Standort.Name in Wegbisher:
            Wegbisher+= Standort.Name + ","
            for p in Standort.Wege:
                SucheDasEnde2(Caves,p,Wegbisher,SmallcaveVisited)
            return
        else:
            Wegbisher+= Standort.Name + ","
            if not SmallcaveVisited:
                for p in Standort.Wege:
                    SucheDasEnde2(Caves,p,Wegbisher,True)
            return
    else:
        Wegbisher+= Standort.Name + ","
        for p in Standort.Wege:
            SucheDasEnde2(Caves,p,Wegbisher,SmallcaveVisited)
        return
    

Caves= {}

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            l=l.split('\n')[0]
            l=l.split('-')
            
            
            for c in l:
                if c not in Caves:
                    Caves[c] = Cave(c)
            Caves[l[0]].addConnection(Caves[l[1]])
            Caves[l[1]].addConnection(Caves[l[0]])

            
SucheDasEnde(Caves,Caves["start"],"")
SucheDasEnde2(Caves,Caves["start"],"",False)




print('Lösung A : ' + str(Lösung_A) )
print('Lösung B : ' + str(Lösung_B) )
    

# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )