#1.Neon number or not:

#input number=9
#square=9*9=81
#sum=8+1=9
#sum=input number

##num=int(input("enter a number"))
##square=num*num
##print("square of a given number:",square)
##sumofdigits=0
##while square>0:
##    sumofdigits=sumofdigits+square%10
##    square=square//10
##print("sum of the given number:",num)
##if(num==sumofdigits):
##    print("number is neon")
##else:
##    print("number is not neon")



#2.niven number

##num=int(input("enter a number"))
##rem=0
##sum=0
##temp=num
##while(temp>0):
##    rem=temp%10
##    sum=sum+rem
##    temp=temp//10
##print("sum of the given number:",sum)
##if(num%sum==0):
##    print("number is niven")
##else:
##    print("number is not niven")


#3.armstrong number:

#input number=370
#length=3

##number=int(input("enter a number"))
##n=str(number)
##length=len(n)
##print(length)
##original_number=number
##result=0
##while(number>0):
##     rem=number%10
##     result=result+rem**length
##     number=number//10
##print(result)
##if (original_number==result):
##    print("number is armstrong")
##else:
##    print("number is not armstrong")



#4.Factors of numbers:
#number:5 (1,5)

num=int(input("enter a number"))
a=1
while(a<=num):
    if(num%a==0):
        print(a)
    a=a+1
