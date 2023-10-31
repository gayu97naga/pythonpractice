#Employee details:

##class Employee:
##    name="gayathri"
##    e_no=6548
##    designation="data science"
##    salary=25000
##    address="pondy"
##    email="gayu97naga@gmail.com"
##    mobile=5465215478
##    def details(self):
##        print("name:\t\t",self.name)
##        print("e_no:\t\t",self.e_no)
##        print("designation:\t",self.designation)
##        print("salary:\t\t",self.salary)
##        print("address:\t",self.address)
##        print("email:\t\t",self.email)
##        print("mobile:\t\t",self.mobile)
##obj=Employee()
##obj.details()


#student information:

class Student:
    school_name="ABC school"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Student:",self.name,self.age,Student.school_name)
    def change_age(self,new_age):
        self.age=new_age
    def modify_school_name(cls,new_name):
        cls.school_name=new_name
s1=Student("Harry",12)
s1.show()
s1.change_age(14)
Student.modify_school_name("xyz school")
s1.show()
