import re


def has_upper_and_lower_case(password):
    count = 0
    if re.match(".*[a-z]+", password) and re.match(".*[A-Z]+", password):
        return 2
    return -2


def has_numeric_digits(password):
    if re.match(".*\d", password):
        return 1
    return -1


def has_special_char(password):
    if re.match(".*\W", password):
        return 2
    return -2


def good_length(password):
    if len(password) >= 6:
        return 2
    return -2


def is_in_blacklist_file(password):
    with open("blacklist.txt", "r") as file:
        for line in file:
            if password in line:
                return -3
    return 3


def get_password_strength(password):
    strength = 0
    strength += has_upper_and_lower_case(password)
    strength += has_numeric_digits(password)
    strength += has_special_char(password)
    strength += good_length(password)
    try:
        strength += is_in_blacklist_file(password)
    except FileNotFoundError:
        pass
    if strength < 0:
        return 0
    return strength


if __name__ == '__main__':
    password = input("Input password:")
    password_strength = get_password_strength(password)
    print("Password strength = ", password_strength)
