def arr_monotonic(arr):
  increasing = decreasing = True

  for i in range(1,len(arr)):
    if(i > arr(i-1)):
      decreasing = False
    if(i<arr(i-1)):
      increasing = False

  return increasing or decreasing

n = list(map(int,input("ENter the array sep by space: ").split()))
if arr_monotonic(n):
  print("Array is monotonic")
else:
  print("It is not monotonoic")  
