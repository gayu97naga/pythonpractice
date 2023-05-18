#1.swapping three number:

####a=5
####b=10
####print("the value of a is",a)
####print("the value of b is",b)
####c=a
####a=b
####b=c
####print("swapping three number a is",a)
####print("swapping three number b is",b)


#2. swapping two number:

##a=10
##b=20
##print("the value of a is",a)
##print("the value of b is",b)
##a,b=b,a
##print("swapping number a is",a)
##print("swapping number b is",b)


#3.factorial of a number:

##num=int(input("enter the stop value"))
##factorial=1
##for i in range(1,num+1):
##    factorial=factorial*i
##    print(factorial)
##print("the fact number",factorial)



#4. fibonacci series:

stop=int(input("enter the stop value"))
a=0
b=1
print(a,end="")
print(b,end="")
for i in range(1,stop):
    c=a+b
    print(c,end="")
    a=b
    b=c
    c=a
