import random

options = ("rock", "paper", "scissors")
turn =int(input("Enter the number of turns :"))
cycle = 0
c_points=0
p_points=0

while cycle <turn:
    print(f"-------------[ROUND {cycle+1}]-------------")
    player = None
    computer= random.choice(options)

    while player not in options:
        player= input("Enter a choice (rock, paper,scissors): ").lower()

    cycle+=1
    print(f"Player{" ":5} = {player}")
    print(f"computer{" ":4}= {computer}")

    if computer == player:
        print("It's a tie! 🏳")
        cycle-=1
    elif player == "rock" and computer == "scissors":
        print("You got one point ✨")
        p_points+=1
    elif player == "paper" and computer == "rock":
        print("You got one point 🔥")
        p_points+=1
    elif player == "scissors" and computer == "paper":
        print("You got one point 🌟")
        p_points+=1
    else :
        print("You lose 👻")
        c_points+=1
print()
print("|--------------------------------|")
if p_points < c_points:
    print(f"{" ":10}You lost 🥺")
else:
    print(f"{" ":10}You win 🏆")
print("|--------------------------------|")