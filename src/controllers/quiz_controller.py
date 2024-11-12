# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint("quiz", __name__, url_prefix="/api/quizzes")


@quiz_bp.route("", methods=["POST"])
def create_quiz():
    quiz_service = QuizService()

    data = request.json

    # INCOMPLETE: Call the create_quiz method in the service
    quiz_id = quiz_service.create_quiz(data)
    # INCOMPLETE: Return a JSON response with the quiz ID and a 201 status
    return jsonify({"message": "quiz sucessfully created", "id": quiz_id}), 201


@quiz_bp.route("/<int:quiz_id>", methods=["GET"])
def get_quiz(quiz_id):
    # INCOMPLETE: Initialize the QuizService
    quiz_service = QuizService()

    # INCOMPLETE: Use the service to retrieve the quiz by its ID
    quiz = quiz_service.get_quiz(quiz_id)
    if quiz:
        return jsonify({"message": "quiz found", "title": quiz.title}), 200
    else:
        return jsonify({"message": "quiz not found"}), 404
    pass  # REMOVE when implementing


@quiz_bp.route("/<int:quiz_id>/submit", methods=["POST"])
def submit_quiz(quiz_id):
    quiz_service = QuizService()

    user_answers = request.json.get("answers")
    print(user_answers)
    score, message = quiz_service.evaluate_quiz(quiz_id, user_answers)

    if score is None:
        return jsonify({"error": "Quiz not found"}), 404
    else:
        return jsonify({"score": score, "message": message}), 200
