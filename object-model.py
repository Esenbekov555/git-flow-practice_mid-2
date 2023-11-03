class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

class Subject:
    def __init__(self, name):
        self.name = name

class Diary:
    def __init__(self, student):
        self.student = student

    def show_student_info(self):
        print(f"Student Name: {self.student.name}")
        print(f"Student ID: {self.student.student_id}")

    def add_grade(self, subject, grade):
        self.student.add_grade(subject, grade)

    def get_student_average_grade(self):
        return self.student.get_average_grade()

math = Subject("Math")
biology = Subject("Biology")

student = Student("Mirrahim", 12345)

diary = Diary(student)

diary.add_grade(math, 90)
diary.add_grade(biology, 85)

diary.show_student_info()
print(f"Average Grade: {diary.get_student_average_grade()}")
