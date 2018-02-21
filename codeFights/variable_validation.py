def variableName(name):
   
    valid_character_list = "abcdefghijklmnopqrstuvwxyz0123456789_"
    variable = name.lower()
    
    # check if variable is empty
    if not variable:
        return False
    
    # checks first character
    if not (variable[0].isalpha() or variable[0] == "_"):
        return False
    
    # checks the rest of the variable
    for c in variable[1:]:
        if not c in valid_character_list:
            return False
    
    return True