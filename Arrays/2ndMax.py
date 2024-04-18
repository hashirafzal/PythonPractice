

def SecondMax(arr):
    if len(arr)<=1:
        return "Array value less than 2 , so no 2nd max"
    Max=max(arr[0],arr[1])
    Min=min(arr[0],arr[1])
    for i in range(2,len(arr)-1):
        if arr[i]>Max:
            Min=Max
            Max=arr[i]
        elif arr[i]>Min:
            Min=arr[i]

    return Min


tempArray=[2,3,4,5,61,100,21,32,9,876,76,10]
oneArray=[1]
Array=[]
print(SecondMax(tempArray))
print(SecondMax(oneArray))
print(SecondMax(Array))