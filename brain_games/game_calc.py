#
#  Реализация игры Калькулятор
#  Суть игры в следующем: пользователю показывается случайное выражение, 
#  например, 35 + 16, которое нужно вычислить и записать правильный ответ.
#
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


def game():

    welcome()

    user_name = get_user_name()

    print('What is the result of the expression?')

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:

        random_number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_sign = random.choice(["+", "-", "*"])
        match random_sign:
            case "+":
                right_answer = random_number1 + random_number2
            case "-":
                right_answer = random_number1 - random_number2
            case "*":
                right_answer = random_number1 * random_number2

        if is_answer_is_right(
            user_name, 
            f'{random_number1} {random_sign} {random_number2}', 
            f'{right_answer}'
            ):
            right_counter += 1
        else:
            loose_message(user_name)   
            break
        if right_counter == CORRECT_TO_WIN:
            win_message(user_name)
