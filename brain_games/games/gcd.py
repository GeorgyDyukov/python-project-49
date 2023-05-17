import random
from math import gcd
GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = -10
MAX_NUMBER = 10


def task():
    '''
    The function generates a random math expression in the form of two randomly
    generated integers and calculates their greatest common divisor (GCD).

    Returns:
        question (str): a string representing the randomly generated
            math expression in the format 'a b'.
        correct_answer (str): a string representing the greatest common divisor
            of the two randomly generated integers.
    '''
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{a} {b}'
    correct_answer = find_gcd(a, b)
    return question, correct_answer


def find_gcd(a, b):
    '''
    The function takes two integers and finds their greatest common divisor.

    Parameters:
        a (int): A random number within a specific numerical range.
        b (int): A random number within a specific numerical range.

    Returns:
        str: a string representing the greatest common divisor
            of the two input integers.
    '''
    return str(gcd(a, b))
