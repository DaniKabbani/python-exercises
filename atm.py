def read_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a number.")
        return None


def atm_simulation():
    balance = None
    while balance is None or balance < 0:
        balance = read_amount("Enter your starting balance: $")

    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            print(f"Your balance is: ${balance:.2f}")

        elif choice == "2":
            amount = read_amount("Enter the amount to deposit: $")
            if amount is None:
                continue
            if amount > 0:
                balance += amount
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Deposit amount must be greater than zero.")

        elif choice == "3":
            amount = read_amount("Enter the amount to withdraw: $")
            if amount is None:
                continue
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrew: ${amount:.2f}")

        elif choice == "4":
            print("Exiting the ATM. Thank you!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")


if __name__ == "__main__":
    atm_simulation()
