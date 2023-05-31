#check the prime number

num=int(input("enter the number"))
count=0
if num==1:
    print("its not prime number")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            count=1
            break
    if(count==1):
        print("its not prime number")
    else:
        print("its prime number")

    
#prime number:

start=int(input("enter the start value"))
stop=int(input("enter the stop value"))
for i in range(start,stop+1):
    if (i>1):
        count=0
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i,end=" ")
