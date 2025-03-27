from colorama import Fore, Back, Style

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"Amount deposited: {amount}")
    print(f"Current balance: {balance}")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if balance < amount:
        print("Insufficient balance")
    else:
        amount -= balance
        print(f"Amount withdrawn: {amount}")
        print(f"Current balance: {balance}")

def check_balance():
    global balance
    print(f"Current balance: {balance}")

balance = 0
is_running = True

if __name__ == "__main__":
    while is_running:
        print(Fore.GREEN + "*******************")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("*******************")
        choice = input(Style.RESET_ALL + "Enter your choice: ")
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice") 