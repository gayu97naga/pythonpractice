#1.parent childclass:

##class ParentClass:
##    def my_method(self):
##        print("this is the parent class method.")
##class ChildClass(ParentClass):
##    def my_method(self):
##        print("this is the child class method.")
##parent=ParentClass()
##child=ChildClass()
##parent.my_method()
##child.my_method()

#2.overridden method:
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

##class Father:
##    def __init__(self):
##        self.property=80000
##    def display_property(self):
##        print("Fathers\property=",self.property)
##class Son(Father):
##    pass
##s=Son()
##s.display_property()


##def getmissNum(arr):
##    n=len(arr)
##    m=n+1
##    total=m*(m+1)//2
##    return total-sum(arr)
##if __name__=="__main__":
##    arr=[1,2,3,4,5,7,8,9,10]
##    print("the missing number is: ")

##class Vehicle:
##    def start(self):
##        print("Vehicle started.")
##class Car(Vehicle):
##    def start(self):
##        super().start()
##        print("Car started.")
##
##car=Car()
##car.start()


##class Animal:
##    name=""
##    def eat(self):
##        print("I can eat")
##
##
##class Dog(Animal):
##    def display(self):
##        print("my name is", self.name)
##labrador=Dog()
##labrador.name="tony"
##labrador=eat()
##labrador.display()
##

#list1:
#max_end3([1, 2, 3]) → [3, 3, 3]

if nums[0] > nums[2]:
        return [nums[0], nums[0], nums[0]]
    else:
        return [nums[2], nums[2], nums[2]]










