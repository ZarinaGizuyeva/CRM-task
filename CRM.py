import enum


class Subject(enum.StrEnum):
    MATHS = 'maths'
    HISTORY = 'history'
    ECONOMICS = 'economics'
    ENGLISH = 'english'
    PSYCHOLOGY = 'psychology'
    INFORMATICS = 'informatics'

    def __repr__(self):
        return self.value


class Mark(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.value


class Week(enum.Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    def __repr__(self):
        return self.name


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return f"{self.name} {self.surname}"

    @staticmethod
    def get_schedule(day: Week):
        match day:
            case Week.MONDAY:
                return Subject.MATHS, Subject.ENGLISH
            case Week.TUESDAY:
                return Subject.HISTORY, Subject.ECONOMICS
            case Week.WEDNESDAY:
                return Subject.INFORMATICS
            case Week.THURSDAY:
                return Subject.PSYCHOLOGY
            case Week.FRIDAY:
                return Subject.INFORMATICS
            case _:
                return tuple()


class Student(User):
    students_marks = dict()  # словарь с оценками учеников, где ключ ученик, значения список оценок

    def check_marks(self):
        if self in self.students_marks:
            return self.students_marks[self]
        return self.students_marks

    def do_homework(self, subject: Subject):
        return f'{self} делает домашку по {subject}'


class Teacher(User):
    teachers = dict()  # словарь с учителями и предметами

    def teach(self, subject: Subject):
        self.teachers.setdefault(subject, self)

    @classmethod
    def give_marks(cls, student: Student, mark: Mark):  # ставим оценки ученикам
        if student not in Student.students_marks:
            Student.students_marks[student] = [mark]
        Student.students_marks[student].append(mark)


Student1 = Student('Sasha', 'Snigirev')
Student2 = Student('Kolya', 'Pak')
Teacher1 = Teacher('Pavel', 'Stepanov')
Teacher1.teach(Subject.HISTORY)
Teacher1.give_marks(Student1, Mark.ONE)
Teacher2 = Teacher('Anton', 'Kashin')
Teacher2.teach(Subject.ECONOMICS)
Teacher2.give_marks(Student2, Mark.THREE)
Teacher2.give_marks(Student1, Mark.FOUR)
Student1.check_marks()
Student1.get_schedule(Week.MONDAY)
Student3 = Student('Tolik', 'Losev')
Student3.check_marks()
Student1.get_schedule(Week.SUNDAY)
print(Teacher.teachers)
print(Student.students_marks)
