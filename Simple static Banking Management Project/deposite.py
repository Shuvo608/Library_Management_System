def deposite_page(user):
    print("\n--- Deposite Page ---")
    try:
        amount = float(input("Enter the deposit amount: "))
        if amount > 0:
            user.balance += amount
            print(f"Deposite successful! New balance is: {user.balance}")
        else:
            print("Deposite amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")