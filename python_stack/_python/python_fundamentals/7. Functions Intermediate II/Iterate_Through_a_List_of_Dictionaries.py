def iterateDictionary(some_list):
  for i in range(0,len(some_list),1):
    for j in some_list[i]:
      print(f"{j} - {some_list[i][j]}",end=", ") 
     
      
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

