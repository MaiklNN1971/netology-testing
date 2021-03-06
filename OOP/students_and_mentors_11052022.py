class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grades_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                (course in self.courses_in_progress or course in self.finished_courses)\
                and 0 < round(grade) <=10:
            if course in lecturer.grades:
                lecturer.grades[course] += [round(grade)]
            else:
                lecturer.grades[course] = [round(grade)]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


lector_1 = Lecturer('Larry', 'Baks')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['C++']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['C++']

best_student.grades_lecturer(lector_1, 'Python', 5)
best_student.grades_lecturer(lector_1, 'C++', 2.6)
best_student.grades_lecturer(lector_1, 'C++', 35)

reviewer_1 = Reviewer('Piter', 'Buxin')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Python']

reviewer_1.rate_hw(best_student, 'Python', 210)
reviewer_1.rate_hw(best_student, 'Python', 110)
reviewer_1.rate_hw(best_student, 'Java', 10)

print(f'Имя: {reviewer_1.name} Фамилия: {reviewer_1.surname}')
print('Оценки студенту', best_student.grades)
print('Оценки лектору', lector_1.grades)
print(lector_1.courses_attached)
print(best_student.finished_courses)
