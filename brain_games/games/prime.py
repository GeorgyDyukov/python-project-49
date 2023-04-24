import random
game_description = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def task():
    '''
    The function generates a random integer and a string
    indicating whether the generated number is prime or not.

    Returns:
        question (int): a randomly generated integer between 0 and 10.
        correct_answer (str): a string indicating whether
            the generated number is prime ('yes') or not ('no').
    '''
    question = random.randint(0, 10)
    correct_answer = is_prime(question)
    return question, correct_answer


def is_prime(question):
    '''
    The function returns 'yes' if the entered number is prime.
    Otherwise the function returns 'no'.

    Args:
        question (int): The number to check.

    Returns:
        str: 'yes' if the number is prime, 'no' if not.
    '''
    if question <= 1:
        return 'no'
    for i in range(2, int(question ** 0.5) + 1):
        if question % i == 0:
            return 'no'
    return 'yes'
