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
                

#user input:
##chocolatelist={"diarymilk":[5,10,20],"kitkat":[5,10,15],"lolipop":[5,10,15]}
##
##length=int(input("enter the length of dictionary"))
##chocolatename=input("enter the chocolate name")
##if(chocolatename in chocolatelist):
##    customerchioce=int(input("enter the chocolate price"))
##    pricelist=chocolatelist.get(chocolatename)
##    if customerchioce in pricelist:
##        noofchocolate=int(input("enter the no of chocolate do you want"))
##        print("price",noofchocolate*customerchioce)
##    else:
##        print("chocolate is not available in that price")
##else:
##    print("not available")
##
##print(chocolatelist)




#fromkeys:
p=("p1","p2","p3","p4")
q=5
myDict=dict.fromkeys(p,q)
print(myDict)

#remove:
programLanguages={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
if 3 in (programLanguages):
    programLanguages[5]
    print(programLanguages)

#pop:

programLanguages={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
print(programLanguages.pop(4))
print(programLanguages)






