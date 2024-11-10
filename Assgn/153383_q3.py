class Employee:
    def __init__(self, name, employee_id, salary):
        """Initialize the employee with name, employee_id, and salary."""
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display the details of the employee including name, employee ID, and salary."""
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        """Update the salary of the employee."""
        self.salary = new_salary
        print(f"Salary of {self.name} has been updated to ${self.salary:.2f}.")


class Department:
    def __init__(self, department_name):
        """Initialize the department with a name and an empty list of employees."""
        self.department_name = department_name
        self.employees = []  # List to store employees in the department

    def add_employee(self, employee):
        """Add an employee to the department."""
        self.employees.append(employee)
        print(f"Employee {employee.name} has been added to the {self.department_name} department.")

    def calculate_total_salary(self):
        """Calculate and display the total salary expenditure for the department."""
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"\nTotal salary expenditure for the {self.department_name} department: ${total_salary:.2f}")

    def display_all_employees(self):
        """Display all employees in the department."""
        if self.employees:
            print(f"\nEmployees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the {self.department_name} department.")


# Interactive part to manage department and employees
def department_management_system():
    """Interactively manage a department, adding employees and displaying total salary expenditure."""
    # Get the department name from the user
    department_name = input("Enter the department name: ")

    # Initialize the department
    department = Department(department_name)

    while True:
        print("\nDepartment Management System")
        print("1. Add a new employee")
        print("2. Display total salary expenditure")
        print("3. Display all employees")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Collect employee details and add them to the department
            name = input("Enter the employee's name: ")
            employee_id = input("Enter the employee's ID: ")
            salary = float(input("Enter the employee's salary: "))

            # Create a new employee instance
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == '2':
            # Display the total salary expenditure for the department
            department.calculate_total_salary()

        elif choice == '3':
            # Display all employees in the department
            department.display_all_employees()

        elif choice == '4':
            print("Exiting the department management system.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the interactive department management system
department_management_system()
