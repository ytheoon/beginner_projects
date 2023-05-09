import  random, re

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

