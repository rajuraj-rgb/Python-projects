#Faulty calculator
# 45 * 3 =555, 56 + 9 = 77, 56/6 = 4
N1 = int(input("Enter first number: "))
print("What to do? +,-,/,*")
operator = input()
N2 = int(input("Enter second number: "))
if N1==45 and N2==3 and operator=="*":
    print("N1","*", "N2", "=" , 555)
elif N1==56 and N2==9 and operator=="+":
    print("N1", "+", "N2", "=" , 77)
elif N1==56 and N2==6 and operator=="/":
    print("N1", "/" , "N2", "=" , 4)
elif operator == "+":
    Sum = N1 + N2
    print("Sum is", Sum)
elif operator == "*":
    Multiplication = N1 * N2
    print("Multiplication is", Multiplication)
elif operator == "-":
    Sub = N1 - N2
    print("Subtraction is", Sub)
elif operator == "/":
    div = N1/N2
    print("Division is", div)
else:
    print("Error! It is not valid")
