class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        
class Library:
    def __init__(self, ):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        if not self.books:
            print("No book found")
        else:
            for book in self.books:
                if isinstance(book, PrintBook):
                    print(f"PrintBooK: {book.title} {book.author}, Page Count {book.page_count}")
                elif isinstance(book, EBook):
                    print(f"EBooK: {book.title} {book.author}, File Size: {book.file_size}KB")
                else:
                    print(f"BooK: {book.title} {book.author}")
                    