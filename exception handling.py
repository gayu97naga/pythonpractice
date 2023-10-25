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



try:
    a=int(input("enter a number1"))
    b=int(input("enter a number2"))
    print(a*b)
except:
    print("error")
else:
    print("no error")
finally:
    print("finally")
print("program completed")

#Exception Handling Using try,except

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

#Catching Specific Exceptions in Python

try: 
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")    
except IndexError:
    print("Index Out of Bound.")


#Python try with else clause
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

#Python try,finally

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Denominator cannot be 0.")
    
finally:
    print("This is finally block.")
