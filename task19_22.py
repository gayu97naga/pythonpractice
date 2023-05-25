##rows=int(input("enter the row value"))
##for i in range(1,rows+1):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()
##    
##rows=int(input("enter the row value"))
##for i in range(rows+1,0,-1):
##    for j in range(1,i):
##        print("*",end=" ")
##    print()


##rows=int(input("enter the row value"))
##for i in range(rows):
##    for j in range(i):
##        print(" ",end=" ")
##    for j in range(rows,i,-1):
##        print("*",end=" ")
##    print()
##
##
##rows=int(input("enter the row value"))
##for i in range(2,rows+1):
##    for j in range(0,rows-i):
##        print(" ",end=" ")
##    for k in range(0,i):
##        print("*",end=" ")
##    print()


##rows=int(input("enter the row value"))
##for i in range(rows,0,-1):
##    for j in range(rows,i,-1):
##        print(end=" ")
##    for j in range(0,i):
##        print("*",end=" ")
##    print()
##
####rows=int(input("enter the row value"))
##for i in range(1,rows):
##    for j in range(0,rows-i-1):
##        print(end=" ")
##    for j in range(0,i+1):
##        print("*",end=" ")
##    print()


##rows=int(input("enter the row value"))
##for i in range(1,rows+1):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()
##for i in range(rows,0,-1):
##    for j in range(2,i+1):
##        print("*",end=" ")
##    print()

   
##rows=int(input("enter the row value"))
##for i in range(rows-1):
##    for j in range(1,rows-i):
##        print(" ",end=" ")
##    for j in range(1,i+2):
##        print("*",end=" ")
##    print()
##for i in range(rows):
##    for j in range(i):
##        print(" ",end=" ")
##    for j in range(rows,i,-1):
##        print("*",end=" ")
##    print()


rows=int(input("enter the row value"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(1,rows+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(2*(rows-i)+1):
        print("*",end=" ")
    print()

