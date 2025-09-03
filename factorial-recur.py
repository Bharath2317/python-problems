def fact_recur(n):
  if(n==1):
    return n
  else:
    return n*fact_recur(n-1)
  
n = int(input("Enter a number to do factorial: "))  

if(n<0):
  print("Please enter a positive number")
elif(n==0):
  print("The factorial of 0 is 1") 
else:
  print(f"The factorial of {n} is {fact_recur(n)}")   