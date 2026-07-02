import random

from .common_part import (
    CORRECT_TO_WIN,
    MAX_NUMBER,
    MIN_NUMBER,
    get_user_name,
    is_answer_is_right,
    loose_message,
    welcome,
    win_message,
)


def is_simple(number):
    temp = 2
    simple = 'yes'
    while temp < number // temp:
        if number % temp == 0:
            simple = 'no'
            break
        temp += 1
    return simple


def game():

    welcome()

    user_name = get_user_name()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:

        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = is_simple(random_number)
        if is_answer_is_right(user_name, f'{random_number}', 
                              f'{right_answer}'):
            right_counter += 1
        else:
            loose_message(user_name)   
            break
        if right_counter == CORRECT_TO_WIN:
            win_message(user_name)
