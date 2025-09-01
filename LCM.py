import math
from functools import reduce

numbers = list(map(int,input("Enter the list of numbers seperated by space: ").split()))

def lcm(a,b):
  return abs(a*b//math.gcd(a,b))

def lcm_list(numbers):
  return reduce(lcm,numbers)

result = lcm_list(numbers)

print(f"The LCM of {numbers} is {result}")