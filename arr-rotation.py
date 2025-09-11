
def left_rotate(arr, d):
    n = len(arr)
    d = d % n 
    return arr[d:] + arr[:d]
def right_rotate(arr, d):
    n = len(arr)
    d = d % n 
    return arr[-d:] + arr[:-d]
arr = [1, 2, 3, 4, 5, 6, 7]
d = int(input("Enter number of rotations: "))

print("Original Array:", arr)
print("Array after Left Rotation:", left_rotate(arr, d))
print("Array after Right Rotation:", right_rotate(arr, d))
