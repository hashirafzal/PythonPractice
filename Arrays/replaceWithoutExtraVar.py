#METHOD 1
def replace(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

#METHOD 2
def pythonReplace(a,b):
   a,b=b,a
   return a,b

print(replace(5,6))

print(pythonReplace(5,6))