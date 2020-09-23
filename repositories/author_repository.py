from db.run_sql import run_sql

from models.author import Author
from models.books import Book
import repositories.book_repository as book_repository

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)

def select_all():
    author_list = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row["last_name"])
        author_list.append(author)
    
    return author_list


