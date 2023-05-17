import random
GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_INITIAL_TERM = -10
MAX_INITIAL_TERM = 10
MIN_COMMON_DIFF = 1
MAX_COMMON_DIFF = 5
MIN_MEMBERS_AMOUNT = 5
MAX_MEMBERS_AMOUNT = 10


def task():
    '''
    The function generates an arithmetic progression.
    Then it selects one member of the progression at random
    and replaces its value with a placeholder.

    Returns:
    question (str): a string representing the progression
        with one member missing.
    correct_answer (str): a string representing the value
        of the missing progression member.
    '''
    initial_term = random.randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    common_diff = random.randint(MIN_COMMON_DIFF, MAX_COMMON_DIFF)
    members_num = random.randint(MIN_MEMBERS_AMOUNT, MAX_MEMBERS_AMOUNT)
    progression = generate_progression(initial_term, common_diff, members_num)
    question_index = random.randint(members_num - members_num, members_num - 1)
    correct_answer = progression[question_index]
    progression[question_index] = '..'
    question = ' '.join(progression)
    return question, correct_answer


def generate_progression(initial_term, common_diff, members_num):
    '''
    The function generates an arithmetic progression based on
    the given initial term, common difference, and number of members.

    Args:
        initial_term (int): The first term of the arithmetic progression.
        common_diff (int): The common difference between consecutive terms.
        members_amount (int): The number of members in the progression.

    Returns:
        progression (list): A list containing the generated progression.
    '''
    progression = []
    for i in range(members_num):
        progression.append(str(initial_term + common_diff * i))
    return progression
