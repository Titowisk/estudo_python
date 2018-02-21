import os

def main():

    print("\nList Keeper Software\n")

    lst_files = get_lst_files()
    print_list(lst_files)
    file_name, file_items = choose_or_create_file(lst_files)

    edited_file_items = file_items
    file_items_was_changed = False
    while True:

        print_list(edited_file_items, file_name=file_name)
        if not edited_file_items:
            message, options = "[A]dd [Q]uit [a]:", "AaQq" 
        else:
            if file_items_was_changed:
                message, options = "[A]dd [D]elete [S]ave [Q]uit [a]:", "AaDdSsQq"
            else:
                message, options = "[A]dd [D]elete [Q]uit [a]:", "AaDdQq"
    
        # User choose and action is triggered
        user_choice = choice(message, options)

        if user_choice in "Aa":
            edited_file_items = add(edited_file_items)
            file_items_was_changed = True
        elif  user_choice in "Dd":
            edited_file_items = delete(edited_file_items)
            file_items_was_changed = True
        elif  user_choice in "Ss":
            save(edited_file_items, file_name)
            file_items_was_changed = False
        else:
            if file_items_was_changed:
                answear = get_string("Do you want to save changes? (y/n)", "yes/no", "y")
                if answear.lower() in "yes":
                    save(edited_file_items, file_name)
            break


def add(list_of_items):

    new_item = get_string(
        "Type the name of the new item", "new item", minimum_length=3
        )
    list_of_items.append(new_item)

    return list_of_items

def delete(list_of_items):

    item_selected = get_integer(
        "Select a item by its number to delete (or 0 to cancel)", "item selected",
        minimum=1, maximum=len(list_of_items)
        )
    if item_selected == 0:
        return list_of_items
    for index, item in enumerate(list_of_items, start=1):
        if item_selected == index:
            list_of_items.remove(item)
    
    return list_of_items

def save(list_of_items, file_name):

    fh = open(file_name, 'w', encoding='utf8')
    for item in list_of_items:
        print(item, file=fh)
    fh.close()
    print("List saved!")


def choice(message, options):
    
    while True:
        print()
        choice = input(message)
        if not choice:
            choice = "a"
            break
        elif choice not in options:
            print("You must type {options} to choose a action.".format(options=options))
            continue
        else:
            break
    return choice


def get_lst_files():

    all_files = os.listdir(".") # returns a list of all filenames
    lst_files = [x for x in all_files if x.endswith(".lst")] # creates a list of strings with all filenames that ends with .lst
    if not lst_files: # If there are no lst files
        return [] # user must create one in the ... function
    else:   # if there are lst files
        return lst_files


def choose_or_create_file(list_of_files):

    if not list_of_files: # user must create one empty file
        return create_file()
    else:
        option = get_integer(
            "Choose a file by its number, or 0 to create a new one", "filename",
            minimum=1, maximum=len(list_of_files)
            )
        if option == 0: # user create a empty file
            return create_file()
        else:
            for number, name in enumerate(list_of_files, start=1):
                if option == number:
                    choosen_file = name
        fh = open(choosen_file, 'r', encoding='utf8')
        file_items = []
        for line in fh:
            file_items.append(line.rstrip())
        file_name = choosen_file

    return file_name, file_items

def create_file():
    new_file_name = get_string("Choose a name for the new file (or 0 to cancel)", "new_file_name", minimum_length=3)
    if ".lst" not in new_file_name:
        new_file_name += ".lst"
    new_file = open(new_file_name, 'x', encoding='utf8')
    new_file.close()
    
    file_name = new_file_name
    file_items = []
    return file_name, file_items

def print_list(list_of_names, file_name=""): # receives a list of filenames (string) or list of items (string)
    if file_name:
        print("\n---- Editting {} ----\n".format(file_name))
    if list_of_names:
        for index, name in enumerate(list_of_names, start=1):
            line = "{index}: {name}".format(index=index, name=name)
            print(line)
        print()
    else:
        print("\n-- there are no items in list --\n")
        print()


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                                     name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                        "{minimum_length} and at most "
                        "{maximum_length} characters".format(
                        **locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                        "and {maximum} inclusive{0}".format(
                        " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))

main()