class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # Задание 3, средняя оценка
        self.avg_grade = 0

    # Задание 3, переопределение __str__
    def __str__(self):
        return f'''Имя: {self.name}
            Фамилия: {self.surname}
            Средняя оценка за домашние задания: {self.avg_grade}
            Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
            Завершенные курсы: {', '.join(self.finished_courses)}'''

    # Задание 3, перегрузка операторов
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade < other.avg_grade

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade > other.avg_grade

    def __le__(self, other):
        if isinstance(other, Student):
            return self.avg_grade <= other.avg_grade

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.avg_grade >= other.avg_grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_grade == other.avg_grade

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.avg_grade != other.avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Задание 1, класс Lecturer
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_lecture_rates = {}
        # Задание 3, средняя оценка лектора
        self.avg_grade = 0

    # Задание 3, переопределение __str__
    def __str__(self):
        return f'''Имя: {self.name}
            Фамилия: {self.surname}
            Средняя оценка за лекции: {self.avg_grade}'''

    # Задание 3, перегрузка операторов
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade < other.avg_grade

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade > other.avg_grade

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade <= other.avg_grade

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade >= other.avg_grade

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade == other.avg_grade

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade != other.avg_grade

    # Задание 2, оценки лекторов
    def rate_lecture(self, course, grade):
        if 1 > grade < 10:
            print('Неправильная оценка')
            return
        if course in self.courses_attached:
            if course in self.student_lecture_rates.keys():
                self.student_lecture_rates[course] += [grade]
            else:
                self.student_lecture_rates[course] = [grade]
            # Задание 3, средняя оценка лектора
            # Если ноль, значит, еще никаких оценок не выставлено, средняя равна единственной оценке
            if self.avg_grade == 0:
                self.avg_grade = grade
            else:
                self.avg_grade = (self.avg_grade + grade) / 2
        else:
            print('Ошибка')
            return


# Задание 1, класс Reviewer
class Reviewer(Mentor):
    # Задание 3, переопределение __str__
    def __str__(self):
        return f'''Имя: {self.name}
            Фамилия: {self.surname}'''

    # Задание 2, оценки студентов
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            # Задание 3, средняя оценка студента
            # Если ноль, значит, еще никаких оценок не выставлено, средняя равна единственной оценке
            if student.avg_grade == 0:
                student.avg_grade = grade
            else:
                student.avg_grade = (student.avg_grade + grade) / 2
        else:
            print('Ошибка')
            return


student1 = Student('Rage', 'Against', 'The Machine')
student1.courses_in_progress += ['Python', 'Golang', 'Ruby']
student2 = Student('Liquid', 'Tension', 'Experiment')
student2.courses_in_progress += ['Python', 'C#', 'PHP']

reviewer1 = Reviewer('Perfect', 'Circle')
reviewer1.courses_attached += ['Python', 'Golang', 'Ruby']
reviewer2 = Reviewer('Pearl', 'Jam')
reviewer2.courses_attached += ['Python', 'C#', 'PHP']

lecturer1 = Lecturer('Alter', 'Bridge')
lecturer1.courses_attached += ['C#', 'Ruby', 'Python', 'Golang']
lecturer2 = Lecturer('Machine', 'Head')
lecturer2.courses_attached += ['Python', 'C#']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student1, 'Golang', 3)
reviewer1.rate_hw(student1, 'Ruby', 10)
reviewer1.rate_hw(student1, 'Ruby', 4)
reviewer2.rate_hw(student2, 'PHP', 10)
reviewer2.rate_hw(student2, 'C#', 5)
reviewer2.rate_hw(student2, 'Python', 6)

lecturer2.rate_lecture('Python', 1)
lecturer2.rate_lecture('C#', 7)
lecturer1.rate_lecture('Python', 3)
lecturer1.rate_lecture('C#', 4)
lecturer1.rate_lecture('Golang', 4)

# Задание 3, список студентов и список преподавателей
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

# Задание 3, функция подсчета средней оценки
def students_avg_grade(students_list, course):
    avg_grade = 0
    for student in students_list:
        if course in student.courses_in_progress:
            course_avg = sum(student.grades[course]) / len(student.grades[course])
            if avg_grade == 0:
                avg_grade = course_avg
            else:
                avg_grade = (avg_grade + course_avg) / 2
    return avg_grade

# Задание 3, функция подсчета средней оценки
def lecturers_avg_grade(lecturers_list, course):
    avg_grade = 0
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            course_avg = sum(lecturer.student_lecture_rates[course]) / \
                         len(lecturer.student_lecture_rates[course])
            if avg_grade == 0:
                avg_grade = course_avg
            else:
                avg_grade = (avg_grade + course_avg) / 2
    return avg_grade

# Задание 4, проверка
print(students_avg_grade(students_list, 'Python'))
print(lecturers_avg_grade(lecturers_list, 'C#'))