import string

def is_pangram(s):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in s.lower():
            return False
    return True