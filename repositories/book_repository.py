from db.run_sql import run_sql

from models.author import Author
from models.books import Book
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def select_all():
    book_list = []
    
    sql = "SELECT * FROM books"
    result = run_sql(sql)

    for row in result:
        book = Book(row["title"], row["author"])
        book_list.append(book)

    return book_list