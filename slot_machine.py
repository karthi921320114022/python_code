import random
import time

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [ random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("****************")
    print("  |  ".join(row))
    print("****************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*4
        elif row[0] == "🍋":
            return bet*5
        elif row[0] == "🔔":
            return bet*10
        elif row[0] == "⭐":
            return bet*20
    return 0
def main():
    balance = 100

    print("*****Welcome to Slots*****")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***************************")

    while balance > 0:
        print(f"Current balance ₹{balance}")
        bet=input("Place your bet amount :₹")

        if not bet.isdigit():
            print("please enter a valid input")
            continue
        bet=int(bet)

        if bet <= balance and bet >0:
            balance -= bet
        else:
            print("Insufficient funds") 

        row =spin_row()
        print("Spinning...\n")
        time.sleep(3)

        print_row(row)

        payout=get_payout(row,bet)
        
        if payout > 0:
            print("🌟🌟🌟🌟🌟🌟🌟🌟")
            print(f"🌟 You won ₹{payout} 🌟")
            print("🌟🌟🌟🌟🌟🌟🌟🌟")

        else:
            print("Better luck next time!")

        balance +=payout

        play_again =input("Do you want to play again? (y/n): ").upper()
        if play_again != "Y":
            break
    print("-------------------------------------------")
    print(f"Game over! Your current balance ₹{balance}")
    print("-------------------------------------------")

if __name__ == '__main__':
    main()