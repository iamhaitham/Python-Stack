def count_positives(L):
    count=0
    for i in range(0,len(L),1):
        if L[i]>0:
            count=count+1
        
    L[len(L)-1]=count
    
    return L
    
    
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))