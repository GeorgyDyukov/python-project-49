import random
GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = -10
MAX_NUMBER = 10


def task():
    '''
    The function generates a random integer and a string
    indicating whether the generated number is even or odd.

    Returns:
        question (int): a randomly generated integer
            within a specific numerical range.
        correct_answer (str): a string indicating whether
            the generated number is even ('yes') or odd ('no').
    '''
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def is_even(question):
    '''
    The function returns True if the entered number is even
    and False if the entered number is odd.

    Args:
        question (int): The number to check.

    Returns:
        bool: True if the number is even, False if the number is odd.
    '''
    return question % 2 == 0
