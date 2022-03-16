from flask import Blueprint, Flask, render_template, redirect, request
from flask import Blueprint

from repositories import author_repository
from repositories import book_repository
from models.book import Book 

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books", methods=["GET"])
def show_books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
