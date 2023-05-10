#1. two numbers and mathematical operator:

num1=int(input("enter the first no of value num1"))
num2=int(input("enter the second no of value num2"))
add=num1+num2
print("addition",add)

#2.leap year:

year=int(input("enter the year"))
if(year%4==0):
    print("the year is leap",year)
else:
    print("the year is not leap",year)
