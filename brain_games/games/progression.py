import random
game_description = 'What number is missing in the progression?'


def task():
    ''''
    The function generates an arithmetic progression.
    Then it selects one member of the progression at random
    and replaces its value with a placeholder.

    Returns:
    question (str): a string representing the progression
        with one member missing.
    correct_answer (str): a string representing the value
        of the missing progression member.
    '''
    progression_start = random.randint(-10, 10)
    progression_members_amount = random.randint(5, 10)
    progression_step = random.randint(1, 5)
    progression = []
    for i in range(progression_members_amount):
        progression.append(str(progression_start + progression_step * i))
    question_index = random.randint(0, progression_members_amount - 1)
    correct_answer = progression[question_index]
    progression[question_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer
