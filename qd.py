import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminent = b**2 - 4*a*c

if(discriminent>0):
  root1 = (-b+math.sqrt(discriminent))/(2*a)
  root2 = (-b-math.sqrt(discriminent))/(2*a)
  print(f"The roots are {root1} and {root2}")
elif(discriminent==0):
  root = (-b)/(2*a)
  print(f"root is {root}") 
else:
  realpart = -b/2*a
  imaginary = math.sqrt(abs(discriminent))/(2*a)
  print(f"roots are {realpart}+{imaginary}i  and {realpart}-{imaginary}i")   
