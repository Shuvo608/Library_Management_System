favourite_food = []

while True:

    print("Welcome to Favourite Food Manager")
    print("1. Add Favourite food")
    print("2. View all Favourite Food")
    print("3. Remove Food")
    print("4. Exit")

    choice = input("Enter any option: ")

    if choice == "1":
        food = input(" Enter your favourite food name: ")
        favourite_food.append(food)
        print(f"{food} added Successfully")
    elif choice == "2": 
        if favourite_food:
            print("Your Favourite Foods:")
            for index, food in enumerate(favourite_food, start = 1):
                print(f"{index}.{food}")
        else:
            print("Food Listed empty")

    elif choice == "3":
        food = input("Enter a food name which you want to remove: ")
        favourite_food.remove(food)
        print("Food remove Successfully")
    elif choice == "4":
        print("Thanks for using Favourite Food manager")
        break

    else:
        print("Invalite Choice")