import random

'''
1 for snake
-1 for water
0 for gun
'''

# mappings

user_dict={"snake":1,"water":-1,"gun":0}
reverse_dict={1:"snake",-1:"water",0:"gun"}

# winning conditions

winning_cases = [
    (1, -1),   # snake beats water
    (-1, 0),   # water beats gun
    (0, 1)     # gun beats snake
]

def get_computer_choice():
    return random.choice([-1,0,1])

def decide_result(user, computer):
    if user==computer:
        return "tie"
    elif (user, computer) in winning_cases:
        return "win"
    else:
        return "lose"