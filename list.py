# l=[]
# a=int(input("enter the number "))
# for i in range(0,a):
#     value=input("enter your values")
#     l.append(value)
# print(l)



# a=[]
# n=int(input("enter the number"))
# for i in range(0,n):
#     if i%2==0:
#         a.append(i)
# print(a)


#POP

# prime_numers=[2,3,5,7]
# removed_element=prime_numers.pop()
# print("Removed element:", removed_element)
# print("updated elements",prime_numers)



# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if i<=len(a)-1:
#         if a[i]%2!=0:
#             a.pop(i)
# print("list",a)


# b=[]
# while True:
#     print("1. to add")
#     print("2. to remove")
#     print("3. exit")
#     a=int(input("enter the choice "))
#     if (a==1):
#         x=int(input("enter the number to be added"))
#         b.append(x)
#         print(b)
#     elif(a==2):
#         y=int(input("enter the number to be removed "))
#         removed=b.pop(y)
        
#         print("the numer ",y,"removed",removed)
#     elif(a==3):
#         print("exiting")
#         break
#     else:
#         print("invalid choice, please try again")
#         print("the number ",y,"is not present in the list")
#         continue
    
        

#delete

# languages=["python","swifft","C++","C","java","rust","R"]
# del languages[1]
# print(languages)
# del languages[-1]
# print(languages)
# del languages[0:2]
# print(languages)


#remove
# languages=["python","swifft","C++","C","java","rust","R"]
# languages.remove("python")
# print(languages)

#reversig

# primeno=[2,3,5,7]
# primeno.reverse()
# print("reversed list",primeno)

#repetition

# list1=[12,14,16,18,20]
# l=list1*2
# print(l)

#concatenation
# list1=[12,14,16,18,20]
# list2=[9,10,32,54,86]
# l=list1+list2
# print(l)

#length

# list1=[12,14,16,18,20,23,27,39,40]
# a=len(list1)
# print(a)


#iteration

# list1=[12,14,16,39,40]
# for i in list1:
#     print(i)
    
    
#membership

list1=[100,200,300,400,500]
print(600 in list1)
print(700 in list1)