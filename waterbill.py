units = int(input("Enter the number of water units consumed: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 8)
else:
    bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)
print(f"Total water bill: ₹{bill}")