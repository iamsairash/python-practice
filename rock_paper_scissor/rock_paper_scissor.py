import random

ROCK = 'r',
SCISSOR = 's',
PAPER = 'p'

emojis = {
    ROCK: "🪨",
    PAPER: "📃",
    SCISSOR: "✂️",
}
choices = tuple(emojis.keys())
print(choices)

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
    elif((user_input==SCISSOR and computer==PAPER) or
       (user_input==PAPER and computer==ROCK) or
       (user_input==ROCK and computer==SCISSOR)):
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