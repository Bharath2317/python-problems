import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = math.gcd(num1,num2)

print(f"the HCF of {num1} and {num2} is {hcf}")