import random
GAME_DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = -10
MAX_NUMBER = 10


def task():
    '''
    The function generates a random math expression and its correct answer.

    Returns:
        question (str): a string representing the randomly generated
            math expression in the format "a operator b".
        correct_answer (str): a string with the correct answer
            to the generated math expression.
    '''
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(['+', '-', '*'])
    question = f'{a} {operator} {b}'
    correct_answer = calculate_answer(question)
    return question, correct_answer


def calculate_answer(question):
    '''
    The function takes a math expression and returns its evaluated answer.

    Parameters:
        question (str): a string containing a math expression
            in the format "a operator b".

    Returns:
        str: a string representing the evaluated answer
            of the given math expression.
    '''
    return str(eval(question))
