age = int(input("Enter your age: "))
if age<18:
    print("You cannot drive")
elif age==18:
    print("We will think about you")
elif age>18:
    print("You can drive")
else:
    print("Not found")