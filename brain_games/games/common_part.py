#
#  Общий функционал всех игр
#
import prompt

CORRECT_TO_WIN = 3  # Число раундов, оно же число правильных ответов
MIN_NUMBER = 1     # Минимум всех генераторов случаных чисел
MAX_NUMBER = 100   # Максимум всех генераторов случайных чисел


def welcome():
     
    print("Welcome to the Brain Games!")
     

def get_user_name():

    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def win_message(user):

    print(f'Congratulations, {user}!')


def loose_message(user):
     
    print(f"Let's try again, {user}!")


def is_answer_is_right(user, question, answer):

    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:

        print('Correct!')
        return True
    else:

        print(f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{answer}'.")
        return False


# Функция-сценарий: задает 3 вопроса, сверяет 3 ответа...
def common_game(anwer_format, questions_answers):

    welcome()
    user_name = get_user_name()
    print(anwer_format)
    right_counter = 0
    for question_answer in questions_answers:
        if is_answer_is_right(
            user_name, question_answer[0], question_answer[1]
            ):
            right_counter += 1
        else:
            break
    if right_counter >= CORRECT_TO_WIN:
        win_message(user_name)
    else:
        loose_message(user_name) 

       
