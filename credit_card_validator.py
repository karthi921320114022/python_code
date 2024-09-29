sum_even_digits = 0
sum_odd_digits = 0
total = 0

print("sample:378282246310005, 5610591081018250, 6011000990139424")

card_number = input("Enter your card number :")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]


for odd in card_number [::2]:
    sum_odd_digits += int(odd)

for even in card_number[1::2]:
    even=int(even)*2

    if even >= 10:
        sum_even_digits += ((even % 10) + 1)
    else:
        sum_even_digits +=  even

total=sum_even_digits + sum_odd_digits

if (total % 10) == 0:
    print(" Your card is valid ✅")
else:
    print(" Your card is invalid! ❌")