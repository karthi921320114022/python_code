import random

lowest_num=1
highest_num=100
answer= random.randint(lowest_num, highest_num)
guesses=0
status=True

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Select a number betweeen {lowest_num} and {highest_num}")

while status:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    guess=input("Enter your guess: ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        print("-------------------------------------")
        if guess<lowest_num or guess>highest_num:
            print("Your guess is out of range")
            print(f"Please select a number betweeen {lowest_num} and {highest_num}")
            

        elif (abs(guess-answer)) <15 and guess<answer:
            print("your guess is low!")
        elif (abs(guess-answer)) <15 and guess>answer:
            print("your guess is high!")
        elif guess>answer:
            print("Your guess is too high!!")
        elif guess<answer:
            print("Your guess is too low!!")
        else :
            print(f"Your guess[{answer}] is CORRECT")
            print(f"NUmber of guesse you made: {guesses}")
            print("|------------------------------------------|")
            status=False
        
    else:
        print("INVALID!")
        print(f"Please select a number betweeen {lowest_num} and {highest_num}")
                