from typing import List

Employee = List[str]
Employees = List[Employee]


def increase_payment_for_employees_on_position(employees: Employees, position: str, rate: float):
    # TODO
    for employee in employees:
        if works_on_position(employee, position) == True:
            print(works_on_position(employee, position))
            employee[5] = str(round(int(employee[5]) * rate))
    return employees
pass


def increase_payment_for_employee(employee: Employee, rate: float):
    # TODO
    pass

def works_on_position(employee: Employee, position: str) -> bool:
    # TODO
    if employee[-2] == position:
        return True   
    return False


def parse_file(file_name: str) -> Employees:
    # TODO
    Employees = []
    with open(file_name) as file:
        for line in file:
            line.strip("\n")
            Employee = line.split(";")
            Employees.append(Employee)
    return Employees


def save_to_file(file_name: str, data: Employees):
    # TODO
    sep = ";"
    with open(file_name, "w") as file:
        for employee in data:
            data_entrance = sep.join(employee)
            file.write(data_entrance)
pass

DB_FILE = "D:\\FT_Folder\\codeP\\si\\employees.csv"
POSITION = "Web developer junior"
RATE = 1.15

# TODO
save_to_file(DB_FILE, increase_payment_for_employees_on_position(parse_file(DB_FILE), POSITION, RATE))