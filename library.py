class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable

class Borrower: #Creating the borrower class with the attributes being the borrower_id and name of the user
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name

class Loan: #Creating the loan class with the attributes being the book being loaned and who is loaning it
    def __init__(self, book, borrower):
        self.book = book
        self.borrower = borrower

class BookManager: #Creating a class that manages the books via multiple methods
    def __init__(self):
        self.books = {} #Books are stored in a dictionary

    def add_book(self, book_id, title, author): #Method to add books into the dictionary
        if book_id in self.books: #If the book ID is already in the dictionary, then you cannot add it again
            raise ValueError("Book ID already exists.")
        self.books[book_id] = Book(book_id, title, author) #The dictionary will contain the book_id, title and author of the book

    def remove_book(self, book_id): #Method the remove books from the dictionary
        if book_id in self.books: #if the book_id is in the dictionary, then it is removed
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.") #If the book_id is not in the dictionary, then an error will be raised

    def search_book(self, book_id): #Method to search books based on the book_id
        return self.books.get(book_id, None) #If the book_id is not in the dictionary, it will return None

class BorrowerManager: #Class to manage the borrowing process through multiple methods
    def __init__(self):
        self.borrowers = {} #The borrowers are stored in a dictionary

    def add_borrower(self, borrower_id, name): #Method to add borrowers into the dictionary
        if borrower_id in self.borrowers: #If the borrower id is already in the dictionary, raise an error
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name) #Dictionary has the borrower_id and name (from borrower class)

    def remove_borrower(self, borrower_id): #method to remove borrowers from the dictionary
        if borrower_id in self.borrowers:
            del self.borrowers[borrower_id] #if its in the dictionary then delete it. otherwise raise error
        else:
            raise ValueError("Borrower ID not found.")

    def search_borrower(self, borrower_id): #method to search for a borrower based on the id. if its not found return none.
        return self.borrowers.get(borrower_id, None)

class LoanManager: #Class to manage loans via  methods
    def __init__(self):
        self.loans = [] #loans are stored in a list

    def create_loan(self, book, borrower): #method to create a loan
        if book.is_loaned:
            raise ValueError("Book is already loaned.")
        loan = Loan(book, borrower) #The loan contains the book and the borrower and is then appended to the list
        self.loans.append(loan)
        book.is_loaned = True #Once is loaned, set to true

    def return_loan(self, book): #method to remove loans 
        for loan in self.loans:  
            if loan.book.book_id == book.book_id: #if its in the loan list it will get removed.
                self.loans.remove(loan)
                book.is_loaned = False
                break
class LibraryFacade:
    def __init__(self):
        self.book_manager = BookManager()
        self.borrower_manager = BorrowerManager()
        self.loan_manager = LoanManager()

    def add_book(self, book_id, title, author):
        self.book_manager.add_book(book_id, title, author)

    def remove_book(self, book_id):
        self.book_manager.remove_book(book_id)

    def search_book(self, book_id):
        return self.book_manager.search_book(book_id)

    def add_borrower(self, borrower_id, name):
        self.borrower_manager.add_borrower(borrower_id, name)

    def remove_borrower(self, borrower_id):
        self.borrower_manager.remove_borrower(borrower_id)

    def search_borrower(self, borrower_id):
        return self.borrower_manager.search_borrower(borrower_id)

    def create_loan(self, book_id, borrower_id):
        book = self.book_manager.search_book(book_id)
        borrower = self.borrower_manager.search_borrower(borrower_id)
        if book and borrower:
            self.loan_manager.create_loan(book, borrower)
        else:
            raise ValueError("Book or Borrower not found.")

    def return_loan(self, book_id):
        book = self.book_manager.search_book(book_id)
        if book:
            self.loan_manager.return_loan(book)
        else:
            raise ValueError("Book not found.")
if __name__ == "__main__":
    library = LibraryFacade()

    # Adding books
    library.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book(2, "1984", "George Orwell")

    # Adding borrowers
    library.add_borrower(1, "Alice")
    library.add_borrower(2, "Bob")

    # Creating a loan
    library.create_loan(1, 1)  # Alice borrows "The Great Gatsby"

    # Searching for a book
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")

    # Returning a loan
    library.return_loan(1)

    # Checking the book status again
    book = library.search_book(1)
    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Is Loaned: {book.is_loaned}")
