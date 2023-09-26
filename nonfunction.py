###lowest and smallest number of tuple:

a=(1,2,3,5,6,8)
b=list(a)
b[3]=15
print(b)
highest=b[0]
lowest=b[0]
for i in range(len(b)):
    if b[i]>highest:
        highest=b[i]
    else:
        lowest=b[i]
a=tuple(b)
print(a)
print(highest)
print(lowest)
 
###ascending  order in tuple:

a=(4,3,5,7,8,1)
c=list(a)
c[4]=10
print(c)
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]>c[j]):
            c[i],c[j]=c[j],c[i]
a=tuple(c)
print(a)

###descending order:

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]<c[j]):
            c[i],c[j]=c[j],c[i]
a=tuple(c)
print(a)


#nonlocal variable:

def myfunction1():
    x="ocean acadmey"
    def myfunction2():
        x="hello"
    myfunction2()
    return x
print(myfunction1())

def team():
    name="john"
    def points():
        nonlocal name
        name=50
    points()
    return name
print(team())


#nonlocal keyword python:

value=0
def fun1():
    value=5
    def fun2():
        value=7.5;
        def fun3():
            nonlocal value;
            value=10;
            print("fun3:",value)
        fun3();
        print("fun2:",value)
    fun2();
    print("fun1:",value)
fun1();


value=0
def fun1():
    value=5
    def fun2():
        value=7.5;
        def fun3():
            value=10;
            print("fun3:",value)
        fun3();
        print("fun2:",value)
    fun2();
    print("fun1:",value)
fun1();


a=0
def outer():
    a=1
    def inner():
        nonlocal a
        a=10
        print("inner variable value:",a)
    inner()
    print("outer variable value:",a)
outer()
print("global variable value:",a)

###Arbitray arugments(*args):

def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("sum:",sum)
add(3,5)
add(4,5,6,7)
add(1,2,3,5,6)


###no of arugments *args multiple functions:

def multiply(*args):
    x=1
    for i in args:
        x=x*i
    print("the product of the numbers is:",x)
multiply(5,87)
multiply(8,11)
multiply(6,9,4,7)
multiply(2,11,98)







