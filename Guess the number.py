n = 18
number_of_guesses=1
print("print number of guesses is limited to 9 times: ")
while (number_of_guesses<=9):
    Guess_number = int(input("Guess the number"))
    if Guess_number>18 :
        print("You entered a greater number, please enter a smaller number")
    elif Guess_number<18:
        print("You entered a smaller number, please enter a greater number")
    else:
        print("Congratulations! You guessed the correct number")
        print(number_of_guesses, "no. of guesses you took to finish")
        break
    print(9-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1