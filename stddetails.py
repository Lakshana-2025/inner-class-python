import gc

import sys

 

class University:

    def __init__(self, university_name):

        self.university_name = university_name

        self.students = []

 

    # Inner Class

    class Student:

        def __init__(self, rollno, name, university):

            self.rollno = rollno

            self.name = name

            self.university = university

 

        def display_details(self):

            print(f"Roll No: {self.rollno}, Name: {self.name}, University: {self.university.university_name}")

 

    # Add Student

    def add_student(self):

        rollno = int(input("Enter Roll Number: "))

        name = input("Enter Name: ")

 

        student = self.Student(rollno, name, self) #student -> reference

        self.students.append(student)

 

        print(f"Student {name} added.")

        print("Reference count:", sys.getrefcount(student))

 

    # Remove Student

    def remove_student(self):

        rollno = int(input("Enter Roll Number to remove: "))

        for student in self.students:

            if student.rollno == rollno:

                print(f"Removing student {student.name}")

                print("Reference count before deletion:", sys.getrefcount(student))

 

                self.students.remove(student)

                del student

 

                gc.collect()

                print("Garbage collection done.")

                return

        print("Student not found")

 

    # Display All Students

    def display_all(self):

        if not self.students:

            print("No students available.")

        else:

            print(f"\nStudents in {self.university_name}:")

            for s in self.students:

                s.display_details()

 

 

# Main Program

uname = input("Enter University Name: ")

u = University(uname)

 

while True:

    print("\n1. Add Student")

    print("2. Remove Student")

    print("3. Display All Students")

    print("4. Exit")

 

    choice = input("Enter your choice: ")

 

    if choice == '1':

        u.add_student()

    elif choice == '2':

        u.remove_student()

    elif choice == '3':

        u.display_all()

    elif choice == '4':

        print("Exiting program...")

        break

    else:

        print("Invalid choice")
