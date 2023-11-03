class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.subjects = []

    def enroll_subject(self, subject):
        self.subjects.append(subject)

    def view_grades(self):
        for subject in self.subjects:
            subject.view_grades(self.student_id)

class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name
        self.grades = {}

    def add_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def view_grades(self, student_id):
        if student_id in self.grades:
            return self.grades[student_id]
        else:
            return "No grade available for this student."

class Diary:
    def __init__(self):
        self.students = {}
        self.subjects = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_subject(self, subject):
        self.subjects[subject.subject_id] = subject

    def record_grade(self, student_id, subject_id, grade):
        if student_id in self.students and subject_id in self.subjects:
            subject = self.subjects[subject_id]
            subject.add_grade(student_id, grade)
        else:
            return "Student or subject not found in the diary."

# Пример использования объектов:
# Создаем объекты Ученик, Предмет и Дневник
student1 = Student(1, "Alice", 16)
student2 = Student(2, "Bob", 17)

subject1 = Subject(101, "Math")
subject2 = Subject(102, "History")

diary = Diary()

# Добавляем Учеников и Предметы в Дневник
diary.add_student(student1)
diary.add_student(student2)

diary.add_subject(subject1)
diary.add_subject(subject2)

# Ученики записываются на предметы
student1.enroll_subject(subject1)
student2.enroll_subject(subject1)
student2.enroll_subject(subject2)

# Учителя записывают оценки
subject1.add_grade(1, 95)
subject1.add_grade(2, 88)
subject2.add_grade(2, 75)

print(student1.view_grades())
print(student2.view_grades())  
