#!C:\Users\a2219\AppData\Local\Programs\Python\Python35-32\ python

import random
import time


card_list = []
dice_value_list = ['9', '10', 'J', 'Q', 'K', 'A']
hand_list = ['High card', 'One pair',
             'Two pair', 'Three of a kind',
             'Straight', 'Full house',
             'Four of a kind', 'Five of a kind']


def game_play():
    player_num = number_of_player()
    rolling()
    player_hands = first_roll(player_num)
    print_all_hand(player_hands, 1)
    player_hands = last_two_rolls(player_hands)
    print_hand_value(player_hands)
    compare_player_list(player_hands)
    print('')


def game():
    print('')
    print('Welcome to Poker Dice game.')
    print('You have two chances to re-roll the dices you pick.')
    print('The player who has the greatest value of combination wins.\n')
    game_play()
    while True:
        try:
            answer = input('Do you want to play again? (Y/N)')
            print('')
            if answer not in ('Y', 'y', 'Yes', 'yes', 'N', 'n', 'No', 'n'):
                print('Wrong input.')
                print('Please enter again.')
            elif answer in ('N', 'n', 'No', 'no'):
                print('Thank you for your playing!\n')
                break
            else:
                game_play()
        except ValueError:
            print('Wrong input.')
            print('Please enter again.')


def rolling():
    print('Rolling dices...', end='', flush=True)
    time.sleep(1)
    print('...', end='', flush=True)
    time.sleep(1)
    print('...')
    time.sleep(0.5)
    print('')


def last_two_rolls(player_hands):
    for iterator in range(2):
        player_hands = re_roll(player_hands, iterator + 2)
        print_all_hand(player_hands, iterator + 2)
    return player_hands


def number_of_player():
    while True:
        try:
            number = int(input('How many people are playing? (2-5): '))
            if number in (2, 3, 4, 5):
                print('')
                break
            else:
                print('Wrong input.')
                print('Please try again.')
        except ValueError:
            print('Wrong input.')
            print('Please try again.')
    return number


def first_roll(player_num):
    global dice_value_list
    global card_list
    card_list = []
    for iterator1 in range(player_num):
        one_card_list=[]
        for iterator2 in range(5):
            one_card_list.append(dice_value_list[random.randrange(6)])
        card_list.append(one_card_list)
    return card_list


def re_roll(card_list, roll_index):
    global dice_value_list
    roll_switch = True
    for iterator in range(len(card_list)):
        print('=============================================')
        print('Roll', roll_index, '\n')
        roll_list = []
        print_one_hand(card_list, iterator + 1)
        print('Player ' + str(iterator + 1) + ', enter the index of dices you want to re-roll. (1-5)')
        print('Enter \'-1\' when you are done.')
        while True:
            try:
                roll_number = int(input('Enter one number at a time (1-5, enter -1 to exist): '))
                if roll_number in (1, 2, 3, 4, 5) and roll_number not in roll_list:
                    roll_list.append(roll_number)
                    card_list[iterator][roll_number - 1] = dice_value_list[random.randrange(6)]
                elif roll_number in roll_list:
                    print('The dice has been selected.')
                    print('Please enter another number.')
                elif roll_number == -1:
                    if len(roll_list) > 0:
                        roll_switch = False
                    break
                else:
                    print('Wrong input.')
                    print('Please try again.')
            except ValueError:
                print('Wrong input.')
                print('Please try again.')
        print('')
    print('=============================================')
    print('=============================================')
    if not roll_switch:
        rolling()
    return card_list


def print_one_hand(card_list, player_number):
    print('Player' + str(player_number) + ': ', end='')
    for iterator in range(len(card_list[player_number-1])):
        print('[' + card_list[player_number-1][iterator] + '] ', end='')
    print('')


def print_all_hand(card_list, round_number):
    print('Round', round_number, '\n')
    for iterator in range(len(card_list)):
        print_one_hand(card_list, iterator + 1)
    print('')


def determine_hand(one_hand):
    global dice_value_list
    global hand_list
    count_list = []
    for iteration in range(len(dice_value_list)):
        count_list.append(one_hand.count(dice_value_list[iteration]))
    if 5 in count_list:
        return [7, count_list]
    elif 4 in count_list:
        return [6, count_list]
    elif 3 in count_list:
        if 2 in count_list:
            return [5, count_list]
        else:
            return [3, count_list]
    elif 2 in count_list:
        if count_list.count(2) == 2:
            return [2, count_list]
        else:
            return [1, count_list]
    elif count_list[0] == 0 or count_list[5] == 0:
        return [4, count_list]
    else:
        return [0, count_list]


def print_hand_value(card_list):
    global hand_list
    for iterator in range(len(card_list)):
        value_list = determine_hand(card_list[iterator])
        print('Player', iterator + 1, 'has', hand_list[value_list[0]] + '.')
    print('')


def compare_player_list(card_list):
    greatest_hand = card_list[0]
    for iterator in range(len(card_list) - 1):
        greatest_hand = compare_hands(greatest_hand, card_list[iterator + 1])
    greatest_index = card_list.index(greatest_hand)
    print('Player', greatest_index + 1, 'has the greatest hand of cards.')
    print('Player', greatest_index + 1, 'wins!')


