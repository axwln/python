# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()


# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n):
#         print(a ,end=" ")
#         a=a+1
#     print()
        

# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(a ,end=" ")
#         a=a+1
#     print()




# 1. Right Half Pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end=" ")
#     print()


# 2.left half pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

# 3.full pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("* ",end=" ")
#     print()

#4.inverted right half pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("* ",end=" ")
#     print()

#inverted left half pyramid:

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("* ",end=" ")
#     print()



#14. floyd's triangle:

n=4
a=1
for i in range(0,n):
    for j in range(0,i+1):
        print(a ,end=" ")
        a=a+1
    print()