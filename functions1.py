#1.global variables:

x=20
def my_function():
    x=20*30
    print("inside function:",x)
my_function()
print("outside function:",x)



#2.

name="hello bob"
def my_function1():
    global name
    name="hello bob"
    print("inside function:",name)
def my_function2():
    print("inside another function:",name)
my_function1()
my_function2()
print("outside function:",name)


#3.

x=20
def my_function():
    print("inside function:",x)
my_function()
print("outside function:",x)


x="python"
def myfun():
    global x
    x="john"
myfun()
print("my name is " + x)

# global keyword:

x=30
def myfunction():
    global x
    print("global variable x inside fuction:",x)
    return
myfunction()
print("global variable x in global scope:",x)

#changes in global scope:

x=10
def myfun():
    x=10
    x=x*2
    print("x inside fun:",x)
myfun()
print("x in global scope:",x)

#add global fun:

c=10
def add():
    global c
    c=c+10
    print(c)
add()



