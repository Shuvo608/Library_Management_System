from deposite import deposite_page
from withdraw import withdraw_page
from check_balance import check_balance_page


class BankingManagement:
    def __init__(self, holder_name="Default User", initial_balance=0):
        self.holder_name = holder_name
        self.balance = initial_balance


def main_menu(user):
    while True:
        print("\n--- Main Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            deposite_page(user)
        elif choice == "2":
            withdraw_page(user)
        elif choice == "3":
            check_balance_page(user)
        elif choice == "4":
            print("Thank you for using the Ostad Banking Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    print("Welcome to the Ostad Banking Management System!")
    holder_name = input("Enter the account holder's name: ")
    try:
        initial_balance = float(input("Enter the initial balance: "))
    except ValueError:
        initial_balance = 0
        print("Invalid input. Setting initial balance to 0.")

    user = BankingManagement(holder_name=holder_name, initial_balance=initial_balance)
    print(f"\nAccount created Successfully for {user.holder_name} with a balance of {user.balance}")

    main_menu(user)