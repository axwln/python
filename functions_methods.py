#String functions and methods
#LOWER___________
# message="PYTHON IS FUN"
# print(message.lower())


#UPPER______________

# message="python is fun"
# print(message.upper())

#COUNT__________
# a="i love appls, apples are my favorite fruit"
# b=a.count("p")
# print(b)

#FIND_______________
# message="python is a fun programming language"
# print(message.find('fun'))


#REPLACE____________

# text="bat ball"
# replaced_text=text.replace('ba','ro')
# print(replaced_text)






#BOOLEAN DATA TYPES

#APPEND_____________
n=[21,34,54,12]
print("before append: ", n)
n.append(32)
print("after append: ",n)


#INSERT()______________

vowel=['a','e','i','u']
vowel.insert(3,'o')
print('List:', vowel)


#EXTEND()_______________
prime_numbers=[2,3,5]
print("list 1:",prime_numbers)
even_numbers=[4,6,8]
print("list 2:",even_numbers)
prime_numbers.extend(even_numbers)
print("list affter append:",prime_numbers)