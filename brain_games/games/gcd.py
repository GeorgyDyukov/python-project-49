import random
from math import gcd
game_description = 'Find the greatest common divisor of given numbers.'


def task():
    '''
    The function generates a random math expression in the form of two randomly
    generated integers and calculates their greatest common divisor (GCD).

    Returns:
        question (str): a string representing the randomly generated
            math expression in the form of 'a b'.
        correct_answer (str): a string representing the greatest common divisor
            of the two randomly generated integers.
    '''
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    question = f'{a} {b}'
    correct_answer = find_gcd(a, b)
    return question, correct_answer


def find_gcd(a, b):
    '''
    The function takes two integers and finds their greatest common divisor.

    Parameters:
        a (int): A random number between -10 and 10.
        b (int): A random number between -10 and 10.

    Returns:
        str: a string representing the greatest common divisor
            of the two input integers.
    '''
    return str(gcd(a, b))
