# f=open('trial.py','x')
# f=open('trial.py','w')
# f.write("this is the write command")
# f.write("\n it allow us to write in a particular file")
# f.close()

# f=open('trial.py','a')
# f.write("this is the write command")
# f.write("\n it allow us to write in a particular file")
# f.close()

# f=open('trial.py','r')
# for i in f:
#     print(i)

# f=open('trial.py','r')
# # print(f.readline())
# # print(f.readline())
# # f.close()
# print(f.read())


# with open("trial.py") as file:
#     data=file.read()
# print(data)


# file=open("trial.py","r")
# print(file.read(5))


with open("trial.py","r")as file:
    data=file.readlines()
for line in data:
    word=line.split()
    print(word)
    
