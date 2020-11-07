""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
from statistics import mean
import datetime


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]

def transmission_headers():
    return HEADERS

def add_employee(record):
    # writes a record to the end of the file
    # ARGS: record (list)
    with open(DATAFILE, "a") as file:
        separator = ";"
        row = separator.join(record)
        file.write(row + "\n")


def list_employees():
    list_of_employees = data_manager.read_table_from_file(DATAFILE)
    return list_of_employees
    #return list of lists


def update_employee(row, data_to_change, new_value):
    # overwrite string to a new string in specific field in the record
    # ARGS: 
    # row: (int): number of record in table
    # data_to_change (string)
    # new_value (string)
    list_of_employees = list_employees()
    record = list_of_employees[row]
    print(record)

    for elem in record:
        print(elem)
        if elem == data_to_change:
            i = record.index(elem)
            record[i] = new_value
            # print(elem)
            data_manager.write_table_to_file(DATAFILE, list_of_employees, ";")  
        else:
            pass


def get_oldest_and_youngest():
    list_of_employees = list_employees()
    list_of_dates = []
    for elem in list_of_employees:
        list_of_dates.append(elem[2])
    list_to_analyse = []
    for date in list_of_dates:
        string_date = date.replace("-", "0")
        int_date = int(string_date)
        list_to_analyse.append(int_date)

    max_number = max(list_to_analyse)
    youngest_index = list_to_analyse.index(max_number)
    youngest_employee = list_of_employees[youngest_index]

    min_number = min(list_to_analyse)
    oldest_index = list_to_analyse.index(min_number)
    oldest_employee = list_of_employees[oldest_index]
    return oldest_employee, youngest_employee
    # return two lists with the oldest younegst employee


def delete_employee(ID):
    # removes the selected record from the file
    # ARGS: ID (string)
    list_of_employees = list_employees()
    for elem in list_of_employees: 
        if ID in elem:
            list_of_employees.remove(elem)
    data_manager.write_table_to_file(DATAFILE, list_of_employees)
        
    
def  count_employees_per_value(value, index_of_column):
    list_of_employees = list_employees() 
    list_of_employees_with_same_value = []
    for elem in list_of_employees:
        if elem[index_of_column] == value:
            list_of_employees_with_same_value.append(elem)
    number_of_employees_with_same_value = len(list_of_employees_with_same_value)
    return list_of_employees_with_same_value, number_of_employees_with_same_value
         

def get_average_age():
    list_of_employees = list_employees() 
    list_of_dates = []
    for elem in list_of_employees:
        list_of_dates.append(elem[2])
    list_to_analyse = []
    for date in list_of_dates:
        year = date[0] + date[1] + date[2] + date[3]
        year = int(year)
        # in "date" year is represented by first 4 indexes
        list_to_analyse.append(year)
    average_year = mean(list_to_analyse)
    now = datetime.datetime.now()
    now = str(now)
    actual_year = now[0] + now[1] + now[2] + now[3] 
    actual_year = int(actual_year)
    ave = actual_year - average_year
    return ave
