import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()
a="--------------------------------"

random.shuffle(key)

plain_text = input("Enter a message :")
encrypt_text=""

#Encrption

for letter in plain_text:
    index = chars.index(letter)
    encrypt_text+= key[index]

print(a)
print(f"Your message is: {plain_text}")
print(f"Encrypted Message is:{encrypt_text}")
print(a)

#Decryption

plain_text = input("Enter a message :")
decrypt_text=""

for letter in plain_text:
    index = key.index(letter)
    decrypt_text+= chars[index]

print(f"The decrypted message was :{decrypt_text}")
print(a)
