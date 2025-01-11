class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def is_correct(self, user_answer):
        return user_answer == self.answer




