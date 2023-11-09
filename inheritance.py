#1.parent childclass:

class ParentClass:
    def my_method(self):
        print("this is the parent class method.")
class ChildClass(ParentClass):
    def my_method(self):
        print("this is the child class method.")
parent=ParentClass()
child=ChildClass()
parent.my_method()
child.my_method()




#2.Create a Cricle class and intialize it with radius. Make two methods getArea and getperimeter inside this class.

class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius**2*3.14
  def getperimeter(self):
    return 2*self.radius*3.14
NewCircle=Circle(8)
print(NewCircle.getArea())
print(NewCircle.getperimeter())



###3.overridden method:
##
##class ChildClass(ParentClass):
##    def overridden_method(self):
##        super().method_name(arguments)
##class ParentClass:
##    def my_method(self):
##        print("this is the parent class method.")
##class ChildClass(ParentClass):
##    def my_method(self):
##        super().my_method(arguments)
##        print("this is the child class method.")
##parent=ParentClass()
##child=ChildClass()
##parent.my_method()
##child.my_method()





















