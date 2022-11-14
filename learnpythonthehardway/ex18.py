# Names, Variables, Code, Functions
# this one is like your script

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args actually pointless


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# take one argument


def print_one(arg1):
    print(f"arg1: {arg1}")

# take no argument


def print_none():
    print("I got nothin'.")


def main():
    print_two("Zed", "Shaw")
    print_two_again("Zed", "Shaw")
    print_one("First!")
    print_none()


if __name__ == '__main__':
    main()
