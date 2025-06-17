i=int(input("Enter your marks: "))
if(i>=90 and i<=100):
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

