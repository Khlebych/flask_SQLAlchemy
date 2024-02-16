from datetime import datetime
from jinja2 import Template


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

from database import db, Book, Genre


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/khleb/PycharmProjects/flask_SQLAlchemy/my_book_data_base.db"

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add(
        Book(
            title="Odin",
            author="Mamin",
            annotation="drama",
            genre_id=1  # drama
        )
    )
    db.session.add(
        Book(
            title="Dva",
            author="Mamin-Papin",
            annotation="opera",
            genre_id=2  # opera
        )
    )

    db.session.add(
        Book(
            title="Tri",
            author="Pushkin",
            annotation="mult",
            genre_id=3  # mult
        )
    )

    db.session.add(
        Book(
            title="Four",
            author="Ильф",
            annotation="comedy",
            genre_id=4  # comedy
        )
    )
    db.session.add(
        Genre(
            id=1,
            genre_name='drama'
        )
    )
    db.session.add(
        Genre(
            id=2,
            genre_name='opera'
        )
    )
    db.session.add(
        Genre(
            id=3,
            genre_name='mult'
        )
    )
    db.session.add(
        Genre(
            id=4,
            genre_name='comedy'
        )
    )

    db.session.commit()


@app.route("/")
def index():
    return "index"


@app.route("/book")
def all_books():
    books = Book.query.all()
    return render_template("all_books.html", books=books)


@app.route("/genre")
def genre():
    return render_template("all_genre.html")


if __name__ == "__main__":
    app.run(debug=True)
