#Rock-Paper-scissors game

import random

options = ["rock", "paper", "scissors"]

lose = [ "Computer won... as expected" ,
        "Huh such a loser" ,
        "You lose ! I think it was your first time" ,
        "A human can't win against Computer"
    ]
win = ["You won... huh by luck" ,
       "You only won because you cheated" ,
       "Your win is as legitimate as a three-dollar bill",       
       "You won... somehow"]
while True:
    player = input("Choose rock, paper, or scissors: ").lower()
    if player not in options:
        print(" You stupid it's not in option Try again.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if player == computer:
        print("ohhh it's tie! Nevermind try again")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print(random.choice(win))
    else:
        print(random.choice(lose))

    play_again = input(" You brat wanna Play again? (yeah/nahh): ").lower()
    if play_again != "yeah":
        break
