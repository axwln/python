#odd or even


# def is_even(num):
#     if num%2==0:
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# a=int(input("enter the numer : "))
# is_even(a)

#factorial

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print("factorial of the number is",fact)
# n=int(input("enter the numer"))
# factorial(n)


#leapyear

# def leapyear(num):
#     if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
#         print(num, "is a leap year.")
#     else:
#         print(num, "is not a leap year.")
# year=int(input("Enter the year"))
# leapyear(year)



# def display(name,age):
#     print(f"hello! my name is {name} and i am {age} years old")
    
# display("Aswin",21)


# def display(**a):
#     print(f"hi {a['name']} Welcome to {a['course']} course")

# display(name="jayan",course="python")


# def addition(x,y):
#     print(f"sum of {x} and {y} is = {x+y}")

# def sub(x,y):
#     print(f"subtractig  {y} from {x} is = {x-y}")
    
# def div(x,y):
#     if(y!=0):
#         z=x/y
#         print(z)
#     else:
#         print("undefined")
        
# def multi(x,y):
#     print(x*y)
# while True:
#     print("1. ADDITION")
#     print("2. SUTRARION")
#     print("3. DIVISION")
#     print("4. MULTIPLICATION")
#     print("5. EXIT")
#     choice = int(input("Enter your choice: "))
#     if(choice==1):
#         print(" ADDITION SELECTED")
#         a=int(input("Enter the first number "))
#         b=int(input("Enter the second number "))
#         addition(a,b)
        
#     elif(choice==2):
#         print(" SUTRARION SELECTED")
#         a=int(input("Enter the first number "))
#         b=int(input("Enter the second number "))
#         sub(a,b)
#     elif(choice==3):
#         print(" DIVISION SELECTED")
#         a=int(input("Enter the first number "))
#         b=int(input("Enter the second number "))
#         div(a,b)
#     elif(choice==4):
#         print(" MULTIPLICATION SELECTED")
#         a=int(input("Enter the first number "))
#         b=int(input("Enter the second number "))
#         multi(a,b)
#     elif 5:
#         e=input("do you wish to exit (yes/no)")
#         if e.lower()=="yes":
#             print("Exitig .....")
#             break


#gloal variable

# a=10
# def globvariable():
#        global a
#        a+=20
#        print(a)
# globvariable()


#factorial using recursion

# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)
# print(fact(5))


# def fun():
#     print("hello")
#     fun()
# fun()
 
 
first,second=0,1
print(first,second,end=" ")
for j in range(8):
    third=first+second
    print(third,end=" ")
    first,second=second,third