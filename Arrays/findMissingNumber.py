

def findMissing(arr):
    n=len(arr)

    expectedOutput= (n+1)*(n+2)//2

    actualOutput= sum(arr)

    return expectedOutput-actualOutput

arr=[1,2,3,5,6]
missingNumber= findMissing(arr)
print(missingNumber)