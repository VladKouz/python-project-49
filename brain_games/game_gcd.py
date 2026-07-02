import random

#from math import a
from .common_part import CORRECT_TO_WIN
from .common_part import welcome, get_user_name, is_answer_is_right, loose_message, win_message

def gcd(a,b):

    a = abs(a) 
    b = abs(b)
    while b != 0:
        temp = b 
        b = a % b 
        a = temp
    return a

def game():

    ##CORRECT_TO_WIN = 3
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    welcome()

    user_name = get_user_name()

    print('Find the greatest common divisor of given numbers.')

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:

        random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)

        right_answer = gcd(random_number1, random_number2)

        if is_answer_is_right(user_name, f'{random_number1} {random_number2}', f'{right_answer}'):
            right_counter += 1
        else:
            loose_message(user_name)   
            break
        if right_counter == 3:
            win_message(user_name)
