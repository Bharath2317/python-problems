lower = int(input("Enter a starting number:"))
upper = int(input("Enter a ending number: "))

print(f"The armstrong numbers between {lower} and {upper} are: ",end=" ")

for num in range(lower,upper+1):
  temp = num
  pow_digit = len(str(num))
  sum_of_pow = 0
  while temp>0:
    last_digit = temp%10
    sum_of_pow += last_digit**pow_digit
    temp //= 10
  if (sum_of_pow==num):
    print(num,end=" ")
