import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Stephen Hawking")
author_2 = Author("Stephen King")

author_repository.save(author_1)
author_repository.save(author_2)

authors = author_repository.select_all()

for author in authors:
    print(author.__dict__)

book_1 = Book("A Brief History of Time", author_1, "Science")
book_2 = Book("Carrie", author_2, "Thriller")

book_repository.save(book_1)
book_repository.save(book_2)

books = book_repository.select_all()

for book in books:
    print(book.__dict__)

pdb.set_trace()