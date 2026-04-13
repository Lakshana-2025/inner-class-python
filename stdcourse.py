 

import sys

import gc

 

class Student:

    def __init__(self, roll_no, name):

        self.roll_no = roll_no

        self.name = name

        self.courses = []   # list to store Course objects

 

    # Inner Class

    class Course:

        def __init__(self, course_name, duration):

            self.course_name = course_name

            self.duration = duration

 

        def display_course(self):

            print(f"Course: {self.course_name}, Duration: {self.duration}")

 

    # Add Course

    def add_course(self):

        course_name = input("Enter Course Name: ")

        duration = input("Enter Course Duration: ")

 

        course = Student.Course(course_name, duration)

        self.courses.append(course)

 

        print(f"Course {course_name} added.")

        print("Reference count of course:", sys.getrefcount(course))

 

    # Display Student Details

    def display_details(self):

        print(f"\nRoll No: {self.roll_no}, Name: {self.name}")

        if not self.courses:

            print("No courses enrolled.")

        else:

            print("Enrolled Courses:")

            for c in self.courses:

                c.display_course()

 

 

# Manager Class

class College:

    def __init__(self):

        self.students = []

 

    # Register Student

    def add_student(self):

        roll_no = int(input("Enter Roll No: "))

        name = input("Enter Name: ")

 

        student = Student(roll_no, name)

        self.students.append(student)

 

        print(f"Student {name} registered.")

        print("Reference count of student:", sys.getrefcount(student))

 

    # Add Course to Student

    def enroll_course(self):

        roll_no = int(input("Enter Roll No: "))

 

        for student in self.students:

            if student.roll_no == roll_no:

                student.add_course()

                return

 

        print("Student not found")

 

    # Display All Students

    def display_all(self):

        if not self.students:

            print("No students available.")

        else:

            for student in self.students:

                student.display_details()

 

    # Remove Student

    def remove_student(self):

        roll_no = int(input("Enter Roll No to remove: "))

 

        for student in self.students:

            if student.roll_no == roll_no:

                print(f"Removing Student {student.name}")

                print("Reference count before deletion:", sys.getrefcount(student))

 

                self.students.remove(student)

                del student

 

                gc.collect()

                print("Garbage collection done.")
