#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.area of a cricle
import math
r=float(input("enter a value of r "))
a=math.pi*(r**2)
print("the ares of cricle=",a)


# In[ ]:


#2.area of a regular polygon
import math
n=int(input("enter  the no of sides of polygon "))
l=float(input("enter the length  of each side of polygon "))
a=(n*(1**2))/(4*math.tan(math.pi/n))
print("the area of resgular polygon=",a)


# In[ ]:


#3.the area of segment of circle
import math
t=float(input("enter the angle measure"))
r=float(input("enter the radius of circle"))
if t>=360:
    print("the angle is not possible")
else:
    a=(math.pi*(r**2)*(t/360))-((1/2)*(r**2)*math.sin((t*math.pi)/180))
    print("the area of segment=",a)


# In[ ]:


#4.random number from the list
import random
print("the random number from the list is ")
print(random.choice([100,1,2,3,30,40]))


# In[ ]:


#5.random numbers b/w 1 to 10000 with difference 50
import random
print("the random numbers between 1 to 10000",random.randrange(1,10000,50))


# In[ ]:


#6.calculating using math module
import math
print("the vaue of sin(60) is",math.sin(60))
print("the value of cos(pi) is",math.cos(math.pi))
print("the value of tan(90) is ",math.tan(90))
print("the value of sin(0.8660254037844386)is ",math.degrees(math.asin(0.8660254037844386)))
print("the value of 5^8 is",5**8)
print("the value of squareroot of 400 is",math.sqrt(400))
print("the value of 5^e is",5**math.e)
print("the value of log(1024) base 2 is",math.log(1024,(2)))
print("the value of log(1024) base 10 is",math.log(1024,(10)))
print("the floor value of 23.56 is ",math.floor(23.56))
print("the ceiling value of 23.56 is ",math.ceil(23.56))


# In[ ]:




