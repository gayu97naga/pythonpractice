#regular ex:

import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


import re
pattern = '^a...a$'
test_string ='alies'
result = re.match(pattern,test_string)
if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")


#re.findall()

import re
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string) 
print(result)


import re
string='shfgkusuyiwtiu'
pattern='[a-z]{5}'
result=re.findall(pattern,string)
print(result)



#re.split()


import re
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string) 
print(result)



import re
string='546shfgkusuyiwtiu587'
pattern='[a-z]{5}'
result=re.split(pattern,string)
print(result)



import re
string="Simple is better than complex."
obj=re.findall(r"ple", string)
print (obj) 


import re
string="Simple is better than complex."
obj=re.findall(r"\w*", string)
print (obj)   
