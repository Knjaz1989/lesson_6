class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        else:
            lst = []
            for i in self.grades:
                lst.append(sum(self.grades[i]) / len(self.grades[i]))
            return sum(lst) / len(lst)

    def give_rate(self, course, mentor, grade):
        if isinstance(self, Student) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):  # Определяет поведение оператора равенства, ==
        if not isinstance(other, Student):
            return "Second person not in Student"
        return self.get_average() == other.get_average()

    def __ne__(self, other):  # Определяет поведение оператора неравенства, !=
        if not isinstance(other, Student):
            return "Second person not in Student"
        return self.get_average() != other.get_average()

    def __lt__(self, other):  # Определяет поведение оператора меньше, <
        if not isinstance(other, Student):
            return "Second person not in Student"
        return self.get_average() < other.get_average()

    def __gt__(self, other):  # Определяет поведение оператора больше, >
        if not isinstance(other, Student):
            return "Second person not in Student"
        return self.get_average() > other.get_average()

    def __le__(self, other):  # Определяет поведение оператора меньше или равно, <=
        if not isinstance(other, Student):
            return "Second person not in Student"
        return self.get_average() <= other.get_average()

    def __ge__(self, other):  # Определяет поведение оператора больше или равно, >=
        if not isinstance(other, Student):
            return "Second person not in Student"
        return self.get_average() >= other.get_average()

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.get_average()}
Курсы в процессе обучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}"""


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rate = []
        self.grades = {}

class Lecturer(Mentor):

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average()}"

    def get_average(self):
        return Student.get_average(self)

    def __eq__(self, other):  # Определяет поведение оператора равенства, ==
        if not isinstance(other, Lecturer):
            return "Second person not in Lecturer"
        return self.get_average() == other.get_average()

    def __ne__(self, other):  # Определяет поведение оператора неравенства, !=
        if not isinstance(other, Lecturer):
            return "Second person not in Lecturer"
        return self.get_average() != other.get_average()

    def __lt__(self, other):  # Определяет поведение оператора меньше, <
        if not isinstance(other, Lecturer):
            return "Second person not in Lecturer"
        return self.get_average() < other.get_average()

    def __gt__(self, other):  # Определяет поведение оператора больше, >
        if not isinstance(other, Lecturer):
            return "Second person not in Lecturer"
        return self.get_average() > other.get_average()

    def __le__(self, other):  # Определяет поведение оператора меньше или равно, <=
        if not isinstance(other, Lecturer):
            return "Second person not in Lecturer"
        return self.get_average() <= other.get_average()

    def __ge__(self, other):  # Определяет поведение оператора больше или равно, >=
        if not isinstance(other, Lecturer):
            return "Second person not in Lecturer"
        return self.get_average() >= other.get_average()

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'