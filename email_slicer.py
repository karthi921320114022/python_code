email=input("Enter your Email :")

index=email.index("@")
username=email[:index]
domain=email[index+1:]

print(f"username:{username} and domain:{domain}")