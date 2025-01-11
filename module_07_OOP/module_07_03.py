class Student:

    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = {}

    def get_grade(self, grade, discipline):
        self.grades[discipline] = grade
        return f'{self.name} {self.surname} получил оценку {grade} по курсу {self.course}, дисциплина {discipline}.'

    def display_all_grades(self):
        for discipline, grade in self.grades.items():
            print(f"Студент {self.name}, {self.surname}. Дисциплина {discipline}. Оценка {grade}")


user_name = 'Иван'
user_surname = 'Иванов'
user_course = 'Python'


student_1 = Student(user_name, user_surname, user_course)
print(student_1.get_grade(8, 'Строки'))
print(student_1.get_grade(9, 'Списки'))
print(student_1.get_grade(7, 'Словари'))
student_1.display_all_grades()
print(student_1.grades)
print()
student_1.name = 'Петр'
student_1.display_all_grades()

# student_2 = Student('Петр', 'Петров', 'Java')
# print(student_2.get_grade(9))
