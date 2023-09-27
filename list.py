####odd number of list:

list1=[10,21,4,45,66,93]
for num in list1:
    if num%2!=0:
        print(num,end=" ")
##   
####even number :
##
list1=[10,21,4,45,66,93]
for num in list1:
    if num%2==0:
        print(num,end=" ")
##
####sum of the numbers:

list1=[1,2,3,4,5,6,10]
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
print(sum)

####highest and lowest number of the list:

a=[1,4,3,5,7,8]
highest=a[0]
lowest=a[0]
for i in range(len(a)):
    if a[i]>a[0]:
        highest=a[i]
    else:
        lowest=a[i]
print(highest)
print(lowest)


####user input for list:

a=[]
length=int(input("enter the length list"))
for i in range(length):
    b=int(input("enter the value"))
    a.append(b)
print(a)
              
#integer input only even values given & print the list:

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
for i in range(num1,num2+1):
    if i%2==0:
        print(i,end=" ")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
while num1<num2:
    if num1%2==0:
        print(num1,end=" ")



###delete all repeated elements of the list:

list=[1,2,3,2,1,3,12,12,32]
finallist=[]
for i in list:
    if i not in finallist:
        finallist.append(i)
print(finallist)


list=[4,5,1,2,9,7,10,8]
count=0
for i in list:
    count +=i
average=count/len(list)
print("sum=",count)
print("average=",average)




