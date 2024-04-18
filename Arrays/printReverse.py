
def reversePrint(arr):
 for i in range(len(arr)-1,-1,-1):
  print(arr[i])


newArray=[2,3,4,5,6]
print(reversePrint(newArray))

x= list(reversed(newArray))
print(x)
