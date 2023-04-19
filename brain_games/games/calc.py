import random
game_description = 'What is the result of the expression?'


def task():
    '''
    The function generates a random math expression and its correct answer.

    Returns:
        question (str): a string with the generated math expression in the format "a operator b".
        correct_answer (str): a string with the correct answer to the generated math expression.
    '''
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    operator = random.choice(['+', '-', '*'])
    question = f'{a} {operator} {b}'
    correct_answer = calculate_answer(question)
    return question, correct_answer


def calculate_answer(question):
    '''
    The function takes a math expression and returns its evaluated answer.

    Parameters:
        question (str): a string containing a math expression in the form "a operator b".

    Returns:
        answer (str): a string representing the evaluated answer of the given math expression.
    '''
    answer = str(eval(question))
    return answer
