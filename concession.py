menu={"pizza":150.00,
      "burger":100.00,
      "popcorn":160.00,
      "chips":80.00,
      "coke":60.00,
      "water":30.00,
      "soda":40.00
}

cart=[]
total=0

print("|-------------MENU-------------------|")
for key, value in menu.items():
    print(f"{key:10}: ₹{value: .2f}")
print("------------------------------------")

while True:
    food=input("Select an item (q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total+=menu.get(food)
    print(food, end=", ")
print()

print("----------------- ---------------------")
print(f"Your total ₹{total: .2f}")
print("|---------------------------------------|")