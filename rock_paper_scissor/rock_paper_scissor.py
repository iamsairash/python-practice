import random

emojis = {
    "r": "🪨",
    "p": "📃",
    "s": "✂️",
}
choices = ("r", "p", "s")

def get_user_input():
    while True:
        user_input = input("Rock, Paper, Scissor? (r/p/s): ")
        if user_input in choices:
            return user_input
        print("invalid input")
        continue
    
def print_detail(user_input, computer):
    print(f"you chose {emojis[user_input]}")
    print(f"computer chose {emojis[computer]}")

def result(user_input,computer):
    if(user_input==computer):
        print("Draw")
    elif((user_input=='s' and computer=='p') or
       (user_input=='p' and computer=='r') or
       (user_input=='r' and computer=='s')):
        print("you won! 🚀")
    else:
        print("you lose!")
    

def playgame():
    while True:
        user_input=get_user_input()
        
        computer = random.choice(choices)
        
        print_detail(user_input, computer)
        
        result(user_input, computer)
        
        want_continue = input("press any key to continue, and 'n' to terminate the game. ")
        if(want_continue=='n'):
            break
        

playgame()