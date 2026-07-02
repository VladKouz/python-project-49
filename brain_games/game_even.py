import random

#import prompt

from .common_part import CORRECT_TO_WIN
from .common_part import welcome, get_user_name, is_answer_is_right, loose_message, win_message

def is_even(number):

    return number % 2 == 0


def game():

    ##CORRECT_TO_WIN = 3
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    welcome()

    user_name = get_user_name()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = 'yes' if is_even(random_number) else 'no'
        if is_answer_is_right(user_name, random_number, right_answer):
            right_counter += 1
        else:
            loose_message(user_name)   
            break
        if right_counter == 3:
            win_message(user_name)
