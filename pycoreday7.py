#score

i=int(input("Enter your score: "))
if(i>=95 and i<=100):
    print("congratulations you are graduated with  High Distinction")
elif(i>=90 and i<=94):
    print("grade A")
elif(i>=80 and i<90):
    print("grade B")
elif(i>=70 and i<80):
    print("grade C")
elif(i>=60 and i<70):
    print("grade D")
elif(i<0 or i>100):
    print("invalid marks")
else:
    print("failed")

#check number
a=int(input("enter a number"))
if(a>0):
    print("the number is positive")
elif(a<0):
    print("the number is negative")
else:
    print("the numer is zero")