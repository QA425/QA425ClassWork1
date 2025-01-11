from ClassQuestion.ClassQuestion import Question

question_1 = Question('My name __ Vova', 'is')
question_2 = Question('I live __ Moscow', 'in')

question_list = [question_1, question_2]

for question in question_list:
    print(question.question)
    answer = input('Введите ваш ответ: ').strip().lower()
    if question.is_correct(answer):
        print('Ответ верный!')
    else:
        print(f"Ответ неверный, верный ответ {question.answer}")
