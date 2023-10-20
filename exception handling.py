#exception handling:

try:
    a=int(input("enter number1"))
    b=int(input("enter number2"))
    print(a/b)
except:
    print("error")
else:
    print("no error")
finally:
    print("finally")
print("program completed")


x=10
y="a"
try:
    print(x+y)
except:
    print("cannot add string and integer")
else:
    print("try block is executed")
finally:
    print("try or except is excuted")


x=10
y=20
try:
    print(x+y)
except:
    print("cannot add string and integer")
else:
    print("try block is executed")
finally:
    print("try or except is excuted")

try:
    x=int(input("enter a number:"))
    y=10/x
    print("the result is:",y)
except:
    print("you must enter a valid integer.")
else:
    print("try block is executed")
try:
    k=5/0
    print(k)
except:
    print("can't divided by zero")
finally:
    print("this is always executed")










