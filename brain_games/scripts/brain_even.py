#!/usr/bin/env python3
from brain_games.scripts.game_engine import welcome_user
import random
import prompt


def is_even(num):
    '''
    A function that returns 'yes' if the entered number is even, and 'no' if the entered number is odd.
    
    Args:
    number (int): The number to check.

    Returns:
    str: 'yes' if the number is even, 'no' if the number is odd.
    '''
    if num % 2 == 0:
        return 'yes'
    return 'no'


def complete_game_lap(name):
    '''
    A function that checks whether the user's answer matches the correct answer.
    '''
    num = random.randint(-10, 10)
    print(f'Question: {num}')
    answer = prompt.string('Your answer: ')
    if answer == is_even(num):
        print('Correct!')
        flag = True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(num)}'.")
        print(f"Let's try again, {name}!")
        flag = False
    return flag


def engine(name):
    '''
    A function that manages the game loop of questions.
    '''
    counter = 0
    while counter < 3:
        flag = complete_game_lap(name)
        if flag == True:
            counter += 1
        else:
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


def main():
    '''
    The main function of the game that greets the user, starts the game loop of questions, and verifies the user's responses to each question.
    '''
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(name)


if __name__ == '__main__':
    main()