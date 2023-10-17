class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            print(f"You've finished reading!")
        else:
            print(f"You're now on page")

    def bookmark(self, page_number):
        self.current_page = page_number

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book.title)  # Intentional bug: should append the book object, not just the title

    def find_book(self, title):
        for book in self.books:
            if book.title == title:  # Intentional bug: since we only stored titles, this will fail
                return book
        return None

if __name__ == "__main__":
    harry_potter = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320)
    harry_potter.read(50)
    harry_potter.read(100)

    my_library = Library()
    my_library.add_book(harry_potter)
    book_found = my_library.find_book("Harry Potter and the Sorcerer's Stone")
    if book_found:
        print(f"Found in the library!")
    else:
        print("Book not found in the library.")  # This will be printed due to the bug
