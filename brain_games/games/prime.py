import random
GAME_DESCRIPTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 10


def task():
    '''
    The function generates a random integer and a string
    indicating whether the generated number is prime or not.

    Returns:
        question (int): a randomly generated integer
            within a specific numerical range.
        correct_answer (str): a string indicating whether
            the generated number is prime ('yes') or not ('no').
    '''
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def is_prime(question):
    '''
    The function returns True if the entered number is prime.
    Otherwise the function returns False.

    Args:
        question (int): The number to check.

    Returns:
        bool: True if the number is prime, False if not.
    '''
    if question <= 1:
        return False
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return False
    return True
