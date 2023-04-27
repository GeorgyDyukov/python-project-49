import prompt


def welcome_user():
    '''
    The function greets the user and prompts for their name.

    Returns:
        name (str): The name of the user entered via the prompt.
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def complete_game_lap(question, correct_answer):
    '''
    The function presents a math expression (question) to the user,
    prompts for an answer, and checks whether the provided answer is correct.

    Parameters:
        question (str): a string containing the math expression (question).
        correct_answer (str): a string representing the correct answer
            to the given math expression(question).

    Returns:
        True if the user's answer matches the correct answer.
        False if the user's answer does not match the correct answer.
    '''
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. \
        Correct answer was '{correct_answer}'.")
        return False


def play_game(game):
    '''
    The function is a game engine that runs a specified game and prompts
    the user to answer math questions until they have correctly answered
    three questions or have given an incorrect answer.

    Parameters:
        game: an object representing the game to be played. The object
            must have two methods: task() and game_description.
            The task() method generates a random math expression and its
            correct answer. The game_description method returns a string
            describing the game.
    '''
    name = welcome_user()
    print(game.game_description)
    counter = 0
    while counter < 3:
        question, correct_answer = game.task()
        if complete_game_lap(question, correct_answer):
            counter += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')
