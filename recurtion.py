#print n to 1

# def rec(num):
#     if num == 1:
#         return str(num)
#     else:
#         return f"{num}, {rec(num - 1)}"

# n = int(input("Enter the number: "))
# print(rec(n))


#sum of n natural numbers

# def sum(num):
#     if num == 1:
#         return num
#     else:
#         return  num+(sum(num - 1))

# n = int(input("Enter the number: "))
# print(sum(n))


#sum of digits

# def sum(n):
#     if n == 0:  
#         return 0
#     else:
#         return (n % 10) + sum(n // 10) 
# num = int(input("Enter a number: "))
# print(f"Sum of digits of {num} is: {sum(num)}")


#reverse of string

# def reverse(s):
#     if len(s) == 0:  
#         return s
#     else:
#         return reverse(s[1:]) + s[0]  
# string = input("Enter a string: ")
# print(f"Reversed string: {reverse(string)}")

