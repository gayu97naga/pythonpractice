#1.working filter():

letters=["a","b","d","e","i","j","0"]
def filtervowels(letter):
    vowels=["a","e","i","o","u"]
    return True if letter in vowels else False
filtervowels=filter(filtervowels,letters)
vowels=tuple(filtervowels)
print(vowels)



#2.lambda fun inside filter():

numbers=[1,2,3,4,5,6,7]
evennum=filter(lambda x:(x%2==0),numbers)
evennum=list(evennum)
print(evennum)



#3.None as inside filter():

randomlist=[1,"a",0,False,True,"0"]
filter_iterator=filter(None,randomlist)
filterlist=list(filter_iterator)
print(filterlist)



#4.square of numbers:

numbers=[2,4,6,8,10]
def square(numbers):
    return numbers*numbers
squarednumbers=map(square,numbers)
squarednumbers=list(squarednumbers)
print(squarednumbers)


#5.filters():

def calculatesquare(n):
    return n*n
numbers=(1,2,3,4)
result=map(calculatesquare,numbers)
print(result)
numberssquare=set(result)
print(numberssquare)


#6.lambda using filters():

numbers=(1,2,3,4)
result=map(lambda x:x*x,numbers)
print(result)
numberssquare=set(result)
print(numberssquare)


#7.multiple using lambda:

num1=[4,5,6]
num2=[5,6,7]
result=map(lambda n1,n2:n1+n2,num1,num2)
print(list(result))

#8.even number check filters():

def checkeven(number):
    if number%2==0:
        return True
    return False
numbers=[1,2,3,4,5,6,7,8,9,10]
evennumbers=filter(checkeven,numbers)
evennumbers=list(evennumbers)
print(evennumbers)


