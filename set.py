# a=set() #empty set
# print(type(a))
# set1={1,6,4,'abc'}
# print(type(set1))


# days=set(["Monday","Tuesday","Wednesday","Thursday"])
# print(days)
# print(type(days))
# for i in days:
#     print(i)
    

#add() mrthod

# months=set(["January","February","March","April","May","June"])
# print(months)
# months.add("July")
# print(months)

#update() method

# months=set(["January","February","March","April","May","June"])
# print(months)
# months.update(["July","August"])
# print(months)


#discard method

# months=set(["January","February","March"])
# print(months)
# months.discard("January") #remove the value without error even if the value is not in the set
# print(months)


#remove method


# months=set(["January","February","March"])
# print(months)
# months.remove("January") #creates an error when the value is not in the set
# print(months)


#Union

# days1=set(["Monday","Tuesday","Wednesday","Thursday"])
# days2=set(["Friday","Saturday","Sunday"])
# print(days1|days2)

#intersection

# days1=set(["Monday","Tuesday","Wednesday","Thursday"])
# days2=set(["Monday","Tuesday","Sunday","Friday"])
# print(days1&days2)


#program1

# l=[1,2,4,2,6]
# print(l)
# s=list(set(l))
# print(s)

#program 2

# s=set()
# for i in range(0,5):
#     i=(input(f"enter {i+1} numbers"))
#     s.add(i)
# print(s)

#progrsm3

a=input("enter the sentence")
s=set()
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


