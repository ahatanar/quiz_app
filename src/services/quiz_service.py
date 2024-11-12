# src/services/quiz_service.py
from src.models.quiz_model import QuizModel

class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data.get("title")
        questions = quiz_data.get("questions")
        quiz = QuizModel(title, questions)
        quiz.save()
        return quiz.id

    def get_quiz(self, quiz_id):
        return QuizModel.get_quiz(quiz_id)
    
    def evaluate_quiz(self, quiz_id, user_answers):
        quiz = self.get_quiz(quiz_id)
        if quiz is None:
            return None, "Quiz not found"
        correct_answers = quiz.questions
        print(correct_answers)
        score = sum(1 for i, answer in enumerate(user_answers) if i < len(correct_answers) and answer == correct_answers[i]['answer'])
        message = f"You scored {score} out of {len(correct_answers)}"
        return score, message