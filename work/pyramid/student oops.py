class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class Menu:
    def _init_(self):
        self.students = []

    def add_student(self):
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))  # No exception handling, assumes valid input
        grade = input("Enter student's grade: ")
        student = Student(name, age, grade)
        self.students.append(student)
        print("Student added successfully")
