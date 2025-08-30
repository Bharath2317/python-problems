num = int(input("Enter number of terms : "))

a,b = 0,1
count =0
if(num<=0):
  print("Please enter a positive number.")
elif(num==1):
  print("The fibonacci sequence of 1 term is: ",end= " ")  
  print(a)
else:
  while count<num:
    print(a,end=" ")
    next_term = a+b
    a = b
    b = next_term
    count += 1


