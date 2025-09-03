def sum_of_array(n):
  total = 0;
  for element in n:
    total += element
  return total

array=list(map(int,input("Enter a list of elemnets seperated by space: ").split())) 

result = sum_of_array(array)

print("The sum of array is",result)
