# make an array with the largest 3 numbers, all are 0. 
# Go through the array, if any element is bigger than any of the 3 elements, 
# replace that element with the new element. Time complexity sshould be O(n) 
# and space complexity should be O(1)

import array

mainarr = [10, 4, 3, 50, 23, 90]

output = [0,0,0]

def print3largest(output, mainarr):
    for each in mainarr:
       # find smallest in output, compare to each
            small = smallest(output)
            output[small] = each
    print(output)
    
def smallest(arr):
    if not arr:
        return None  # Return None for an empty array
    
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    
    return smallest_index

print3largest(output, mainarr)
      


