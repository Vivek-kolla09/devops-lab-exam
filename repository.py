from model import Book
books = []

# CREATE
def create_books(book:Book):
    books.append(book)
    return books

# READ
def get_books():
    return books

# UPDATE
def update_books(bid:id, book:Book):
    for book in books:
        if book.bid == id:
            book.bookName = Book.bookName
            book.bookCount = Book.bookCount
            return book
    return None

# DELETE
def delete_books(old_name:bookName):
    for book in books:
        if book.old_name == bookName:
            books.remove(book)
            return books
    return None

