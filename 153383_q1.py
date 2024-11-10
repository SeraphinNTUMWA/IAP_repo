class Book:
    def initialize_book(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Initially, the book is available for borrowing

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Sorry, the book '{self.title}' you wanted is now marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already taken by someone else.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has successfully been returned.")
        else:
            print(f"The book '{self.title}' was never borrowed.")


class Member:
    def initialize_member(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_checked_out = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.books_checked_out.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, the book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_checked_out:
            book.return_book()
            self.books_checked_out.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")

    def display_borrowed_books(self):
        if self.books_checked_out:
            print(f"{self.name} has borrowed the following books:")
            for book in self.books_checked_out:
                print(f"- '{book.title}' by {book.author}")
        else:
            print(f"{self.name} has no borrowed books.")


# Main Interactive Code
def start_library_system():
    # Creating books and initializing them with title and author
    book1 = Book()
    book1.initialize_book("Zamenga", "Author One")

    book2 = Book()
    book2.initialize_book("La Bonne Musique", "Author Two")

    book3 = Book()
    book3.initialize_book("L'Ancien", "Author Three")

    # Get user details and initialize the member
    member_name = input("Please enter your name: ")
    member_id = input("Please enter your member ID: ")
    member = Member()
    member.initialize_member(member_name, member_id)

    while True:
        print("\nLibrary System Menu:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View borrowed books")
        print("4. Exit the system")

        choice = input("Please select an option (1-4): ")

        if choice == '1':
            print("\nAvailable books:")
            print("1. Zamenga by Author One")
            print("2. La Bonne Musique by Author Two")
            print("3. L'Ancien by Author Three")

            book_choice = input("Choose the book number to borrow: ")
            if book_choice == '1':
                member.borrow_book(book1)
            elif book_choice == '2':
                member.borrow_book(book2)
            elif book_choice == '3':
                member.borrow_book(book3)
            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            print("\nList of books you have borrowed:")
            if member.books_checked_out:
                for idx, book in enumerate(member.books_checked_out, 1):
                    print(f"{idx}. {book.title} by {book.author}")

                return_choice = int(input("Enter the number of the book to return: "))
                if 1 <= return_choice <= len(member.books_checked_out):
                    member.return_book(member.books_checked_out[return_choice - 1])
                else:
                    print("Invalid selection. Please try again.")
            else:
                print("You haven't borrowed any books yet.")

        elif choice == '3':
            member.display_borrowed_books()

        elif choice == '4':
            print("Thank you for using the Library System! Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a valid number (1-4).")


# Start the library system
start_library_system()
