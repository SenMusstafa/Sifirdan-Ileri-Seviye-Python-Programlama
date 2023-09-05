class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]

    def display_question(self):
        question = self.get_question()
        print(f'Soru {self.question_index + 1}: {question.text}')
        
        for q in question.choices:
            print('-' + q)

        answer = input('cevap: ')
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        self.question_index += 1

    def load_question(self):
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()

    def show_score(self):
        print('Score:', self.score)

    def display_progress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_question:
            print('Quiz bitti')
        else:
            print(f'Question {question_number} of {total_question}'.center(100, '*'))

# Demonstration
def quiz_example():
    q1 = Question('en iyi programlama dili hangisidir?', ['c#', 'python', 'javascript', 'java'], 'python')
    q2 = Question('en popüler programlama dili hangisidir?', ['c#', 'javascript', 'java', 'python'], 'python')
    q3 = Question('en çok kazzandıran programlama dili hangisidir?', ['c#', 'java', 'python', 'javascript'], 'python')
    questions = [q1, q2, q3]

    quiz = Quiz(questions)
    quiz.load_question()

if __name__ == "__main__":
    quiz_example()
