from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = [Question(question["text"], question["answer"]) for question in question_data]

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    question = quiz.next_question()


print("The quiz is compeleted")
print(f"Tour final score was: {quiz.score}/{quiz.question_number}")