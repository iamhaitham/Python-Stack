def maximum(L):
  if len(L)==0:
    return False
  else:
    max=L[0]
    for i in L:
      if i>max:
        max=i
    return max

print(maximum([37,2,1,-9]))
print(maximum([]))