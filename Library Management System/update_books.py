from view_all_books import view_all_books
from save_all_books import save_all_books

def update_books(all_books):
    view_all_books(all_books)

    book_index = int(input("Enter the number of the book to update: ")) - 1

    if 0 <= book_index < len(all_books):
        book = all_books[book_index]

        print(f"Updating {book['title']} by {book['author']}")

        book['title'] = input(f"Enter new title (current: {book['title']}): ")
        book['author'] = input(f"Enter new author (current: {book['author']}): ")
        book['isbn'] = input(f"Enter new ISBN (current: {book['isbn']}): ")
        book['year'] = input(f"Enter new year (current: {book['year']}): ")
        book['price'] = input(f"Enter new price (current: {book['price']}): ")
        book['quantity'] = input(f"Enter new quantity (current: {book['quantity']}): ")



        save_all_books(all_books)
        print("Book updated successfully!") 

    else:
        print("Invalid.")
    return all_books