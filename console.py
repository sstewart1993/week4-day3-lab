import pdb
from models.author import Author
from models.books import Book


import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()


author1 = Author("George", "Martin")
author_repository.save(author1)
author2 = Author("Ken", "Davis")
author_repository.save(author2)

book1 = Book("Game of Thrones", author1)
book_repository.save(book1)
book2 = Book("One Flew Over the Cuckoo's Nest", author2)
book_repository.save(book2)
book3 = Book("Storm of Swords", author1)
book_repository.save(book3)

author_repository.select_all()