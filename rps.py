import random

u_score = 0
comp_score = 0
draw = 0
options = ["rock","paper","scissors"]

print("Welcome to the rock paper scissors game : ")
while True:
    opt = input("Enter choice or Q to quit : ").lower()
    if opt == 'q':
        break
    if opt not in options:
        print("Please enter a valid option !")
        continue
    rnd_int = random.randint(0,2) #0 = rock , 1 = paper , 2 = scissor
    print("Computer picks "+options[rnd_int]+".")

    if opt == "rock" and options[rnd_int] == "scissors":
        print("You won !")
        u_score+=1
    elif opt == "paper" and options[rnd_int] == "rock":
        print("You won !")
        u_score+=1
    elif opt == "scissors" and options[rnd_int] == "paper":
        print("You won !")
        u_score+=1
    elif options[rnd_int] == opt:
        print("Draw")
        draw+=1
    else:
        print("You lost :(")
        comp_score+=1
print("You won",u_score,"times.")
print("The computer won",comp_score,"times.")
print("There was a draw",draw,"times.")
print("Adios")