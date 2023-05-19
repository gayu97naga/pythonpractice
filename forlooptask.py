#1 1 1 1
#2 2 2 2
#3 3 3 3
#4 4 4 4


##rows=int(input("enter the rows"))
##cols=int(input("enter the cols"))
##for i in range(1,rows+1):
##    for j in range(1,cols+1):
##        print(i, end=" ")
##    print()
#iterator:
##i=1 1=>5 t
##    j=1 1=>5 t
##
##    1
##
##    j=2 2=>5 t
##
##    1 1
##
##    j=3 3=>5 t
##
##    1 1 1
##
##    j=4 4=>5 t
##
##    1 1 1 1
##
##    j=5 5=>5 f
##
##i=2 2=>5 t
##    j=1 1=>5 t
##
##    1 1 1 1
##    2
##
##    j=2 2=>5 t
##
##    1 1 1 1
##    2 2
##
##    j=3 3=>5 t
##
##    1 1 1 1
##    2 2 2
##
##    j=4 4=>5 t
##
##    1 1 1 1
##    2 2 2 2
##
##    j=5 5=>5 f
##
##    1 1 1 1
##    2 2 2 2
##    3 
##
##i=3 3=>5 t
##    j=1 1=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3
##
##    j=2 2=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3
##
##    j=3 3=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3 3
##
##    j=4 4=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3 3 3
##    4
##
##    j=5 5=>5 f
##
##i=4 4=>5 t
##    j=1 1=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3 3 3
##    4 4
##
##    j=2 2=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3 3 3
##    4 4 4
##
##    j=3 3=>5 t
##
##    1 1 1 1
##    2 2 2 2
##    3 3 3 3
##    4 4 4 4
##
##    j=4 4=>5 t
##
##    j=5 5=>5 f



# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


##rows=int(input("enter the rows"))
##cols=int(input("enter the cols"))
##for i in range(1,rows+1):
##    for j in range(1,cols+1):
##        print(j, end=" ")
##    print()


# 1 2 3
# 4 5 6
# 7 8 9

##rows=int(input("enter the rows"))
##cols=int(input("enter the cols"))
##a=0
##for i in range(1,rows+1):
##    for j in range(1,cols+1):
##        a+=1
##        print(a, end=" ")
##    print()





# A B C D E
# F G H I J
# K L M N O
# P Q R S T
# U V W X Y


##rows=int(input("enter the rows"))
##cols=int(input("enter the cols"))
##rows=5
##count=0
##for i in range(rows):
##    for j in range(rows):   
##     print(chr(65 + count),end=" ")
##     count+=1
##    print()




# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E


##rows=int(input("enter the rows"))
##cols=int(input("enter the cols"))
##for i in range(rows):
##    for j in range(cols):
##       print(chr(65+i),end=" ")
##    print()


# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

rows=int(input("enter the rows"))
cols=int(input("enter the cols"))
for i in range(rows):
    for j in range(cols):
        print(chr(65+j),end=" ")
    print()
