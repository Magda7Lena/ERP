import os

def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print("======================")
    print(title)
    print("======================")
    for elem in list_options:
        print(elem)
    pass


def print_message(message):
    print("======================")
    print(message)
    print("======================")



def print_general_results(result, label):
    if str(type(result).__name__) == "int":
        print(f'{label}: {result}')
    elif str(type(result).__name__) == "float":
        print(f'{label}: {round(result, 2)}')
    elif str(type(result).__name__) == "list":
        print(f'{label}:\n')
        for element in result:
            print(f'{element}; ')
    else:
        print("Unrecognized data type, please check for any errors")



# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/

def print_table(table, HEADERS):
    # os.system('cls' if os.name == 'nt' else 'clear')     
    print('{:>2} {:>15}{:>15}{:>15}{:>15}{:>15}'.format("No",HEADERS[0],HEADERS[1],HEADERS[2],HEADERS[3],HEADERS[4]))     
    print("==","="*78)     
    if len(table) > 1:                      
        counter = 1         
        for line in table:             
            print('{:>2} {:>15}{:>15}{:>15}{:>15}{:>15}'.format(int(counter),str(line[0]),str(line[1]),str(line[2]),str(line[3]),str(line[4])))             
            counter += 1         
        print()     
    else:         
        print('{:>2} {:>15}{:>15}{:>15}{:>15}{:>15}'.format(str(table[0]),str(table[1]),str(table[2]),str(table[3]),str(table[4])))         
        print()


def get_input(label):
    return input(label)


# def get_inputs(labels):
#     """Gets a list of string inputs from the user.

#     Args:
#         labels: list - the list of the labels to be displayed before each prompt
#     """
#     pass


def print_error_message(message):
    print("======================")
    print(message)
    print("======================")

