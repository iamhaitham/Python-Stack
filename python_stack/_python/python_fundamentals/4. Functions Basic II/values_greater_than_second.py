list=[5,2,3,2,1,4]


def values_greater_than_second(listName):
    newList=[]
    count=0
    if len(listName)<2:
        return False
    else:
       for i in range(0,len(listName)):
            if listName[i]>listName[1]:
                newList.append(list[i])
                count=count+1
                
    print(count)   
    return newList
            
test=values_greater_than_second(list)
print(test)