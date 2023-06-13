#1.lowest and smallest number of tuple:

a=(1,2,3,5,6,8)
b=list(a)
b[3]=15
print(b)
highest=b[0]
lowest=b[0]
for i in range(len(b)):
    if b[i]>highest:
        highest=b[i]
    else:
        lowest=b[i]
a=tuple(b)
print(a)
print(highest)
print(lowest)
    
#2.ascending  order in tuple:

a=(4,3,5,7,8,1)
c=list(a)
c[4]=10
print(c)
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]>c[j]):
            c[i],c[j]=c[j],c[i]
a=tuple(c)
print(a)
##
###descending order:

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i]<c[j]):
            c[i],c[j]=c[j],c[i]
a=tuple(c)
print(a)



