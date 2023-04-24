import random
game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    '''
    The function generates a random integer and a string
    indicating whether the generated number is even or odd.

    Returns:
        question (int): a randomly generated integer between -10 and 10.
        correct_answer (str): a string indicating whether the generated number
            is even ('yes') or odd ('no').
    '''
    question = random.randint(-10, 10)
    correct_answer = is_even(question)
    return question, correct_answer


def is_even(question):
    '''
    The function returns 'yes' if the entered number is even,
    and 'no' if the entered number is odd.

    Args:
        question (int): The number to check.

    Returns:
        str: 'yes' if the number is even, 'no' if the number is odd.
    '''
    if question % 2 == 0:
        return 'yes'
    return 'no'
