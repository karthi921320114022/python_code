def show_balance(balance):
    print("********************************")
    print(f"Your balance amount is ₹{balance:.2f}")
    print("********************************")

def deposit():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    amount = float(input("Enter deposit amount :"))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    if amount <= 0:
        print("********************************")
        print("Please enter a valid amount")
        print("********************************")
        return 0
    else:
        return amount
def withdraw(balance):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    amount = float(input("Enter withdraw amount :"))
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    if amount > balance:
        print("********************************")
        print("Insufficient balance!")
        print("********************************")
        return 0
    elif amount <= 0:
        print("********************************")
        print("Please enter a valid amount")
        print("********************************")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True
    while is_running :
        print("--------------------------------")
        print("Welcome to Banking programming")
        print(" 1-Show balance amount \n 2-Deposit amount\n 3-Withdraw amount\n 4-Exit")
        print("--------------------------------")

        choice=int(input("Enter your choice (1-4):"))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -=withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("--------------------------------")
            print("Your choice is invalid!")
            print("--------------------------------")
    print("________________________________")
    print("Thank you! have a nice day!")
    print("--------------------------------")

if __name__ == "__main__":
    main()