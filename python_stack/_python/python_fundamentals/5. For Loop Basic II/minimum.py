def minimum(L):
 
  if len(L)==0:
    return False 

  min=L[0]    
  for i in L:
    if i<min:
      min=i
  return min
    
print(minimum([37,2,1,-9]))
print(minimum([]))