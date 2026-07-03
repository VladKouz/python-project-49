#
#  Реализация игры НОД
#  Суть игры в следующем: пользователю показывается два случайных числа. 
#  Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.
#
import random

from .common_part import (
    CORRECT_TO_WIN,
    MAX_NUMBER,
    MIN_NUMBER,
    common_game,
    get_user_name,
    is_answer_is_right,
    loose_message,
    welcome,
    win_message,
)

QUESTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):

    a = abs(a) 
    b = abs(b)
    while b != 0:
        temp = b 
        b = a % b 
        a = temp
    return a


# Старая версия - работает на импортированных функциях из общего модуля
def oldgame():

    welcome()

    user_name = get_user_name()

    print(QUESTION)

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:

        random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = gcd(random_number1, random_number2)
        if is_answer_is_right(user_name, f'{random_number1} {random_number2}', 
                              f'{right_answer}'):
            right_counter += 1
        else:
            loose_message(user_name)   
            break
        if right_counter == CORRECT_TO_WIN:
            win_message(user_name)


# Новая версия - формируется список вопрос-ответ и общая функция-сценарий
def game():

    questions_answers = []
    for i in range(CORRECT_TO_WIN):

        random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = gcd(random_number1, random_number2)
        questions_answers.append(
            [f'{random_number1} {random_number2}', f'{right_answer}']
            )
    common_game(QUESTION, questions_answers)