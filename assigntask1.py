#assignment operator

num=-7
num1=8
num2=9
num-=num1
num1+=-5
num*=6
num-=-12
num1/=6
num1-=6
num2%=8
print(num)
print(num1)
print(num2)


num1=0.7
num2=6
num3=-4
num1-=-5
num1**=num2
num1-=7
num2+=8
num2-=0
num2+=num3
num3-=num1
print(num1)
print(num2)
print(num3)


#membership operator

string=input("enter the string name")
userinput=input("enter the character your are going to check")
print(userinput in string)
print(userinput not in string)


string="gaythri"
print("g"in string)
print("d"in string)
print("a"not in string)


#identity operator
#imutable datatype
#integer

int1=20
int2=20
print(id(int1))
print(id(int2))
print(int1 is int2)
print(int1 is not int2)

#float

float1=2.5
float2=1.5
print(id(float1))
print(id(float2))
print(float1 is float2)
print(float1 is not float2)

      




