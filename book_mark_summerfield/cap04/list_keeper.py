import os

def main():

    print("\nList Keeper Software\n")
    filename, filename_items = get_file()

def get_file():
    all_files = os.listdir(".") # returns a list of all filenames
    lst_files = [x for x in all_files if x.endswith(".lst")] # creates a list of strings with all filenames that ends with .lst

    if not lst_files: # If are no lst files
        # user must creat one
        print("-- there are no items in list --")
        new_list_filename = get_string("Enter the name of the new list (or 0 to cancel)", "new list", minimum_length=3)
        if new_list_filename == '0':
            print("Cancelled")
            return
        if ".lst" not in new_list_filename:
            new_list_filename += ".lst"
        empty_file = open(new_list_filename, 'x', encoding='utf8')
        # in this case
        filename = new_list_filename
        filename_items = []
    else:   # if there are lst files
        # show all lst lists available
        print_list(lst_files)
        # choose one
        choosen_filename = get_string("Choose a filename (or 0 to cancel)", "filename")
        if choosen_filename == '0':
            print("Cancelled")
            return
        fh = open(choosen_filename, 'r', encoding='utf8')
        filename_items = []
        for line in fh:
            filename_items.append(line)

    return filename, filename_items

def print_list(list_of_names): # receives a list of filenames (string) or list of items (string)

    for index, name in enumerate(list_of_names):
        line = "{index}: {name}".format(index=index, name=name)
        print(line)
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