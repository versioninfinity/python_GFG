import array

print("\n")


arr = array.array('i', [1,2,3,4,5])

print ("The new created array is : ", end="")


for i in range (0,5):
	print (arr[i],end=" ")

print("\r")

# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2));

print("The array after popping is : ",end="")
for i in range(len(arr)):
	print(arr[i],end=" ")

print("\r")

print("The index of element 2 is : ", end="")
print(arr.index(2))

print("\n")




arr2 = array.array('i',[1,2,3,4,5])
print("The new arr2 is: ", end="")
for i in range(len(arr2)):
	print(arr2[i],end=" ")

print("\n")



