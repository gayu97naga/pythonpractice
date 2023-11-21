#https://pythondjangorestapi.com/top-50-python-oops-interview-questions-and-answers/




#Class in python
#The class itself is an object. Classes are designed to create class objects. Class objects have attributes(state) and behavior(variables). In class, we can define class variables in which we can store data that are accessible in each instance object. Classes are created with metaclass type. In the example given below, a class named Student has been created.

#ex;
class Student(object):
  pass

print(Student)


#classes created in Python
class Student(object):
  def __init__(self, name):
    self.name = name

S1=Student("Martin")
print(S1.name)

#create an empty class in Python
class Student:
    pass
     
stud=Student()
print(stud)

#Create an Object

class Student:
  def __init__(self):
    self.name = 'Martin'
    print('You are inside the init method')

  def disp(self):
    print('Student name:',self.name)

stud = Student()
print('type of class:',type(stud),' id of object:',id(stud))
stud.disp()

#constructor in class
class Student:
  def __init__(self, name):
    self.name = name
    print('Name of Student:',self.name)
stud1 = Student('Martin')

class StudMarks:
  def __init__(self, name, marks=80):
    self.name = name
    self.marks = marks
    print('Name of Student:',self.name,' Student Marks:',self.marks)
stud2 = StudMarks('Genny', 70)


#Instance Variable in Python

class Student:
  def __init__(self):
    self.name = 'Martin'
    print('Inside the init method')
  
  def disp(self):
    print('Student Name:',self.name)

stud = Student()
stud.disp()

#Class variable/ Static Variable
class Student:
  standard = '5th'
  def __init__(self):
    self.name = 'Martin'
  
  def disp(self):
    print('Instance Variable:',self.name,' Class variable:',Student.standard)

stud = Student()
stud.disp()
print('Class Variable:',Student.standard)

#new method in Python

class Student(): 
  def __new__(cls): 
    print("We are in new method") 
    return super(Student, cls).__new__(cls) 
    
  def __init__(self): 
    print("We are in init method") 

student = Student() 
print(student)

#init in python

#init is a method and constructor of a class in Python. This method is automatically called after memory allocation from the new method. All classes have the init method

#Instance Method in Python

class Student:
  def __init__(self):
    self.name = 'Martin'
    print('You are in init method')

  def disp(self):
    print(self.name)

stud = Student()
stud.disp()

#Class Methods in python
class Student:
  standard = '5th'
  
  @classmethod
  def disp(cls):
    print('Class Variable:',cls.standard)

stud = Student()
Student.disp()

#Static Methods in python

class Student:
  standard = '5th'
  
  @staticmethod
  def disp(name):
    print('Student Name:',name,' Standard:',Student.standard)

stud = Student()
stud.disp('Martin')


#Nested Class in python

class Collage:
  def __init__(self):
    self.name = 'Yale University'
    self.show()
    self.course = self.Course()
  
  def show(self):
    print('College/University:',self.name)
  
  class Course:
    def __init__(self):
      self.name = 'MBA'
      self.seats = 105
      self.disp()
            
    def disp(self):
      print('Course Name:',self.name,' Seats:',self.seats)

college = Collage()


#Inheritance in Python

class Student(object):
  pass
  
class Student:
  pass

#Single Inheritance in Python

class University: 
  def __init__(self): 
    self.name = 'Yele University'
    print("You are in University Class Constructor")

class College (University):
  def show(self):
    print('College class instance method:',self.name)

college = College()
college.show()


#Constructor Overriding in Python

class University: 
  def __init__(self): 
    self.name = 'Yele University'
    print("You are in University Class Constructor")

