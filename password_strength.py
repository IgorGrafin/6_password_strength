import re
import os
import getpass


def has_upper_and_lower_case(password):
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
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


def is_in_blacklist_file(password, blacklisted_words):
    if password in blacklisted_words:
        return -3
    return 3


def get_blacklisted_words():
    if not os.path.exists("blacklist.txt"):
        return None
    with open("blacklist.txt", "r") as file:
        return file.read().split("\n")


def get_password_strength(password):
    strength = sum([has_upper_and_lower_case(password),
                    has_numeric_digits(password),
                    has_special_char(password),
                    good_length(password)])

    blacklisted_words = get_blacklisted_words()
    if blacklisted_words:
        strength += is_in_blacklist_file(password, blacklisted_words)
    if strength < 0:
        return 0
    return strength


if __name__ == '__main__':
    password = getpass.getpass(prompt="Enter your password: ")
    print("Password strength = ", get_password_strength(password))
