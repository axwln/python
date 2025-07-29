#inheritance:

#  1.single = one base class and one derived class

# class Animal:
#     def speak(Self):
#         print("Animal speaking")
# class Dog(Animal):                  //child class Dog inherits the base class Animal
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.speak()
# d.bark()

# 2.multilevel = one base class and multiple derived class, one derived class inherits another derived class

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):                 //the child class Dog inherits the base class Animal
#     def bark(self):
#         print("dog barking")
# class DogChild(Dog):              //the child class DogChild inherits the base class Dog
#     def eat(self):
#         print("Eating bread")
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()

# 3. multiple = multiple parent class and single derived class

# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def subtraction(self,a,b):
#         return a-b
# class Derived(Calculation1,Calculation2):
#     def Multiplication(self,a,b):
#         return a*b
# d=Derived()
# print(d.summation(10,20))
# print(d.subtraction(50,20))
# print(d.Multiplication(3,10))

# 4. hierarchical = single base class and multiple derived class

# class Parent:
#     def func1(self):
#         print("This function is in parent class")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2")
# d=Child1()
# d.func1()
# d.func2()

# c=Child2()
# c.func1()
# c.func3()

# 5. hybrid - 

class Person:
    def display(self):
        print("This is the person class")
class Student(Person):
    def student_info(self):
        print("This is the stucent class")
class Sports:
    def sports_info(self):
        print("This is the sports class")
class SchoolStudent(Student,Sports):
    def school_student_info(self):
        print("This is the SchoolStudent")
s=SchoolStudent()
s.display()
s.student_info()
s.sports_info()
s.school_student_info()