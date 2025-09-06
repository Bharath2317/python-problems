
def split_and_add(arr, pos):

    first_part = arr[:pos]
    second_part = arr[pos:]
  
    result = second_part + first_part
    return result

arr = [1, 2, 3, 4, 5, 6, 7]
pos = int(input("Enter the position to split the array: "))

print("Original array:", arr)
print("Modified array:", split_and_add(arr, pos))
