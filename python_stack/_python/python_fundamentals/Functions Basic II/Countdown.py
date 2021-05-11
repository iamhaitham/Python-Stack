def countdown(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list
    
    
x=countdown(5)
print(x)