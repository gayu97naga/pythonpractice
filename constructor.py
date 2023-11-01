##class Student:
##    school_name="ABC school"
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##    def show(self):
##        print("Student:",self.name,self.age,Student.school_name)
##    def change_age(self,new_age):
##        self.age=new_age
##    def modify_school_name(cls,new_name):
##        cls.school_name=new_name
##s1=Student("Harry",12)
##s1.show()
##s1.change_age(14)
##Student.modify_school_name("xyz school")
##s1.show()



#1.Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

##class Circle():
##  def __init__(self,radius):
##    self.radius = radius
##  def  getArea(self):
##    return 3.14*self.radius*self.radius
##  def getCircumference(self):
##    return self.radius*2*3.14



#2.Create a Student class and initialize it with name and roll number. Make methods to :

##class student:
##    def __init__(self,name,age,rollno,mark1,mark2,mark3):
##        self.name=name
##        self.age=age
##        self.rollno=rollno
##        self.mark1=mark1
##        self.mark2=mark2
##        self.mark3=mark3
##    def displayinfo(self):
##        print("name:",self.name)
##        print("age:",self.age)
##        print("rollno:",self.rollno)
##        print("mark1:",self.mark1)
##        print("mark2:",self.mark2)
##        print("mark3:",self.mark3)
##        print("total mark:",self.total())
##        print("Average marks:",self.Average())
##    def total(self):
##        return(self.mark1+self.mark2+self.mark3)
##    def Average(self):
##        return(self.mark1+self.mark2+self.mark3)/3
##name=input("enter the name: ")
##age=int(input("enter the age: "))
##rollno=int(input("enter the rollno: "))
##mark1=int(input("enter the mark1: "))
##mark2=int(input("enter the mark2: "))
##mark3=int(input("enter the mark3: "))
##s1=student(name,age,rollno,mark1,mark2,mark3)
##s1.__init__(name,age,rollno,mark1,mark2,mark3)
##s1.displayinfo()

#2.Create a Temprature class. Make two methods :

class Temprature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

celsius=12
farenhiet=((celsius*9))/5+32
print("Temprature  in farenhiet is:  ")
print(farenhiet)

#3.Create a Time class and initialize it with hours and minutes.

class Time():
  def __init__(self,hours,mins):
    self.hours=hours
    self.mins=mins
  def addTime(t1,t2):
    t3=Time(0,0)
    if t1.mins+t2.mins>60:
        t3.hours=(t1.mins+t2.mins)/60
    t3.hours=t3.hours+t1.hours+t2.hours
    t3.mins=(t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
    return t3
  def displayTime(self):
      print("Time is",self.hours,"hours and",self.mins,"minutes.")
  def displayMinute(self):
      print(self.hours*60)+self.mins
a=Time(2,50)
b=Time(1,20)
c=Time.addTime(a,b)
c.displayTime()
c.__init__displayMinute()     
