import random as rd
total_rounds = 10
rounds_played = 0
user_score = 0
computer_score = 0
name = input("Enter your name:\n")
print("welcome to this game", name)
print("Total rounds = 10")
print("s for stone\np for paper\nc for scissor\n")
while rounds_played < total_rounds:
    lst = ["s", "p", "c"]
    computer = rd.choice(lst)
    user = input("Enter your choice: ")
    if user == computer:
        print("Tie")
        print("No one got point")
        print("your score =",user_score, "computer score =",computer_score)
    elif user == "s" and computer == "p":
        computer_score = computer_score + 1
        print("Computer get 1 point")
        print("your score =",user_score, "computer score =",computer_score)
    elif user == "s" and computer == "c":
        user_score = user_score + 1
        print("You get 1 point")
        print("your score =",user_score, "computer score =",computer_score)
    elif user == "p" and computer == "s":
        user_score = user_score + 1
        print("You get 1 point")
        print("your score =",user_score, "computer score =",computer_score)
    elif user == "p" and computer == "c":
        computer_score = computer_score + 1
        print("Computer gets 1 point")
        print("your score =", user_score, "computer score =", computer_score)
    elif user == "c" and computer == "s":
        computer_score = computer_score + 1
        print("Computer gets 1 point")
        print("your score =", user_score, "computer score =", computer_score )
    elif user == "c" and computer == "p":
        user_score = user_score + 1
        print("You get 1 point")
        print("your score =", user_score, "computer score =", computer_score)
    else:
        print("Invalid input !!")
    rounds_played = rounds_played + 1
    print(f"{total_rounds - rounds_played} is left out of {total_rounds}")

print("Game over")
if computer_score > user_score:
    print("Computer wins and you loose")

if computer_score > user_score:
    print("you win and computer loose")

if computer_score == user_score:
    print("No one won, Tie")

print(f"your point is {user_score} and computer point is {computer_score}")
