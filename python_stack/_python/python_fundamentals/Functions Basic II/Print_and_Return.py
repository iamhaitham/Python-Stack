def print_and_return(list):
    
    if len(list)==2:
        print(list[0])
    
    return list[1]
    
   
list=[1,2]
#shall print the first index's value and return the second index's value
x=print_and_return(list)
print(x)

#shall just print the first index's value
print_and_return(list) 