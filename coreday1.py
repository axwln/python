 #Think of a real-life problem you encounter daily (like remembering grocery items). Write down the steps as if you were programming a solution for it. For example, ‘Create a list of items, check each item in the pantry, remove items you already have,’ and so on. This task will get you into the habit of breaking down problems into steps.
items = ["milk", "eggs", "bread", "butter", "cheese"]
pantry = input("Enter items you already have in the pantry, separated by commas: ").split(",")
tobuy = []
for i in items:
    if i not in pantry:
        tobuy.append(i)
print("Items to buy:", tobuy)
    