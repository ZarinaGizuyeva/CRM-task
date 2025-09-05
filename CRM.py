import random
class Subject:
    subjects = dict() #здесь словарь, где ключ это предмет, а значение учитель
    def __init__(self, subject_name):
        self.subject_name = subject_name

class Users:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"

class Student(Users):

    list_of_students = [] #список всех учеников
    students_marks = dict() #словарь с оценками учеников, где ключ ученик, значения список оценок
    def add_students(self):
        self.list_of_students.append(self)

    def do_homework(self, subject_name):
        if subject_name in Subject.subjects:
            print(f'{self} делает домашку по {Subject.subjects[subject_name]}')
        else: print(f'{self} не изучает такой предмет')

    def check_marks(self, subject_name):
        if subject_name in Subject.subjects:
            print(f'{self} получил оценку по {Subject.subjects[subject_name]}')
        else: print(f'{self} не изучает такой предмет')

    def take_exam(self):
        print(f'{self} сдает экзамен у преподавателя {Teacher1}')

class Teacher(Users):
    def teach(self, subject_name):
        Subject.subjects.setdefault(subject_name, self.surname) #добавляю предметы и преподавателей в словарь
        print(f'{self} преподает {subject_name}')
        print(Subject.subjects)

    def give_marks(self): #ставим оценки ученикам
        for student in Student.list_of_students:
            if student not in Student.students_marks:
                Student.students_marks[student] = [random.choice([1, 2, 3, 4, 5])]
            elif student in Student.students_marks:
                Student.students_marks[student].append(random.choice([1, 2, 3, 4, 5]))
        print(Student.students_marks)

Student1 = Student('Sasha', 'Snigirev')
Student2 = Student('Kolya', 'Pak')
Teacher1 = Teacher('Pavel', 'Stepanov')
Teacher1.teach('Maths')
Student1.add_students()
Student2.add_students()
Teacher1.give_marks()
Teacher2 = Teacher('Anton', 'Kashin')
Teacher2.teach('History')
Teacher2.give_marks()
Student1.do_homework('English')
