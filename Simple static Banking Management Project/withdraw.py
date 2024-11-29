def withdraw_page(user):
    print("\n--- Withdraw Page ---")
    try:
        amount = float(input("Enter the withdrawal amount: "))
        if amount > user.balance:
            print(f"Insufficient funds! Your balance is {user.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            user.balance -= amount
            print(f"Withdrawal successful! New balance is: {user.balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
