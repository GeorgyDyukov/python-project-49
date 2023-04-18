import prompt


def welcome_user():
    '''
    A function that greets the user.
    '''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine():
    '''
    A function that manages the game loop of questions.
    '''
    counter = 0
    while counter < 3:
        flag = complete_game_lap()
        if flag == True:
            counter += 1
        else:
            break
    if counter == 3:
        print(f'Congratulations, {name}!')