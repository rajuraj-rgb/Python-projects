items = [float, list, 5, 3, 4, 234,4435,34, 34, 2,3,32]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)