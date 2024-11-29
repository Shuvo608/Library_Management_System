import add_books
import view_all_books
import update_books
import remove_books

all_books=[]

while True:
    print("Welcome to Library Management System")
    print("1. Add Book")
    print("2. View all book")
    print("3. Update")
    print("4. Remove")
    print("5. Exit")

    menu = input ("Please Select any Number: ")

    if menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_books.update_books(all_books)
    elif menu == "4":
        remove_books.remove_books(all_books)
    elif menu == "5":
        print("Thanks for Library Management System")
        break
    
    else:
        print("You Do not Select any Option! Please Select any Option")
