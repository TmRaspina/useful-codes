import random

player_1 = input("Player, make you move : ")
computerMove = random.randint(0, 2)

if computerMove == 0 :
    player_2 = "rock"
elif computerMove == 1 :
    player_2 = "paper"
elif computerMove == 2 :
    player_2 = "scissors"    

print(f"computer move : {player_2}")

if (player_1 == "rock" and player_2 == "paper") or (player_1 == "paper" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "rock") :
    print("computer won!")
elif (player_2 == "rock" and player_1 == "paper") or (player_2 == "paper" and player_1 == "scissors") or (player_2 == "scissors" and player_1 == "rock") :
    print("Player  won!")
elif player_1 == player_2 :
    print("DRAW!!")
else :
    print("An error occurred.....")
