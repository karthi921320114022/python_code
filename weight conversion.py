weight=float(input("Enter your weight:"))
unit=input("Enter the unit(K OR L)")

if unit == "K":
    weight*=2.205
    print(f"Your weight is {round(weight, 1)}Lbs")
elif unit =="L":
    weight/=2.205
    print(f"Your weight is {round(weight, 1)}Kgs")
else:
    print(f"{unit} is invalid input!")