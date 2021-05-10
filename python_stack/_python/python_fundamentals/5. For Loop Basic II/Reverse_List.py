def reverse_list(L):
  
  temp=0
  
  for i in range(0,int(len(L)/2),1):
    temp=L[i]
    L[i]=L[len(L)-1-i]
    L[len(L)-1-i]=temp
  
  return L

print(reverse_list([37,2,1,-9]))