#
#  Тестовое задание, в ппроекте не используется
#
import prompt


def get_user_name():

    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name