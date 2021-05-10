def average(L):
    sum=0
    avg=0
    for i in L:
        sum=sum+i
    avg=sum/len(L)
    return avg
    
    
print(average([1,2,3,4]))