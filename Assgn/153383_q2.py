class Student:
    def initialize_student(self, full_name, student_id):
        """Initializing  the student's basic information."""
        self.full_name = full_name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignment names and their corresponding grades

    def submit_assignment(self, assignment_name, grade):
        """Store the assignment and its associated grade for the student."""
        self.assignments[assignment_name] = grade
        print(f"Assignment '{assignment_name}' with grade '{grade}' has been added for {self.full_name}.")

    def show_grades(self):
        """Display all assignments and their grades for the student."""
        if self.assignments:
            print(f"\nGrades for {self.full_name}:")
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print(f"{self.full_name} has no assignments or grades yet.")


class Instructor:
    def initialize_instructor(self, name, course_name):
        """Initialize the instructor's details and the course they are teaching."""
        self.name = name
        self.course_name = course_name
        self.students = []  # List to track all students enrolled in the course

    def enroll_student(self, student):
        """Add a student to the instructor's course."""
        self.students.append(student)
        print(
            f"Student {student.full_name} (ID: {student.student_id}) has been enrolled in the course '{self.course_name}'.")

    def assign_grade(self, student, assignment_name, grade):
        """Assign a grade to a student for a specific assignment."""
        if student in self.students:
            student.submit_assignment(assignment_name, grade)
        else:
            print(f"Error: Student {student.full_name} is not enrolled in this course.")

    def display_all_grades(self):
        """Show the list of all students and their grades in the course."""
        if self.students:
            print(f"\nCourse: {self.course_name}")
            for student in self.students:
                student.show_grades()
        else:
            print("No students have been enrolled in the course yet.")


# Interactive code for managing course enrollment and grading
def course_management():
    """Interactively manage course, enroll students, and assign grades."""
    # Sample Instructor
    instructor_name = input("Enter your name (Instructor): ")
    course_name = input("Enter the course name: ")

    # Initialize instructor with the entered details
    instructor = Instructor()
    instructor.initialize_instructor(instructor_name, course_name)

    while True:
        print("\nOnline Course Management System")
        print("1. Enroll a student")
        print("2. Assign grade to a student")
        print("3. View all students' grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Enroll a new student
            student_name = input("\nEnter the student's name: ")
            student_id = input("Enter the student's ID: ")

            # Initialize student with their details
            student = Student()
            student.initialize_student(student_name, student_id)
            instructor.enroll_student(student)

        elif choice == '2':
            if not instructor.students:
                print("There are no students enrolled in the course.")
                continue

            # Select a student to assign a grade
            print("\nSelect a student to assign a grade:")
            for idx, student in enumerate(instructor.students, 1):
                print(f"{idx}. {student.full_name} (ID: {student.student_id})")

            student_choice = int(input("Enter the number of the student: "))
            if 1 <= student_choice <= len(instructor.students):
                selected_student = instructor.students[student_choice - 1]

                # Collect assignment details from the instructor
                assignment_name = input(f"\nEnter the assignment name for {selected_student.full_name}: ")
                grade = input("Enter the grade for this assignment: ")

                # Assign the grade to the selected student
                instructor.assign_grade(selected_student, assignment_name, grade)
            else:
                print("Invalid selection, please try again.")

        elif choice == '3':
            # Display all students and their grades
            instructor.display_all_grades()

        elif choice == '4':
            print("Exiting the course management system.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the interactive course management system
course_management()
