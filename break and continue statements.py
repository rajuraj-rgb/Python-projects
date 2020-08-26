while(True):
    inp = int(input("Enter a number"))
    if inp>100:
        print("Congrats! You have entered a number greater than 100")
        break
    else:
        print("Try again")
        continue
