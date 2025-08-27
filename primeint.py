lower = int(input("Enter a number to start : "))
upper = int(input("Enter the ending number : "))

print(f'The prime numbers beween {lower} and {upper} are :',end =" ")

for num in range(lower,upper):
  if(num>1):
    for i in range(2,num):
      if(num%i == 0):
        break

    else:
      print(num,end=" ")
    