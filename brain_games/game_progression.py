#
#  Реализация игры Арифметическая прогрессия
#  Показываем игроку ряд чисел, который образует арифметическую прогрессию, 
#  заменив любое из чисел двумя точками. Игрок должен определить это число.
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

PROGRESSION_LENGTH = 10
QUESTION = 'What number is missing in the progression?'


def progression(start, increment, count=PROGRESSION_LENGTH):

    return [start + increment * i for i in range(count)]


# Старая версия - работает на импортированных функциях из общего модуля
def oldgame():

    welcome()

    user_name = get_user_name()

    print(QUESTION)

    right_counter = 0
    while right_counter < CORRECT_TO_WIN:

        random_number = random.randint(0, PROGRESSION_LENGTH - 1)
        random_progression = progression(
            random.randint(MIN_NUMBER, MAX_NUMBER),
            random.randint(MIN_NUMBER, MAX_NUMBER)
        )
        right_answer = random_progression[random_number]
        match random_number:
            case 0: 
                question = '.. ' + ' '.join(
                    map(str, random_progression[random_number + 1:])
                    )
            case 9: 
                question = ' '.join(
                    map(str, random_progression[:random_number])
                    ) + ' ..'
            case _: 
                question = \
                ' '.join(
                    map(str, random_progression[:random_number])
                    ) + ' .. ' + \
                ' '.join(
                    map(str, random_progression[random_number + 1:])
                    )
        if is_answer_is_right(user_name, question, 
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

        random_number = random.randint(0, PROGRESSION_LENGTH - 1)
        random_progression = progression(
            random.randint(MIN_NUMBER, MAX_NUMBER),
            random.randint(MIN_NUMBER, MAX_NUMBER)
        )
        right_answer = random_progression[random_number]
        match random_number:
            case 0: 
                question = '.. ' + ' '.join(
                    map(str, random_progression[random_number + 1:])
                    )
            case 9: 
                question = ' '.join(
                    map(str, random_progression[:random_number])
                    ) + ' ..'
            case _: 
                question = \
                ' '.join(
                    map(str, random_progression[:random_number])
                    ) + ' .. ' + \
                ' '.join(
                    map(str, random_progression[random_number + 1:])
                    )
        questions_answers.append(
            [question, f'{right_answer}']
            )
    common_game(QUESTION, questions_answers)