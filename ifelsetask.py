#1.senior citizen or not:

age=int(input("enter the age"))
if(age>=60):
    print("you are the senior citizen")

else:
    print("this person is not senior citizen")

#2.odd or even number:

a=int(input("enter the value odd a"))
if(a%2==0):
    print("a is even")

else:
    print("a is odd")


#3.positive or negative number:

a=int(input("enter the value of a"))
if(a>0):
    print("a is postive")

else:
    print("a is negative")

#4.divisible no 3 or not:

a=int(input("enter the value of a"))
if(a%3==0):
    print("3 is divisible number")

else:
    print("he is not divisible number")


#5.divisible no 3,5 number:

a=int(input("enter the value of a"))
if(a%3==0) and (a%5==0):
    print("3 and 5 is divible number")

else:
    print("3 and 5 is not divisible number")



#6.divisible no 7 and not divisible 3:

a=int(input("enter the value of a"))
if(a%7==0)and(a%3==0):
    print("7 and 3 divisible number")

else:
    print("he is not divisible number")

