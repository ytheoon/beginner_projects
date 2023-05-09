import  random, re, sys

def get_number():
    return random.randint(1,100)

def get_user_input():
    flag = True
    user_input = None
    while flag:
        user_input = input("Guess a number between 1 and 100: ")
        match_val = re.match("[-+]?\\d+$", user_input)

        if match_val is None:
            print("Please enter an integer:")
        elif int(user_input)<1 or int(user_input)>100:
            print("Number should be between 1 and 100")
        else:
            flag = False
    return int(user_input)

def check_answer(guess, answer):
    if guess < answer:
        print("\nGuess a higher number")
        return False
    elif guess > answer:
        print("\nGuess a lower number")
        return False
    else:
        print("You Won!!!")
        return True        

answer = get_number()
answer_found = False
while not answer_found:
    guess = get_user_input()
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    answer_found = check_answer(guess, answer)

sys.exit()