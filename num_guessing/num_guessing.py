import random

num = random.randint(1,100)
print("you can print 'end' to terminate")

while True:
    try:
        guessed_num=input("Guess a number between 1 and 100: ")
        if(guessed_num.lower()=='end'):
            print("Game terminated. ")
            break
        
        guessed_num = int(guessed_num)
        if(guessed_num==num):
            print("Congratulation!!🚀🚀🚀🚀 you won")
            break
        elif(guessed_num>num):
            print("too high!")
        elif(guessed_num<num):
            print("too low")
    except ValueError:
        print("Invalid input. guess between 1 and 100 OR 'end' to terminate the game.")