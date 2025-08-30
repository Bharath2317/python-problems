def fibonacci_recurr(n):
  if(n<=0):
    return "Invalid! Please enter a positive number"
  elif(n==1):
    return 0
  elif(n==2):
    return 1
  else:
    return fibonacci_recurr(n-1)+fibonacci_recurr(n-2)
  
num = int(input("ENter number of terms : "))
print("The fibonacci sequence is : ",end=" ")
for i in range(1,num+1):
  print(fibonacci_recurr(i),end=" ")  