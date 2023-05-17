import prompt
MAX_QUESTIONS = 3


def play_game(game):
    '''
    The function is a game engine that runs a specified game and prompts
    the user to answer math questions until they have correctly answered
    three questions or have given an incorrect answer.

    Parameters:
        game: an object representing the game to be played. The object
            must have two methods: task() and GAME_DESCRIPTION.
            The task() method generates a random math expression and its
            correct answer. The GAME_DESCRIPTION method returns a string
            describing the game.
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_DESCRIPTION)
    counter = 0
    while counter < MAX_QUESTIONS:
        question, correct_answer = game.task()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
            Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if counter == MAX_QUESTIONS:
        print(f'Congratulations, {name}!')
