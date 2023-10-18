#random modules:
#random:

import random
print(random.random())

import random
random.seed(2)
print(random.random())
print(random.random())
print(random.random())

#choice:

import random
mylist=[1,"a",32,"c","d",31]
print(random.choice(mylist))


import random
list1=["apple","banana","cherry"]
print(random.choice(list1))


import secrets
mylist=[1,"a",32,"c","d",31]
print(secrets.choice(mylist))

import random
print(random.randrange(10,20))
list1=["a","b","c","d","e"]
print(random.choice(list1))
random.shuffle(list1)
print(list1)
print(random.random())


#shuffle:

import random
list1=["apple","banana","cherry"]
random.shuffle(list1)
print(list1)


#sample:

import random
list1=["apple","banana","cherry"]
print(random.sample(list1,k=2))


#uniform:

import random
print(random.uniform(20,60))



#math moduels:
#truncated:

import math
print(math.sqrt(25))
print(math.sqrt(16))

#sqrt:

import math
print(math.sqrt(9))

#ceil:

import math
print(math.ceil(1.5))
print(math.ceil(6.9))


#comb:

import math
n=7
k=5
print(math.comb(n,k))

#copisign:

import math
print(math.copysign(5,1))



#datetime modules:

from datetime import datetime
now=datetime.now()
print("current datetime:",now)
print("Type:",type(now))

#convert datetime string format:

from datetime import datetime
now=datetime.now()
datetime_str=now.strftime("%Y-%m-%d %H:%M:%S")
print("datetime String:",datetime_str)


#convert string to datetime in python:

from datetime import datetime
now=datetime.now()
date=now.strftime("%d/%m/%Y")
print("date String:",date)
time=now.strftime("%H:%M:%S")
print("time string:",time)
year=now.strftime("%Y")
print("year String:",year)
month=now.strftime("%m")
print("month String:",month)
day=now.strftime("%d")
print("day String:",day)


