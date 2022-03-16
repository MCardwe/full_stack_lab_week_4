import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()

author_1 = Author("Stephen Hawking")
author_2 = Author("Stephen King")

author_repository.save(author_1)
author_repository.save(author_2)

authors = author_repository.select_all()

for author in authors:
    print(author.__dict__)

pdb.set_trace()