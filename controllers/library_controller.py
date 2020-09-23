from flask import Flask, render_template, request, redirect
from models.author import Author

from flask import Blueprint
from repositories import author_repository, book_repository

library_blueprint = Blueprint("author", __name__)

@library_blueprint.route("/library")
def library():
    authors = author_repository.select_all()
    books = book_repository.select_all()
    return render_template("index.html", authors=authors, books=books)

