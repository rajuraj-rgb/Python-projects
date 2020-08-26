#Faulty calculator
# 45 * 3 =555, 56 + 9 = 77, 56/6 = 4
while(True):
    N1 = int(input("Enter first number:\n"))
    operator = input("What to do? +, -, *, / :\n")
    N2 = int(input("Enter second number:\n"))
    if N1 == 45 and operator == "*" and N2 == 3 :
        print("N1", "*", "N2", "=", 555)
    elif N1 == 56 and operator == "=" and N2 == 9 :
        print("N1", "+", "N2", "=", 77)
    elif N1 == 56 and operator == "/" and N2 == 6 :
        print("N1", "/", "N2", "=", 4)
    elif operator == "+":
        sum = N1 + N2
        print("Sum is", sum)
    elif operator == "-":
        sub = N1 - N2
        print("Subtraction is", sub)
    elif operator == "*":
        mul = N1 * N2
        print("Multiplication is", mul)
    elif operator == "/":
        div = N1/N2
        print("Division is", div)
    else:
        print("Invalid input!")