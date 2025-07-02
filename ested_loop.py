# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()

#

# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n):
#         print(a ,end=" ")
#         a=a+1
#     print()
        
#floyd's triangle:
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



#floyd's triangle:

# n=4
# a=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(a ,end=" ")
#         a=a+1
#     print()


# 5. Inverted Full Pyramid:
# n = 5
# for i in range(0, n):
#     for j in range(0, i):
#         print(" ", end="")
#     for k in range(0, n - i):
#         print("* ", end="")
#     print()
    
#rhombus pattern
# n=5
# for i in range(0, n):
#     for j in range(0,n + i + 1):
#         print(" ", end="")
#     for k in range(0, n):
#         print("* ", end="")
#     print()
        


#diamond pattern
# n=5
# for i in range(0, n-1):
#     for j in range(0,n-i):
#         print(" ", end="")
#     for k in range(0, i+1):
#         print(" *", end="")
#     print()
# a=5
# for i in range(0, a):
#     for j in range(0, i+2):
#         print(" ", end="")
#     for k in range(0,n-i):
#         print("* ", end="")
#     print()
    
#hourglass pattern
# a=5
# for i in range(0, a):
#     for j in range(0, i+1):
#         print(" ", end="")
#     for k in range(0,n-i):
#         print(" *", end="")
#     print()
# n=5
# for i in range(0, n-1):
#     for j in range(0,n-i):
#         print(" ", end="")
#     for k in range(0, i+2):
#         print("* ", end="")
#     print()


#hollow square pattern
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
    
    
#hollow full pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,2*i+1):
#         if k==0 or k==2*i or i==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
    
#hollow inverted full pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(0,2*(n-i)-1):
#         if k==0 or k==2*(n-i)-2 or i==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
    
#hollow diamond pattern
# n=5
# for i in range(0, n-1):
#     for j in range(0,n-i):
#         print(" ", end="")
#     for k in range(0, 2*i+1):
#         if k==0 or k==2*i or i==n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(0, n-1):
#     for j in range(0, i+2):
#         print(" ", end="")
#     for k in range(0, 2*(n-i)-1):
#         if k==0 or k==2*(n-i)-2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


#letter a 
n = 5
for i in range(0, n):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range(0, i + 1):
        if i == n // 2 or k == 0 or k == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

