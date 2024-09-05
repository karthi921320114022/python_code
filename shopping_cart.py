foods=[]
prices=[]
total=float()

while True:
    food=input("Enter the food to buy (press q to quit) :")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price=float(input(f"Enter the price of {food} :"))
        prices.append(price)
        total+=price

print("------------YOUR CART-----------")
for x in foods:
    print(x, end=" ")

print("\n")
print(f"Your total amount is {total}Rs")
print("------------THANK YOU-----------")