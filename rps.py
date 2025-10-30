import sys, random

print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

def userFunc(user_input):
    #user input
    if user_input == 'q':
        sys.exit()
    if user_input == 'r' or user_input == 'p' or user_input == 's':
        return user_input
        

def comFunc():
    #computer input
    ranint = random.randint(1,3) #1,2,3
    if ranint == 1:
        computer_input = 'r'
    elif ranint == 2:
        computer_input = 'p'
    elif ranint == 3:
        computer_input = 's'
    return computer_input

def gameLogic(user_input, computer_input):
    global wins, losses, ties
    if user_input == 'r' and computer_input == 'p':
        print('ROCK verses PAPER')
        print('You lose!')
        losses = losses + 1
    if user_input == 'r' and computer_input == 's':
        print('ROCK verses SCISSORS')
        print('You win!')
        wins = wins + 1
    if user_input == 'p' and computer_input == 'r':
        print('PAPER verses ROCK')
        print('You win!')
        wins = wins + 1
    if user_input == 'p' and computer_input == 's':
        print('PAPER verses SCISSORS')
        print('You lose!')
        losses = losses + 1
    if user_input == 's' and computer_input == 'r':
        print('SCISSORS verses ROCK')
        print('You lose!')
        losses = losses + 1
    if user_input == 's' and computer_input == 'p':
        print('SCISSORS verses PAPER')
        print('You win!')
        wins = wins + 1
    if user_input == computer_input:
        print(user_input + ' verses ' + computer_input)
        print("It's a tie!")
        ties = ties + 1

while True:
    print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) +  " Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_input = input()    
    if not gameLogic(userFunc(user_input), comFunc()):
        print('Choose between r,p,s and q.')

