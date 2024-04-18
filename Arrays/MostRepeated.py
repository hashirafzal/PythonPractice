

def mostRepeated(arr):
    freq_map={}
    for elem in arr:
        if elem in freq_map:
            freq_map[elem]+=1
        else:
            freq_map[elem]=1
  #  print(freq_map)      
    max_freq=0
    max_elem=None
    for elem, freq in freq_map.items():
        if freq>max_freq:
            max_freq=freq
            max_elem= elem
    return max_elem        

                
oneArray=[]
tempArray=[2,3,4,5,61,100,21,32,9,876,76,2,1,1,2,3,6,7,8,9,9,9,9,6,6,6,6,6,6,10]          
print(mostRepeated(oneArray))
print(mostRepeated(tempArray))
    
