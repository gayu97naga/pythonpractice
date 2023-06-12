#1.sum of the numbers:

list1=[1,2,3,4,5,6]
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
print(sum)


#2.highest and lowest number of the list:

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


#3.ascending and descending order for list:

a=[2,8,4,9]
a.sort()
print("Ascending order",a)
a.reverse()
print("Descending order",a)
print(max(a))
print(min(a))

#4. user input for list:
a=[]
length=int(input("enter the length list"))
for i in range(length):
    b=int(input("enter the value"))
    a.append(b)
print(a)
