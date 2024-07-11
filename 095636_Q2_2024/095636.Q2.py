class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grade}")

    def average_grade(self, student_name):
        for student in self.students:
            if student.name == student_name:
                if not student.grades:
                    return "No grades available ."
                total_grades = sum(student.grades.values())
                average_grade = total_grades / len(student.grades)
                return average_grade
        return f"Student '{student_name}' not found."

    def get_subject_average(self, subject):
        total_grades = 0
        num_students_with_grades = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += student.grades[subject]
                num_students_with_grades += 1
        if num_students_with_grades == 0:
            return f"No students have grades for '{subject}'."
        class_average = total_grades / num_students_with_grades
        return class_average
