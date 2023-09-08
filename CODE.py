class Library:
    def __init__(self):
        self.catalog = {}
        self.users = {}

    def add_book(self, title, author):
        book_id = len(self.catalog) + 1
        self.catalog[book_id] = {'title': title, 'author': author, 'checked_out': False}
        print(f"Book '{title}' by {author} added with ID {book_id}")

    def list_books(self):
        print("Library Catalog:")
        for book_id, book_info in self.catalog.items():
            status = "Available" if not book_info['checked_out'] else "Checked Out"
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Status: {status}")

    def check_out_book(self, user_id, book_id):
        if book_id not in self.catalog:
            print("Invalid book ID.")
            return

        if self.catalog[book_id]['checked_out']:
            print("This book is already checked out.")
            return

        if user_id not in self.users:
            print("Invalid user ID.")
            return

        self.catalog[book_id]['checked_out'] = True
        print(f"Book '{self.catalog[book_id]['title']}' checked out by User ID {user_id}")

    def add_user(self, user_id, name):
        if user_id in self.users:
            print("User ID already exists.")
            return

        self.users[user_id] = {'name': name}
        print(f"User '{name}' added with ID {user_id}")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. List Books")
        print("3. Check Out Book")
        print("4. Add User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            library.check_out_book(user_id, book_id)

        elif choice == '4':
            user_id = int(input("Enter user ID: "))
            name = input("Enter user name: ")
            library.add_user(user_id, name)

        elif choice == '5':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
