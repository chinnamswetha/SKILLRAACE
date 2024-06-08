class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def author_royalty(self):
        return self._author_royalty

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._author_royalty = 0.1 * self._price * copies_sold
        elif 500 < copies_sold <= 1500:
            self._author_royalty = (0.1 * 500 * self._price) + (0.125 * self._price * (copies_sold - 500))
        else:
            self._author_royalty = (0.1 * 500 * self._price) + (0.125 * 1000 * self._price) + (0.15 * self._price * (copies_sold - 1500))


class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, ebook_format):
        self._ebook_format = ebook_format

    def royalty(self, copies_sold):
        gst = 0.12  # GST rate for ebooks
        super().royalty(copies_sold)
        self._author_royalty -= gst * self._author_royalty


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 25)
book1.royalty(1000)
print(f"Author's royalty for book: ${book1.author_royalty:.2f}")

ebook1 = Ebook("Python for Beginners", "John Doe", "Tech Publications", 15, "EPUB")
ebook1.royalty(500)
print(f"Author's royalty for ebook: ${ebook1.author_royalty:.2f}")