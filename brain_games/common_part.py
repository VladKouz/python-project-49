import prompt


CORRECT_TO_WIN = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


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


