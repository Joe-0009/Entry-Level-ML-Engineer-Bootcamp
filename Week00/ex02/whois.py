import sys


def whoami():
    if len(sys.argv) < 2:
        print()
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif (sys.argv[1].isnumeric() == 0):
        print("AssertionError: argument is not an integer")
    elif (int(sys.argv[1]) % 2 == 0):
        print("I'm Even.")
    elif (int(sys.argv[1]) % 2 != 0):
        print("I'm Odd.")
    elif (int(sys.argv[1]) == 0):
        print("I'm Zero.")


whoami()
