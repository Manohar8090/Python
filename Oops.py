# class Students:
#     college_name = "ABC College"

#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("adding new students in Database..")

# s1 = Students("Karan", 77)
# print(s1.name,s1.marks)
# print(s1.college_name)

# s2 = Students("Mohit", 85)
# print(s2.name,s2.marks)

# s3 = Students("Golu", 88)
# print(s3.name,s3.marks)

# class Car:
#     color = "Red"
#     brand = "Range Rover"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# Inheritance Method

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type) # super() method is used to access method of the parent class.
#         self.name = name
#         super().start()

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# __init__Function

# Constructor --> all classes have a function called __init__(),
# which is always executed when the class is being initiated.

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# Class method -> 
# A class method is a bound to the class & receive the class as an implict first argument.

# Note - static method can't access or modify class state & generally for utility.

# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.__class__.name = "Rahul"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)

# Property ->
# We use @property decorater on any method in the class to use the method as a property

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property 
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(95, 92, 95)
print(stu1.percentage)

stu1.phy = 85
# print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage)








