import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask
from src.config import Config
from src.database import db

from src.controllers.quiz_controller import quiz_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully.")
        except Exception as e:
            print("Error initializing the database:", e)

    app.register_blueprint(quiz_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
