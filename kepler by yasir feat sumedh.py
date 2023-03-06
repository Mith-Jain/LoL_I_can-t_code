import random 
import math
def func(x):
    return 1/math.sqrt(1 + x**2) #This is the equation you get when you solve 1/r^2 potential and assume the constants to be 1
l = [] # To store the values
begin = 1 #This will be our first point u(1/r) values
for j in range(1,51): #Plotting 50 points
    res = 0 # Count of points satisfying the condition
    for i in range(100000):
        x = 1 + 0.1*j*random.random() # To iteratively get x = 1 - 1.1, then 1 - 1.2, till 1 - 6
        y = 10*random.random() #Taken the y range possibilites from 0 to 10 so we get a rectange of area j 
        if y < func(x): #Condition for being in the region 
            res += 1
    begin += 0.1 #updating the u values to store in a list
    l.append((begin ,j*res/100000)) #storing the values and multiplying by j as it was the total area 
for k in l:
    print((1/k[0], k[1])) #1/k[0] as we want r not u.


