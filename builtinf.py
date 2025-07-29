# // Builtin function

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("John",101,22)   //create the object of the student
# print(getattr(s,'name'))   //prints the attribute name of the object s
# setattr(s,"age",23)        //reset the value of attribute age to 23
# print(getattr(s.'age'))    //prints the modified value of age
# print(hasattr(s,'id'))     //print true if the student contains the attribute with name id
# delattr(s,'age')           //deletes the attribute age
# print(s.age)               //this will give an error since the attribute age has been deleted