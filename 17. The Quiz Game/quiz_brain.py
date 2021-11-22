class Quiz_Brain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question =  self.questions_list[self.question_number]
        user_answer = input(f"{current_question.text} (True / False) :").lower()
        self.check_answer(user_answer)
        self.question_number +=1

    def check_answer(self, user_answer):
        correct_answer = self.questions_list[self.question_number].answer
        if correct_answer.lower() == user_answer:
            print("You got it right !")
            self.score += 1
            
        else:
            print("That's wrong")
        print(f"The answer was {correct_answer}")
        print(f" Current score: {self.score}/{self.question_number + 1}")
        print("\n")