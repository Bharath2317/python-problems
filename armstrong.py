def armstrong(num):
  if num<0:
    return False
  original = num
  num_digits = len(str(num))
  arm_sum = 0

  while num>0:
    last_digit = num%10
    arm_sum += last_digit**num_digits
    num = num//10

  return arm_sum == original

try:
  n = int(input("Enter a number: "))
except ValueError:
  print("Invalid! Please enter a valid number")

if(n<0):
  print("Please enter a positive integer")
elif armstrong(n):
  print(f"{n} is an armstrongnuber")
else:
  print(f"{n} is NOT an armstrong number")    
