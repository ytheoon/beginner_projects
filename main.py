#!/usr/bin/env python

"""Simple number guessing game. A random number is generated and you need to guess it! :)"""

import random
import re
import sys


def get_number():
    """Generate a random number

    Returns:
        int: random integer
    """
    return random.randint(1, 100)


def get_user_input():
    """record the user's guess

    Returns:
        int: user's guess
    """
    flag = True
    user_input = None
    while flag:
        user_input = input("Guess a number between 1 and 100: ")
        match_val = re.match("[-+]?\\d+$", user_input)

        if match_val is None:
            print("Please enter an integer:")
        elif int(user_input) < 1 or int(user_input) > 100:
            print("Number should be between 1 and 100")
        else:
            flag = False
    return int(user_input)


def check_answer(guess, answer):
    """check whether the guess is correct

    Args:
        guess (int): the users guess
        answer (int): the actual answer

    Returns:
        bool: true if the guess is right
              false if the guess is wrong
    """
    if guess < answer:
        print("\nGuess a higher number")
        return False
    if guess > answer:
        print("\nGuess a lower number")
        return False
    else:
        print("You Won!!!")
        return True


def run_program():
    """start the game"""
    answer = get_number()
    answer_found = False
    while not answer_found:
        guess = get_user_input()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        answer_found = check_answer(guess, answer)
    sys.exit()


run_program()
