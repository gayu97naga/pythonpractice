#1.create dictionary:
alphabetDict={"a":"apple","b":"ball","c":"cat","d":"doll"}
print(alphabetDict)

#2.duplicate items:

num_dict={1:11,2:22,2:22,3:33,4:44,3:33}
print(num_dict)

#3.allow duplicate value:

num_dict={1:11,2:22,3:33,4:44,5:55,6:66}
print(num_dict)

#4.clear values:

clearDict={1:"python",2:"java",3:"c++",4:"php"}
print("Before clearing the dictionary:",clearDict)
clearDict.clear()
print("After clearing the dictionary:",clearDict)

#5.value geting from dict:

program={1:"python",2:"java",3:"c++",4:"php"}
print(program.get(2))
print(program.get(5))


#6.items() methods:

program={1:"python",2:"java",3:"c++",4:"php"}
print(program.items())


#7.keys()methods:

program={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
print(program.keys())

#8.values()methods:

program={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
print(program.values())

#9.pop()methods:

programLanguages={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
print(programLanguages.pop(4))
print(programLanguages)

#10.converting two list in dictionary:

letters=['a','b','c','d','e']
numbers=[1,2,3,4,5]
myDict=dict(zip(letters,numbers))
print(myDict)

#11. del()methods:

programLanguages={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
if 3 in (programLanguages):
    programLanguages[5]
    print(programLanguages)


#12.sort elements:

programLanguages={1:"python",2:"java",3:"c++",4:"php",5:"sql"}
for key in sorted(programLanguages):
    print(key,programLanguages[key])


#13.sum of all values in dict:

myDict={"n1":50,"n2":100,"n3":200}
print(sum(myDict.values()))

#14.fromkey()methods:

p=("p1","p2","p3","p4")
q=5
myDict=dict.fromkeys(p,q)
print(myDict)


#15. min and max values:

myDict={"n1":50,"n2":100,"n3":200,"n4":250}
print(max(myDict.values()))
print(min(myDict.values()))

#16. square of numbers:

squareDict={}
for i in range(1,6):
    squareDict[i]=i**2
print(squareDict)







