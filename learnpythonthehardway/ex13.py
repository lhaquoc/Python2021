# Parameters, Unpacking, Variables

from sys import argv


def main():
    script, first, second, third, fourth = argv
    user_name = input("input your user name here >")
    print(f"The script is called: {script}")
    print(f"Your first variable is: {first}")
    print(f"Your second variable is: {second}")
    print(f"Your third variable is: {third}")
    print(f"Your fourth variable is: {fourth}")
    print(f"Your name is: {user_name}")


if __name__ == '__main__':
    main()
