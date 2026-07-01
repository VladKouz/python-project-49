import random

import prompt


def main():

    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_counter = 0
    while right_counter < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        right_answer = 'yes' if random_number % 2 == 0 else 'no'
        if user_answer == right_answer:
            print('Correct!')
            right_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")

    print(f'Congratulations, {user_name}')


if __name__ == "__main__":
    main()