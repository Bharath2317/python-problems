def find_largest_ele(arr):
  if not arr:
    return "Array is empty"
  
  largest_arr = arr[0]
  for element in arr:
    if element>largest_arr:
      largest_arr=element
  return largest_arr

arr = list(map(int,input("ENter the array seperated by spaces: ").split()))
print(f"The largest element in the array is {find_largest_ele(arr)}")    
