#elif statement:
    #more than one condition
##a=int(input("enter the value of a"))
##b=int(input("enter the value of b"))
##c=int(input("enter the value of c"))
##if((a>b)and(a>c)):
##    print("A is greater")
##elif(b>c):
##    print("B is greater")
##else: 
##    print("C is greater")

#Nested if
##age=int(input("enter the age"))
##if(age>0):
##    if(age>=18):
##        print("eligible to vote")
##    else:
##        print("not eligible to vote")
##else:
##    print("don't enter the negative value and zero")


#two number and operator:

num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
operator=input("enter the operator")
if operator=="+":
    add=num1+num2
    print("addition",add)
elif operator=="-":
    sub=num1-num2
    print("subtraction",sub)
elif operator=="*":
    mul=num1*num2
    print("multiplication",mul)
elif operator=="/":
    div=num1/num2
    print("division",div)
else:
    print("enter the correct value of num1 and num2")




#leap year:

year=int(input("enter the year to be checked"))
if(year%4==0):
    if(year%100==0):
        print("leap year")
            else:
                print("the is leap year")
                else:
                    print("leap year")
                else:
                    print("not leap year")
