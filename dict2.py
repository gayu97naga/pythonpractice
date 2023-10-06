
##find the sum of all items:

dict1={"a":100,"b":200,"c":300}
sum=0
for x in dict1:
    sum=sum+dict1[x]
print(sum)
dict2={"x":25,"y":18,"z":45}
sum=0
for x in dict2:
    sum=sum+dict2[x]
print(sum)
    

##username and pwd login dictionary:

dict1={"abi":[5264],"ben":[1002],"bob":[4025],"john":[2005]}
username=input("enter the username")
if username in dict1:
    print("username is correct")
    pwd=input("enter the pwd")
    pwdlist=dict1.get(username)
    if pwd in pwdlist:
        print("pwd is successfully login")
    else:
        print("your pwd is incorrect")
else:
    print("your enter valid username and pwd")




           
           






    
