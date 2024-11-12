# src/config.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'quiz_app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
