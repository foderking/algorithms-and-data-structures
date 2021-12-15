from math import floor
from random import random


def getArray(max, length):
    return [ floor(random() * max) for i in range(length)]