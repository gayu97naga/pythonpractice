#1.two numbers and operations:









#2.leap year:

##year=int(input("enter the year:"))
##if(year%400==0) and (year%100==0):
##    print("0 is leap year",year)
##elif(year%4==0) and (year%100!=0):
##    print("0 is leap year",year)
##else:
##    print("0 is not leap year",year)


#1.current bill:

unit=int(input("enter the units"))
if(unit<=100):
    print("there is no charge")
elif(unit<=200):
    a=((unit-100)*5)
    print("next 100 units price",a)
elif(unit>200):
    b=((unit-200)*10)+500
    print("after 200 units",b)
else:
    print("total bill ammount is 2000")
