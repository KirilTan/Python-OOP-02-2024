class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f'{self.title} by {self.author}. Currently at page {self.page}'


class Library:
    def __init__(self, name: str, books: list[Book] = []):
        self.name = name
        self.books = books

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f'Book {book.title} from {book.author} added to {self.name} library')

    def remove_book(self, book: Book) -> None:
        try:
            self.books.remove(book)
            print(f'Book {book.title} from {book.author} removed from {self.name}')
        except ValueError:
            print('Book not found')

    def find_book(self, title: str) -> Book or str:
        try:
            book_object = next(filter(lambda x: x.title == title, self.books))
            return book_object
        except StopIteration:
            return f'Book {title} not found in {self.name} library'


# Test Code
if __name__ == '__main__':
    library = Library('Test Library')
    book = Book('Test Book', 'Author')
    library.add_book(book)
    print(library.find_book('Test Book'))
    library.remove_book(book)
    library.remove_book(book)
    print(library.find_book('Test Book'))
