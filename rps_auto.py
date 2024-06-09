import random

c1_score = 0
c2_score = 0
draw = 0
options = ["rock","paper","scissors"]

print("Welcome to the automatic rock paper scissors game.")
iter = int(input("Enter number of iterations wanted : "))
for i in range(iter):
    rnd_int_1 = random.randint(0,2) #0 = rock , 1 = paper , 2 = scissor
    rnd_int_2 = random.randint(0,2)
    
    ch1 = options[rnd_int_1]
    ch2 = options[rnd_int_2]

    print("Computer 1 picks " + ch1+" while computer 2 picks "+ch2+".")
    if ch1 == "rock" and ch2 == "scissors":
        print("Comp 1 won")
        c1_score+=1
    elif ch1 == "paper" and ch2 == "rock":
        print("Comp 1 won")
        c1_score+=1
    elif ch1 == "scissors" and ch2 == "paper":
        print("Comp 1 won")
        c1_score+=1
    elif ch1 == ch2:
        print("Draw")
        draw+=1
    else:
        print("Comp 2 won")
        c2_score+=1
print()
print("Computer 1 won",c1_score,"times.")
print("Computer 2 won",c2_score,"times.")
print("There was a draw",draw,"times.")
print("Percentage distribution is "+str(c1_score/iter)+"% "+ str(c2_score/iter)+"% "+ str(draw/iter)+"%.")
print("The highest percent was "+str(max(c1_score,c2_score,draw)/iter)+"%")