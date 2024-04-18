

def Swap(arr):
    first=arr[0]
    last=arr[len(arr)-1]

    arr[len(arr)-1]=first
    arr[0]=last
    return arr


def pythonSwap(arr):
    arr[0],arr[-1]= arr[-1],arr[0]
    return arr

tempArray=[2,3,4,5,6,7]
print("array Before swapping ",tempArray)
print("array after swapping ",Swap(tempArray))
print("array after swapping again ",pythonSwap(tempArray))