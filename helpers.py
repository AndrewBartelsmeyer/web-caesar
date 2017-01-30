import string


def user_input_is_valid(cl_args):
    if len(cl_args) == 2 and check_int(cl_args[1]):
        return True
    else:
        return False

def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def alphabet_position(letter):
    letter = letter.upper()
    alphabet = string.ascii_uppercase
    position = alphabet.find(letter)
    return position


def rotate_character(char, rot):
    alphabet = string.ascii_uppercase
    if char.isalpha():
        new_char = alphabet[(alphabet_position(char) + rot) % 26]
        if char.islower():
            new_char = new_char.lower()
    else:
        new_char = char
    return new_char
