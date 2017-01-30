import string
from helpers import alphabet_position, rotate_character, check_int
from sys import argv

def user_input_is_valid(cl_args):
    if len(cl_args) == 2 and check_int(cl_args[1]):
        return True
    else:
        return False


def encrypt(text,rot):
    new_text = ""
    for x in text:
        new_text = new_text + rotate_character(x,rot)
    return new_text


def main():
    if user_input_is_valid(argv):
        rot = int(argv[1])
    else:
        print("usage: python3 caesar.py n")
    message = input("Type a message:\n")
    print(encrypt(message,rot))

if __name__ == "__main__":
    main()
