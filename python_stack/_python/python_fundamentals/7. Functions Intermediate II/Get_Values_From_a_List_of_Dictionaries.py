def iterateDictionary2(key_name, some_list):
  for i in range(0,len(some_list),1):  
    print(f"{some_list[i][key_name]}")  
  
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    
print(iterateDictionary2("first_name", students))
print(iterateDictionary2("last_name", students))