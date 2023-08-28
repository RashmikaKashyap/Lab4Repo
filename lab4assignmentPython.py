class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_by_age(emp):
    return emp.age

def sort_by_name(emp):
    return emp.name

def sort_by_salary(emp):
    return emp.salary

def sort_employee_data(employees, sort_parameter):
    if sort_parameter == 1:
        employees.sort(key=sort_by_age)
    elif sort_parameter == 2:
        employees.sort(key=sort_by_name)
    elif sort_parameter == 3:
        employees.sort(key=sort_by_salary)
    else:
        print("Invalid sorting parameter")

def print_employee_data(employees):
    for emp in employees:
        print(f"ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sort_option = int(input("Enter the sorting parameter (1/2/3): "))
    
    sort_employee_data(employees, sort_option)
    print_employee_data(employees)
