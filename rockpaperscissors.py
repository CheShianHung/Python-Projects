#!C:\Users\a2219\AppData\Local\Programs\Python\Python35-32\ python
import random
import time

menu = (
        """\
Let\'s make a move:
Rock: 1
Paper: 2
Scissors: 3

        """)

error = 'Wrong input. Please try again.\n'

moveList = ['Rock', 'Paper', 'Scissors']

score = [0, 0]


def game():
    print('Welcome to Rock Paper Scissors Game.\n\n')
    print(menu)

    result = False
    next_game = True

    while next_game:
        while not result:

            move = move_verify()
            processing()
            result = outcome(move)

        next_game = next_game_question()
        result = False

    score_result()
    print('Thank you for playing.')
    print('Game finished.')


def move_verify():
    input_move = input('Make a move: ')
    while input_move not in ('1', '2', '3'):
        print(error)
        print(menu)
        input_move = input('Make a move: ')
    return input_move


def processing():
    print('Rock...\n')
    time.sleep(1)
    print('Paper...\n')
    time.sleep(1)
    print('Scissors!!!\n')
    time.sleep(0.5)


def outcome(my_move):
    robot_move = random.randrange(1, 4, 1)
    print('You threw ' + moveList[int(my_move) - 1] + '.')
    print('Computer threw ' + moveList[robot_move - 1] + '.\n')
    return compare(my_move, robot_move)


def compare(my_move, computer_move):

    if my_move == '1':
        if computer_move == 1:
            return tie()
        elif computer_move == 2:
            return lose()
        else:
            return win()

    elif my_move == '2':
        if computer_move == 1:
            return win()
        elif computer_move == 2:
            return tie()
        else:
            return lose()

    else:
        if computer_move == 1:
            return lose()
        elif computer_move == 2:
            return win()
        else:
            return tie()


def tie():
    print("It's a tie! Let's try again!\n")
    return False


def win():
    print("You win! Good job!\n")
    global score
    score[0] += 1
    return True


def lose():
    print("Computer Wins! You lose!\n")
    global score
    score[1] += 1
    return True


def next_game_question():
    while True:
        next_game_answer = input('Do you want to play again?(y/n): ')
        if next_game_answer in ('y', 'Y', 'Yes', 'yes'):
            return True
        elif next_game_answer in ('n', 'N', 'No', 'no'):
            return False
        else:
            print(error)


def score_result():
    print('Scores:')
    print('You: ' + str(score[0]))
    print('Computer: ' + str(score[1]) + '\n')


if __name__ == '__main__':
    game()