def compare_hands(hand_one, hand_two):
    hand_one_value = determine_hand(hand_one)
    hand_two_value = determine_hand(hand_two)
    if hand_one_value[0] > hand_two_value[0]:
        return hand_one
    elif hand_one_value[0] < hand_two_value[0]:
        return hand_two
    else:
        if hand_one_value[0] == 7:
            if hand_one_value[1].index(5) > hand_two_value[1].index(5):
                return hand_one
            elif hand_one_value[1].index(5) < hand_two_value[1].index(5):
                return hand_two
            else:
                return -1
        elif hand_one_value[0] == 6:
            if hand_one_value[1].index(4) > hand_two_value[1].index(4):
                return hand_one
            elif hand_one_value[1].index(4) < hand_two_value[1].index(4):
                return hand_two
            else:
                if hand_one_value[1].index(1) > hand_two_value[1].index(1):
                    return hand_one
                elif hand_one_value[1].index(1) < hand_two_value[1].index(1):
                    return hand_two
                else:
                    return -1
        elif hand_one_value[0] == 5:
            if hand_one_value[1].index(3) > hand_two_value[1].index(3):
                return hand_one
            elif hand_one_value[1].index(3) < hand_two_value[1].index(3):
                return hand_two
            else:
                if hand_one_value[1].index(2) > hand_two_value[1].index(2):
                    return hand_one
                elif hand_one_value[1].index(2) < hand_two_value[1].index(2):
                    return hand_two
                else:
                    return -1
        elif hand_one_value[0] == 4:
            if hand_one_value[1][5] > hand_two_value[1][5]:
                return hand_one
            elif hand_one_value[1][5] < hand_two_value[1][5]:
                return hand_two
            else:
                return -1
        elif hand_one_value[0] == 3:
            if hand_one_value[1].index(3) > hand_two_value[1].index(3):
                return hand_one
            elif hand_one_value[1].index(3) < hand_two_value[1].index(3):
                return hand_two
            else:
                temp_one_count_list = hand_one_value[1]
                temp_two_count_list = hand_two_value[1]
                temp_one_count_list.reverse()
                temp_two_count_list.reverse()
                if temp_one_count_list.index(1) < temp_two_count_list.index(1):
                    return hand_one
                elif temp_one_count_list.index(1) > temp_two_count_list.index(1):
                    return hand_two
                else:
                    if hand_one_value[1].index(1) > hand_two_value[1].index(1):
                        return hand_one
                    elif hand_one_value[1].index(1) < hand_two_value[1].index(1):
                        return hand_two
                    else:
                        return -1
        elif hand_one_value[0] == 2:
            temp_one_count_list = hand_one_value[1]
            temp_two_count_list = hand_two_value[1]
            temp_one_count_list.reverse()
            temp_two_count_list.reverse()
            if temp_one_count_list.index(2) < temp_two_count_list.index(2):
                return hand_one
            elif temp_one_count_list.index(2) > temp_two_count_list.index(2):
                return hand_two
            else:
                if hand_one_value[1].index(2) > hand_two_value[1].index(2):
                    return hand_one
                elif hand_one_value[1].index(2) < hand_two_value[1].index(2):
                    return hand_two
                else:
                    if hand_one_value[1].index(1) > hand_two_value[1].index(1):
                        return hand_one
                    elif hand_one_value[1].index(1) < hand_two_value[1].index(1):
                        return hand_two
                    else:
                        return -1
        elif hand_one_value[0] == 1:
            if hand_one_value[1].index(2) > hand_two_value[1].index(2):
                return hand_one
            elif hand_one_value[1].index(2) < hand_two_value[1].index(2):
                return hand_two
            else:
                temp_one_count_list = hand_one_value[1]
                temp_two_count_list = hand_two_value[1]
                temp_one_count_list.reverse()
                temp_two_count_list.reverse()
                if temp_one_count_list.index(1) < temp_two_count_list.index(1):
                    print('Hand one')
                    return hand_one
                elif temp_one_count_list.index(1) > temp_two_count_list.index(1):
                    return hand_two
                else:
                    temp_one_count_list.remove(1)
                    temp_two_count_list.remove(1)
                    if temp_one_count_list.index(1) < temp_two_count_list.index(1):
                        return hand_one
                    elif temp_one_count_list.index(1) > temp_two_count_list.index(1):
                        return hand_two
                    else:
                        temp_one_count_list.remove(1)
                        temp_two_count_list.remove(1)
                        if temp_one_count_list.index(1) < temp_two_count_list.index(1):
                            return hand_one
                        elif temp_one_count_list.index(1) > temp_two_count_list.index(1):
                            return hand_two
                        else:
                            return -1
        elif hand_one_value[0] == 0:
            if hand_one_value[1].index(0) < hand_two_value[1].index(0):
                return hand_one
            elif hand_one_value[1].index(0) > hand_two_value[1].index(0):
                return hand_two
            else:
                return -1

if __name__ == '__main__':
    game()
