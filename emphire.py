import gc
import sys

class Employee:
    def __init__(self, emp_id, name, address):
        self.emp_id = emp_id
        self.name = name
        self.address = address   # reference to Address object

    # Inner Class
    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state

        def display_address(self):
            print(f"City: {self.city}, State: {self.state}")

    # Display Employee Details
    def display_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}")
        self.address.display_address()


# Manager Class to handle employees
class Company:
    def __init__(self):
        self.emp_list = []

    # Hire Employee
    def add_employee(self):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        city = input("Enter City: ")
        state = input("Enter State: ")

        addr = Employee.Address(city, state)
        emp = Employee(emp_id, name, addr)

        self.emp_list.append(emp)

        print(f"Employee {name} hired.")
        print("Reference count:", sys.getrefcount(emp))

    # Display Employees
    def display_all(self):
        if not self.emp_list:
            print("No employees available.")
        else:
            print("\nEmployee Details:")
            for emp in self.emp_list:
                emp.display_details()

    # Remove Employee
    def remove_employee(self):
        emp_id = int(input("Enter Employee ID to remove: "))

        for emp in self.emp_list:
            if emp.emp_id == emp_id:
                print(f"Removing Employee {emp.name}")
                print("Reference count before deletion:", sys.getrefcount(emp))

                self.emp_list.remove(emp)
                del emp

                gc.collect()
                print("Garbage collection done.")
                return

        print("Employee not found")

# Main Program
c = Company()

while True:
    print("\n1. Hire Employee")
    print("2. Remove Employee")
    print("3. Display Employees")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        c.add_employee()
    elif choice == '2':
        c.remove_employee()
    elif choice == '3':
        c.display_all()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
