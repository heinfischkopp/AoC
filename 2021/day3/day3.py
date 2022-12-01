# -*- coding: utf-8 -*-


"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
currentpath = os.path.dirname(os.path.realpath(__file__));

input_File= currentpath +   "\\input.txt"


gamma = ""
epsilon = ""


c=[];
with open(input_File) as file:
        lines = file.readlines()
        for i in range(0,len(lines[1])-1):
            print(i)
            a=0;
            for l in lines:
                if l[i] == "1":
                    a+=1
            print("> " +str(a))
            c.append(a)
            if a >= len(lines)/2:
                gamma+="1"
                epsilon+="0"
            else:
               gamma+="0"
               epsilon+="1"     
        print(gamma)        
        p = int(gamma,2) * int(epsilon,2)
        print("gamma : " + str(int(gamma,2)) + " epsilon : " + str(int(epsilon,2)) + "power " + str(p)  )    
        

with open(input_File) as file:
        lines = file.readlines()

#oxy
oxy_list = lines
i=-1
while len(oxy_list) > 1:
    new_list = [];
    i+=1;
    bits=0;
    for e in oxy_list:
        if e[i] == "1":
            bits+=1
    if bits >= len(oxy_list)/2:
        c="1"
    else:
        c="0"
        
    #print(" c " + c + " "+ str(bits))    
    for e in oxy_list:
        if e[i] == c:
            new_list.append(e)
            
    oxy_list = new_list
    #print(oxy_list)
print('oxy: ' + str(int(oxy_list[0],2)))

#co2
co_list = lines
i=-1
while len(co_list) > 1:
    new_list = [];
    i+=1;
    bits=0;
    for e in co_list:
        if e[i] == "1":
            bits+=1
    if bits < len(co_list)/2:
        c="1"
    else:
        c="0"
        
    print(" c " + c + " "+ str(bits))    
    for e in co_list:
        if e[i] == c:
            new_list.append(e)
            
    co_list = new_list
    print(co_list)
print('c02: ' + str(int(co_list[0],2)))

print("life " + str(int(co_list[0],2) * int(oxy_list[0],2)))