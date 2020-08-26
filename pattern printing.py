print("pattern printing")
num = int(input("Enter how many rows you want: \n"))
print("Enter 1 or 0")
bool_value = input("1 for true or 0 for false: \n")
if bool_value == "1":
    for i in range(0, num + 1):
        print("*"*i)
if bool_value == "0":
    for i in range(num, 0, -1):
        print("*"*i)
