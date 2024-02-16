from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()


class Book(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    publication_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    title = db.Column(db.String, primary_key=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    annotation = db.Column(db.String(100), nullable=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.genre_name"))
    # genre = relationship("Genre")

    def __repr__(self):
        return f"Book {self.title!r}"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    # book_name = relationship("Book")

    # def __repr__(self):
    #     return f"Genre {self.genre_name!r}"