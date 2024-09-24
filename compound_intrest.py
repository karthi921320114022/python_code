principle=0
rate=0
time=0

while principle <=0:
    principle= float(input("Enter pinciple amount (Rs):"))
    if principle<=0:
        print("principle amount can't be less than or equal to zero")

while rate <=0:
    rate= float(input("Enter intrest rate (%):"))
    if principle<=0:
        print("Rate  can't be less than or equal to zero")

while time <=0:
    time= int(input("Enter time (Y):"))
    if principle<=0:
        print("Time can't be less than or equal to zero")

total=principle*pow((1+rate/100), time)
print(f"Balance after {time} year/s :{total:.2f}.RS")