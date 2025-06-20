#print numbers from 1 to 5 using a while loop

# count=1
# while count <= 5:
#     print(count)
#     count += 1
    
    
    
#print even numbers from 1 to 10

# count = 1
# while count <= 10:
#     if count % 2 == 0:
#         print(count)
#     count += 1
    
    
#print numbers from 10 to 1

# count=int(input("enter a number"))
# while count >=1:
#     print(count)
#     count -= 1



#calculator for addition of number of numbers the user enters
# num = int(input("Enter a number: "))
# sum = 0
# while num != -1:
#     sum += num
#     num = int(input("Enter a number : "))
# print("the sum of the number is :", sum)



#sum off diits

# i=int(input("Enter a number: "))
# j=0
# while (i>0):
#     a=i%10
#     j=j+a
#     i=i//10
# print("the sum of the digits is :", j)


#palindrome__________________
# i = input("Enter a number: ")
# j=0
# b=i
# while (b>0):
#     a=(b%10)
#     j=(j*10)+a
#     b=b//10
# if (i==j):
#     print("the number is a palindrome")
# else:
#     print("the number is not a palindrome")


#amstrong number____________________
i= int(input("Enter a number: "))
a=i
j=0
b=len(str(i))
while (i>0):
    b=i%10
    f=f+b**3
    i=i//10
if (a==f):
    print("the number is an amstrong number")
else:
    print("the number is not an amstrong number")