from view import terminal as view
from model.hr import hr
from model import util



def list_employees():
    list_of_employees = hr.list_employees()
    HEADERS = hr.transmission_headers()
    view.print_table(list_of_employees, HEADERS)


def add_employee():
    name = view.get_input("Give name: ")
    if len(name) > 15:
        name = view.get_input("Give name: ")
    date_of_birth = view.get_input("Give date of birth in format YYYY-MM-DD: ")

    n_department = view.get_input("Choose department \n 1. Production \n 2. Sales \n 3. HR \n")
    department = " "
    if n_department == "1":
        department = "Production"
    if n_department == "2":
        department = "Sales"
    if n_department == "3":
        department = "HR"
    clearance = view.get_input("Give clearance level (0-7): ")
    ID = util.generate_id()
    employee_record = [ID, name, date_of_birth, department, clearance]
    hr.add_employee(employee_record)


def update_employee():
    list_employees()
    row_num = view.get_input("Provide No: ")
    row_num = int(row_num) - 1
    data_to_change = view.get_input("Provide value to change: ")
    new_value = view.get_input("Provide correct value: ")
    hr.update_employee(row_num, data_to_change, new_value)
    

def delete_employee():
    list_employees()
    id_to_delete = view.get_input("Provide ID to delete: ")
    hr.delete_employee(id_to_delete)


def get_oldest_and_youngest():
    oldest, youngest = hr.get_oldest_and_youngest()
    label_1 = "Oldest employee"
    view.print_general_results(oldest, label_1)
    label_2 = "Youngest employee"
    view.print_general_results(youngest, label_2)


def get_average_age():
    average = hr.get_average_age()


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    index_in_table = 4
    # column "clearance" has index 4 in table
    level = view.get_input(" Provide level of clerance to display employee: ")
    list_of_employees_with_same_level, number_of_employees_with_same_level = hr.count_employees_per_value(level, index_in_table)
    print(number_of_employees_with_same_level)
    print(list_of_employees_with_same_level)


def count_employees_per_department():
    index_in_table = 3
    # column "department" has index 3 in table
    department = "Sales"
    list_of_employees_with_same_department, number_of_employees_with_same_department = hr.count_employees_per_value(department, index_in_table)
    print(number_of_employees_with_same_department)
    print(list_of_employees_with_same_department)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["(0) Back to main menu",
               "(1) List employees",
               "(2) Add new employee",
               "(3) Update employee",
               "(4) Remove employee",
               "(5) Oldest and youngest employees",
               "(6) Employees average age",
               "(7) Employees with birthdays in the next two weeks",
               "(8) Employees with clearance level",
               "(9) Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