class College (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')

  def show(self):
    print('College class instance method:',self.name)

college = College()
college.show()


#Super Method in Python

class University: 
  def __init__(self): 
    self.name = 'Yele University'
    print("You are in University Class Constructor")
  
  def disp(self):
    print('You are in University class disp method')

class College (University):
  def __init__(self):
    super().__init__()
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')

  def show(self):
    print('College class instance method:',self.name)

college = College()
college.show()
college.disp()


#Multi-level Inheritance in Python

class University: 
  def __init__(self): 
    self.name = 'Yele University'
    print("You are in University Class Constructor")
  
  def disp(self):
    print('You are in University class disp method')

class College (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')

  def show(self):
    print('College class instance method:',self.name)

class Student(College):
  def __init__(self):
    self.name='Martin'
    print('You are in student Class Constructor')

  def view(self):
    print('Student class instance method:',self.name)

student = Student()
student.view()
student.show()
student.disp()


#Hierarchical Inheritance in Python

class University: 
  def __init__(self): 
    self.name = 'Yele University'
    print("You are in University Class Constructor")
  
  def disp(self):
    print('You are in University class disp method')

class MedicalCollege (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in Medical college Class Constructor')

  def show(self):
    print('Medical College class instance method:',self.name)

class LawCollege (University):
  def __init__(self):
    self.name = 'Yale Law School'
    print('You are in Law college Class Constructor')

  def view(self):
    print('Law College class instance method:',self.name)  

lawcollege = LawCollege()
lawcollege.view()
lawcollege.disp()

medicalcollege = MedicalCollege()
medicalcollege.show()
medicalcollege.disp()


#Multiple Inheritance in Python

class Father:
  def __init__(self):
    print('You are in Father Class Constructor')
  
  def disp(self):
    print("Father Class instance Method")
		
class Mother:
  def __init__(self):
    print("You are in Mother Class Constructor")
  
  def show(self):
    print("Mother Class instance Method")
		
class Son(Father, Mother):
	def __init__(self):
		print("You are in Son Class Constructor")
  
	def view(self):
		print("Son Class Instance Method")
		
		
son = Son()
son.view()
son.show()
son.disp()

#Method Resolution Order (MRO) in Python

class Father:
  def __init__(self):
    print('You are in Father Class Constructor')
  
  def show(self):
    print("Father Class instance Method")
		
class Mother:
  def __init__(self):
    print("You are in Mother Class Constructor")
  
  def show(self):
    print("Mother Class instance Method")
		
class Son(Father, Mother):
	def __init__(self):
		print("You are in Son Class Constructor")
  	
son = Son()
son.show()


#Polymorphism in Python

#Method overloading in Python


#In Python, if a method is written in such a way that it can perform more than one task, then it is called method overloading.


class Calculation:
  def product(self, a=None, b=None):
    if a!=None and b!=None:
      prod = a * b
    elif a!=None and b!=None:
      prod = a * b
    elif a!=None:
      prod = a*a
    else:
      prod = 'Provide at least One Numbers'
    return prod
		
cal = Calculation()
print(cal.product(5, 5))
print(cal.product(6))

#Method Overriding in Python

class University:
  def name(self):
    self.name = 'Yele University'
    print('Name:', self.name)
		
class College(University):
  def name(self):
    super().name()
    self.name = 'Yele Medical college'
    print('Name:', self.name)
		
college = College()
college.name()


#Operator Overloading in python

# Operator Overloading
class A:
	def __init__(self, x):
		self.x = x
	def __add__(self, other):
		return self.x + other.x
			
class B:
	def __init__(self, x):
		self.x = x
		
a = A(100)
b = B(200)
print(a+b)


#Namespace Dictionaries in Python

class College:
  def __init__(self):
    self.name = 'Yele Medical College'

  def disp(self):
    print('Name of College:',self.name)

class Student(College):
  def __init__(self):
    self.name = 'Martin'

  def show(self):
    print('Name of Student:',self.name)

college = College()
print(college.__dict__)
print(college.__class__)
print(Student.__bases__)
print(College.__bases__)

#Encapsulation in python

class Student:
  def __init__(self):
    self.name = 'Martin'
    self._name ='Denny'
    self.__name = 'Michel'

student = Student()
print(student.name)
print(student._name)
#print(student.__name)
print(student._Student__name)

#Strong and Weak References in python

class Student:
    def __init__(self):
        self.name = 'Martin'
        
    def __repr__(self):
        return f'Student(name={self.name})'

student = Student()
stud = student






