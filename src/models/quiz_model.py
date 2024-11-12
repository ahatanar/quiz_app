# src/models/quiz_model.py
from src.database import db
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import PickleType


class QuizModel(db.Model):
    # Set up the table name
    __tablename__ = "quizzes"

    # Define table columns
    id = db.Column(
        db.Integer, primary_key=True
    )  # Primary key column named `id`
    title = db.Column(
        db.String, nullable=False
    )  # String column `title` that cannot be null
    questions = db.Column(
        PickleType, nullable=False
    )  # Column `questions` to store a list using PickleType

    def __init__(self, title, questions):
        # Initialize the model with title and questions
        self.title = title
        self.questions = questions

    def save(self):
        # Save the quiz to the database
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        # Retrieve a quiz by its ID
        return cls.query.get(quiz_id)
