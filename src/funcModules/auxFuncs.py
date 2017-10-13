# -*- coding: UTF-8 -*-
from random import Random

def random_str(randomlength=6):
    string = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for l in range(randomlength):
        string += chars[random.randint(0, length)]
    return string

def help():
    print("")

