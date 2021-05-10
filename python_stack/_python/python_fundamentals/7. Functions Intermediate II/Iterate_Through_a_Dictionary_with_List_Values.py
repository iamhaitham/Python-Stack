def printInfo(some_dict):
  for i in some_dict:
    print("{} {}".format(len(some_dict[i]),i.upper()))
    for j in some_dict[i]:
      print("{}".format(j))
        
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
