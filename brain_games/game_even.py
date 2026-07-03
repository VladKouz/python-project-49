#
#  Реализация игры Проверка на четность
#  Суть игры в следующем: пользователю показывается случайное число. 
#  И ему нужно ответить yes, если число чётное, или no — если нечётное:
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

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):

    return number % 2 == 0


# Старая версия - работает на импортированных функциях из общего модуля
def oldgame():

    welcome()

    user_name = get_user_name()

    print(QUESTION)

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = 'yes' if is_even(random_number) else 'no'
        if is_answer_is_right(user_name, random_number, right_answer):
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
        right_answer = 'yes' if is_even(random_number) else 'no'
        questions_answers.append(
            [f'{random_number}', f'{right_answer}']
            )
    common_game(QUESTION, questions_answers)