n = int(input("Enter a number: "))

flag = False

if(n==1):
  print("1 is neither a prime nor a composite number")

elif(n>1):
  for i in range(2,n):
    if(n%i == 0):
      flag = True
      break
  if flag:
    print(f"{n} not a prime number")
  else:
    print(f"{n} is a prime Number")  



