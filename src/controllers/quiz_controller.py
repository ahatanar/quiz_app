# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')

@quiz_bp.route('', methods=['POST'])
def create_quiz():
    # INCOMPLETE: Initialize the QuizService
    # TODO: Initialize an instance of QuizService (Hint: service = QuizService())
    quiz_service = QuizService()
    
    # INCOMPLETE: Retrieve JSON data from the request
    # TODO: Get JSON data from the request using request.json and assign it to `data`
    data = request.json
    
    # INCOMPLETE: Call the create_quiz method in the service
    # TODO: Use the service to create a quiz with the `data` and store the returned quiz ID in `quiz_id`
    quiz_id = quiz_service.create_quiz(data)
    # INCOMPLETE: Return a JSON response with the quiz ID and a 201 status
    # TODO: Use jsonify to create a JSON response containing `message` and `quiz_id`, with status code 201
    return jsonify({"message":"quiz sucessfully created", "id":quiz_id}),201

@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    # INCOMPLETE: Initialize the QuizService
    # TODO: Initialize an instance of QuizService (Hint: service = QuizService())
    quiz_service = QuizService()

    # INCOMPLETE: Use the service to retrieve the quiz by its ID
    # TODO: Call the `get_quiz` method with `quiz_id` and store the result in `quiz`
    quiz = quiz_service.get_quiz(quiz_id)
    # INCOMPLETE: Check if the quiz exists and return a JSON response
    if quiz:
        return jsonify({"message":"quiz found","title":quiz.title}),200
    else:
        return jsonify({"message":"quiz not found"}),404
    # TODO: If `quiz` exists, return it as a JSON response with status 200. Otherwise, return an error message with status 404.
    pass  # REMOVE when implementing

@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    quiz_service = QuizService()
    
    user_answers = request.json.get('answers' )
    print(user_answers)
    score, message = quiz_service.evaluate_quiz(quiz_id, user_answers)
    
    if score is None:
        return jsonify({"error": "Quiz not found"}), 404
    else:
        return jsonify({"score": score, "message": message}), 200