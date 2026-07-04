#
#  Реализация игры Простое число
#  Суть игры в следующем: пользователю показывается число. 
#  Пользователь должен определить простое число или нет.
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

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simple(number):
    if number < 2:
        return 'no'
    temp = 2
    simple = 'yes'
    while temp < number:
        if number % temp == 0:
            simple = 'no'
            break
        temp += 1
    return simple


# Старая версия - работает на импортированных функциях из общего модуля
def oldgame():

    welcome()

    user_name = get_user_name()

    print(QUESTION)

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


# Новая версия - формируется список вопрос-ответ и общая функция-сценарий
def game():

    questions_answers = []
    for i in range(CORRECT_TO_WIN):

        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = is_simple(random_number)
        questions_answers.append([f'{random_number}', f'{right_answer}'])
    common_game(QUESTION, questions_answers)