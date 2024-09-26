import random

#● ┌ ─ ┐ │ └ ┘ 

dice_art={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘")
}

dice=[]
total=0

num_of_dice=int(input("Enter the number of dice to roll: "))
for die in range (num_of_dice):
    dice.append(random.randint(1, 6))


for die in dice:
   total+=die
   print(" ", end="")
   print(die,end="          ")
print()

for line in range (5):
   for die in dice:
      print(dice_art[die][line],end=" ")
   print()
for _ in range (num_of_dice):
   print("   ", end="")
print(f"The total value is :{total}")