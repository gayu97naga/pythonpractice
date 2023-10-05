##choc={"diarymilk":{"Almond":{"quatity":5,"price":[5,10,15]},
##                   "nuts":{"quatity":5,"price":[5,15,20]}},
##      "milkbar":{"stawberry":{"quatity":50,"price":[5,10,15]},
##                 "venila":{"quantity":25,"price":[5,15,15]}}
##
##    }
##print(choc.keys())
##print(choc["diarymilk"].keys())
##print(choc["diarymilk"]["Almond"].keys())
##print(choc["diarymilk"]["Almond"]["price"][0])
##
###user input:
##
##choc={}
##length=int(input("enter the length of dictionary"))
##for i in range (length):
##    keysvalue=input("enter the key value")
##    choc[keysvalue]={}
##    length1=int(input("enter the length1"))
##    for i in range (length1):
##        keysvalue1=input("enter the key value1")
##        choc[keysvalue][keysvalue1]={}
##        length1=int(input("enter the length1"))
##        for i in range(length1):
##            if(i%2==0):
##                keysvalue2=input("enter the keysvalue2")
##                choc[keysvalue][keysvalue1][keysvalue2]=input("enter the value")
##            else:
##                keysvalue2=input("enter the key value2")
##                listrange=int(input("enter the range"))
##                choc[keysvalue][keysvalue1][keysvalue2]=[]
##                for i in range(listrange):
##                    inputvalue=int(input("enter the value"))
##                    choc[keysvalue][keysvalue1][keysvalue2].append(inputvalue)
##print(choc)
                


choc={"diarymilk":[5,10,20],"kitkat":[5,10,15],"lolipop":[5,10,15]}
print(choc.keys())

#user input:


choc={}
length=int(input("enter the length of dictionary"))
for i in range (length):
    keysvalue=input("enter the key value")
    choc[keysvalue]={}
    for i in range (length1):
        if(i%2==0):
            keysvalue2=input("enter the keysvalue2")
            length1=int(input("enter the length1"))
                for i in range (length2):
                    keysvalue1=input("enter the key value1")
                    choc[keysvalue][keysvalue1]={}



##dict1={"diarymilk":[5,10,25],"kitkat":[5,10,15],"lolipop":[5,10,15]}
##print(dict1)
##length=int(input("enter the length of dictionary"))
##print("welcome to the shop")
##for dict1 in range(length):
##    keysvalues1=input("what do want choclate")
##    dict1[keysvalues]=input("yes is cholate is avaiable")
##    print("enter the quantity")
