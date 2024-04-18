def MoveZeroToLeft(arr):
    left=0
    right=len(arr)-1

    while left<right:
        while arr[right]!=0:
            right-=1
        while arr[left]==0:
            left+=1
        if left<right:
            arr[left],arr[right]= arr[right],arr[left]
            left+=1
            right-=1
    return arr

tempArr=[0,1,4,0,-1,-5,5,4,3,0,2,3,0,10,0,6]

print(MoveZeroToLeft(tempArr))