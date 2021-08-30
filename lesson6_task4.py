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


def average_of_students(students, course):
    if not isinstance(students, list):
        print("Not list")
    else:
        nlist = []
        for i in students:
            nlist.append(sum(i.grades[course]) / len(i.grades[course]))
        print(sum(nlist) / len(nlist))

def average_of_lecturers(lecturers, course):
    average_of_students(lecturers, course)

s1 = Student("Игорь", "Сверчков")
s2 = Student("Сергей", "Манаев")
l1 = Lecturer("Олег", "Булыгин")
l2 = Lecturer("Александр", "Бардин")
r1 = Reviewer("Анна", "Патракова")
r2 = Reviewer("Михаил", "Окатьев")

s1.courses_in_progress.append("OOP")
s2.courses_in_progress.append("OOP")
l1.courses_attached.append("OOP")
l2.courses_attached.append("OOP")

s1.give_rate("OOP", l1, 8)
s2.give_rate("OOP", l1, 6)
s1.give_rate("OOP", l2, 4)
s2.give_rate("OOP", l2, 8)

r1.rate_hw(s1, "OOP", 9)
r2.rate_hw(s1, "OOP", 7)
r1.rate_hw(s2, "OOP", 5)
r1.rate_hw(s2, "OOP", 7)

print(s1.get_average())
print(s2.get_average())
print(l1.get_average())
print(l2.get_average())

print(s1 > s2)
print(s1 < s2)
print(s1 == s2)
print(s1 != s2)
print(s1 >= s2)
print(s1 <= s2)
print(l1 > l2)
print(l1 < l2)
print(l1 == l2)
print(l1 != l2)
print(l1 >= l2)
print(l1 <= l2)
print(s1 > l1)
print(l2 > s2)

students = [s1, s2]
lecturers = [l1, l2]
average_of_students(students, "OOP")
average_of_lecturers(lecturers, "OOP")
