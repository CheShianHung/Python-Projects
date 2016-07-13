#!C:\Users\a2219\AppData\Local\Programs\Python\Python35-32\ python

import random


def game():
    again = True
    game_number = 1
    question_list = ['rhythm', 'buzz', 'sometimes', 'jazz music', 'euphemism', 'scared','university', 'ellen', 'grandmother', 'january', 'independent day']
    introduction()
    while again:
        input_list = []
        miss_time = [0]
        answer = random_question(question_list)
        question_list.remove(answer)
        current_list = create_list(answer)
        finish = False
        while not finish:
            menu(current_list, miss_time, game_number)
            user_guess = input('Guess a letter: ')
            while not input_check(input_list, user_guess) :
                user_guess = input('Guess a letter: ')
            input_list.append(user_guess)
            current_list = guess(user_guess, answer, current_list, miss_time)
            finish = check_finish(current_list, miss_time, answer, game_number)
        if len(question_list) != 0:
            again = play_again_question()
            game_number += 1
        else:
            print('There are no more questions.\n')
            again = False
    print('Game finished.')


def introduction():
    print('\nWelcome to Hangman Game.')
    print('Guess the letters in the word. You have six chances to have the wrong guess.')
    input('Press Enter to start the game.')


def play_again_question():
    answer = input('Do you want to play again?(Y/N): ')
    while answer not in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'no'):
        print('Wrong input')
        answer = input('Do you want to play again?(Y/N): ')
    if answer in ('Y', 'y', 'Yes', 'yes'):
        return True
    else:
        print('Thank you for your playing!\n')
        return False


def menu(current_list, graph_counter, game_number):
    print('====================================')
    print('Game ' + str(game_number) + '\n')
    print_graph(graph_counter[0])
    print_list(current_list)
    print()


def random_question(question_list):
    random_number = random.randrange(0, len(question_list), 1)
    question = question_list[random_number]
    return question


def guess(user_guess, answer, current_guess, graph_counter):
    if user_guess not in answer:
        graph_counter[0] += 1
        print('There is no \'' + user_guess + '\' in this word.\n')
        return current_guess
    else:
        for iterator in range(len(answer)):
            if user_guess == answer[iterator]:
                if iterator == 0:
                    current_guess[iterator] = user_guess.upper()
                else:
                    current_guess[iterator] = user_guess
        return current_guess


def print_final_answer(answer):
    print(answer[0].upper(), end='')
    for iterator in range(len(answer)-1):
        print(answer[iterator + 1], end='')


def print_list(list_printed):
    print('    ', end='')
    for iterator in range(len(list_printed)):
        print(list_printed[iterator] + '  ', end='')
    print()


def create_list(answer):
    empty_list = []
    for iterator in range(len(answer)):
        if answer[iterator] == ' ':
            empty_list.append(' ')
        else:
            empty_list.append('_')
    return empty_list


def input_list_check(input_list, user_guess):
    repeat_guess = False
    iterator = 0
    if len(input_list) != 0:
        while not repeat_guess and iterator < len(input_list):
            if user_guess == input_list[iterator]:
                repeat_guess = True
            else:
                iterator += 1
    return repeat_guess


def check_finish(current_list, miss_time, answer, game_number):
    finish_switch = True
    iterator=0
    if miss_time[0] == 6:
        menu(current_list, miss_time, game_number)
        print('You are dead.\n')
        print('The word is actually \'', end='')
        print_final_answer(answer)
        print('\'.\n')
    else:
        while finish_switch and iterator < len(current_list):
            if current_list[iterator] == '_':
                finish_switch = False
            else:
                iterator += 1
        if finish_switch:
            menu(current_list, miss_time, game_number)
            print('Congratulations! You solved the word!\n')
    return finish_switch


def input_check(input_list, user_guess):
    if user_guess.isalpha():
        if len(user_guess) == 1:
            if input_list_check(input_list, user_guess):
                print('Repeated guess.\n')
                return False
            else:
                return True
        else:
            print('Too many letters.\n')
            return False
    else:
        print('Wong input.\n')
        return False


def print_graph(miss_num):
    graphic = [
"""\
    +------+
    |
    |
    |
    |
    |
==================
  ||          ||
  ||          ||
"""
,
"""\
    +------+
    |      |
    |      O
    |
    |
    |
==================
  ||          ||
  ||          ||
"""
,
"""\
    +------+
    |      |
    |      O
    |      |
    |
    |
==================
  ||          ||
  ||          ||
"""
,
"""\
    +------+
    |      |
    |      O
    |     /|
    |
    |
==================
  ||          ||
  ||          ||
"""
,
"""\
    +------+
    |      |
    |      O
    |     /|\\
    |
    |
==================
  ||          ||
  ||          ||
"""
,
"""\
    +------+
    |      |
    |      O
    |     /|\\
    |     /
    |
==================
  ||          ||
  ||          ||
"""
,
"""\
    +------+
    |      |
    |      O
    |     /|\\
    |     / \\
    |
==================
  ||          ||
  ||          ||
"""
    ]
    print(graphic[miss_num])


if __name__ == '__main__':
    game()
