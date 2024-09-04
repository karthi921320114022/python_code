unit= input("Enter unit of temperaturein C or F :")
temp= float(input("Enter the temperature value :"))

if unit == "C" or "c":
    temp= round(((9*temp)/5)+32, 1)
    print(f"Temperature in Fahrenheit is :{temp}°F")
elif unit =="F" or "f":
    temp= round((temp-32)*5/9, 1)
    print(f"Temperature in Celcius is :{temp}°C")
else:
    print(f"{unit} is an invalid unit for input")