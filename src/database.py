# src/database.py
from flask_sqlalchemy import SQLAlchemy
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Initialize the SQLAlchemy instance
db = SQLAlchemy()
