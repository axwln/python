# class Base:
#    def __init__(self):
#        # Protected member
#        self._a = 2
# # Creating a derived class
# class Derived(Base):
#    def __init__(self):
#        # Calling constructor of
#        # Base class
#        Base.__init__(self)
#        print("Calling protected member of base class: ", self._a)
#        # Modify the protected variable:
#        self._a = 3
#        print("Calling modified protected member outside class: ", self._a)
# obj1 = Derived()
 
# obj2 = Base()



#private members




# class Base:
#     def __init__(self):
#         self.a = "Hello"
#         self.__c = "World"
  
# # Creating a derived class
# class Derived(Base):
#     def __init__(self):
  
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
# obj1 = Base()
# print(obj1.a)
# Uncommenting print(obj1.c) will
# raise an AttributeError
  
# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class



#astraction



# from abc import ABC, abstractmethod

# class Animal(ABC):  # Abstract class
#     @abstractmethod
#     def make_sound(self):
#         pass  # Abstract method

# class Dog(Animal):  # Concrete class
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):  # Concrete class
#     def make_sound(self):
#         return "Meow!"

#     # Client code
# dog = Dog()
# cat = Cat()

# print(dog.make_sound())  # Output: Woof!
# print(cat.make_sound())  # Output: Meow!