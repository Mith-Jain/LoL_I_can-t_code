
import random 
import math
from matplotlib import pyplot as p

def func(x):
  return (1/math.sqrt(1 + x**2)) #This is the equation you get when you solve 1/r^2 potential and assume the constants to be 1

def golden(a,b,func):
  xl=a
  xu=b
  R = (math.sqrt(5) - 1)/2
  d = R*(xu-xl)
  x1 = xl+d
  x2 = xu -d
  exite=0
  
  while exite==0:
    
    if(func(x1)>func(x2)):
      
      xopt=x1
      error = (1 - R)*abs((xu-xl)/xopt)
      xl=x2
      x2=x1
      d=R*(xu-xl)
      x1 = xl + d
    else:
     
      xopt = x2
      error = (1 - R)*abs((xu-xl)/xopt)
      xu=x1
      x1 = x2
      d=R*(xu-xl)
      x2 = xu - d
    if (error<0.0001):
      exite=1
  return xopt

n = 500 #Number of points
l = [] # To store the values
begin = 1 #This will be our first point u(1/r) values
yheight = func(golden(1, 1 + n*0.1,func)) + 10
for j in range(1,n): #Plotting 50 points
    res = 0 # Count of points satisfying the condition
    for i in range(100000):
        x = 1 + 0.1*j*random.random() # To iteratively get x = 1 - 1.1, then 1 - 1.2, till 1 - 6
        y = yheight*random.random() #Taken the y range possibilites from 0 to max + 10 so we get a rectange of area j 
        if y < func(x): #Condition for being in the region 
            res += 1
    begin += 0.1 #updating the u values to store in a list
    l.append((begin ,0.1*j*yheight*res/100000)) #storing the values and multiplying by j as it was the total area 
for k in l:
    p.scatter( math.cos(k[1])/k[0], math.sin(k[1])/k[0] ) #1/k[0] as we want r not u.
p.show()


