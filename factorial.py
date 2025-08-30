num = int(input("Enter the number you want to do factorial : "))
factorial = 1 
if(num<0):
  print("Factorial of negative numbers is not possible")
elif(num == 0):
  print("Factorial of 0 is 1")
else:
  for i in range(1,num+1):
    factorial *= i
  print(f"The factorial of  {num} is {factorial}")   