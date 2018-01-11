from os.path import isfile


def input_float(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return float(user_input)
        else:
            print("Не верно, требуется число")


def input_file(prompt):
    while True:
        user_input = input(prompt)
        if isfile(user_input):
            return user_input
        else:
            print("Не верно, требуется путь к файлу")
