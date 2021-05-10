def ultimate_analysis(L):
  sum=0
  avg=0
  min=L[0]
  max=L[0]
  for i in L:
    if i>max:
      max=i
    if i<min:
      min=i
    sum=sum+i
  avg=sum/len(L)
  
  D={"sumTotal":sum,
  "average":avg,
  "minimum":min,
  "maximum":max,
  "length":len(L)}
    
  return D

print(ultimate_analysis([37,2,1,-9]))