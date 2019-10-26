class Library:
    def __init__(self, collection=None):
        self._book_collection = []

        if collection:
            for book in collection:
                self.add_book(book)

    @property
    def number_of_books(self):
        return len(self._book_collection)

    def add_book(self, book):
        if book not in self._book_collection:
            self._book_collection.append(book)

    def borrow_book(self, book):
        if book in self._book_collection:
            self._book_collection.remove(book)

    def show_book(self):
        print(f"Book Collection: {self._book_collection}")

if __name__ == '__main__':

    collection_1 = Library()
    collection_2 = Library(['Java', 'C#', 'C++'])
    collection_2.show_book()
    collection_2.borrow_book('C#')
    collection_2.add_book('Ruby')
    collection_2.show_book()
    print(f'Liczba książek: {collection_2.number_of_books}')