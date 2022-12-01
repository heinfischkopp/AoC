# -*- coding: utf-8 -*-

"""
Created on Wed Dec  1 16:59:02 2021

@author: 
"""
import os
import time
from math import sqrt
t = time.time()

currentpath = os.path.dirname(os.path.realpath(__file__));
input_File= os.path.join(currentpath, "input.txt")
#input_File= os.path.join(currentpath, "Example_input.txt")

with open(input_File) as file:
        lines = file.readlines()
        for l in lines:
            for e in l.split(','):
                if "x" in e:
                    x_target_start, x_target_end = e.split("=")[1].split("..")
                    print(x_target_start)
                if "y" in e:
                    y_target_start, y_target_end = e.split("=")[1].split("..")
            

v_x = 7
v_y = 2


xmin=int(x_target_start)
xmax=int(x_target_end)

ymin=int(y_target_start)
ymax=int(y_target_end)

# Min vx_0 to never undershoot :
# x_t_inf >= xmin
#  => vx_0(vx_0+1)/2 >= xmin
#  => vx_0 >= (sqrt(8*xmin+1)-1)/2
vx_0_min = int((sqrt(8*xmin+1)-1)/2)

# Max vx_0 to never overshoot :
# x_0 <= xmax
#  => vx_0 <= xmax
vx_0_max = xmax

# Min vy_0 to never undershoot :
# y_t >= ymin
# => t*vy_0 - t*(t-1)/2 >= ymin
vy_0_min = min(0, ymin)

# Max vy_0 :
# The part of the trajectory where y goes up is symmetric in y : we pass by
# the same y values going up then going down, and also the y speed at each
# point is also symmetric. So, if y(t) = 0, we need y(t+1) >= ymin (assuming
# negative y target) :
# y(t_cross) = 0
# vy(t_cross) = -(vy(0)+1)
# y(t_cross+1) >= ymin
#  => -(vy(0)+1) >= ymin
#  => vy(0) <= -ymin-1
vy_0_max = -ymin-1



Lösung_A = [];

for v_x_t in range(vx_0_min,vx_0_max+1):
    for v_y_t in range(vy_0_min,vy_0_max+1):
        
        
        v_x = v_x_t
        v_y = v_y_t
        
        #print(v_x,v_y)
        
        x_pos=0
        y_pos=0
        max_y_try = 0
        
        while x_pos < int(x_target_end) and y_pos > int(y_target_end):
            x_pos = x_pos + v_x
            y_pos = y_pos + v_y
            
            max_y_try = max(max_y_try,y_pos)
            #print(x_pos, y_pos)
            
            v_x = max(v_x-1,0)
            v_y -= 1
            
            if x_pos in range (int(x_target_start),int(x_target_end)+1) and y_pos in range (int(y_target_start),int(y_target_end)+1):
                #print ("treffer")
                #print(v_x_t,v_y_t)
                Lösung_A.append(max_y_try)
                break
            
            
    
print ("Lösung A: ")
print(max(Lösung_A))
    
print ("Lösung b: ")
print(len(Lösung_A))

#print((Lösung_A))

# do stuff
elapsed = time.time() - t
 
print("")
print("time: " + str(elapsed) )


allmaxy = 0
count = 0
for vx_0 in range(vx_0_min, vx_0_max+1):
  for vy_0 in range(vy_0_min, vy_0_max+1):
    t = x = y = maxy = 0
    vx = vx_0; vy = vy_0
    while x <= xmax and y >= ymin:
      x += vx; y += vy
      vx = vx-1 if vx > 0 else 0
      vy -= 1
      maxy = max(maxy, y)
      if x <= xmax and x >= xmin and y >= ymin and y <= ymax:
        allmaxy = max(allmaxy, maxy)
        count += 1
        break
      t += 1

print("Part one", allmaxy, 1)
print("Part two", count, 2)