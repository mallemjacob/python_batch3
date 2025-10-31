import sys, random

print("ROCK, PAPER, SCISSORS")
wins = 0
losses = 0
ties = 0

def userFunc(user_input):
    #user input
    if user_input == 'q':
        if wins > 0 or losses > 0 or ties > 0:
            print('I hope you enjoyed the game!')
        else:
            print('Atleast try once!')
        sys.exit()
    elif user_input == 'r' or user_input == 'p' or user_input == 's':
        userValues(user_input)
        return user_input
    else:
        print('Choose between r,p,s and q.')
        

def userValues(u):
    if u == 'r':
        print('ROCK verses...')
    elif u == 'p':
        print('PAPER verses...')
    elif u == 's':
        print('SCISSORS verses...')


def comFunc():
    #computer input
    ranint = random.randint(1,3) #1,2,3
    if ranint == 1:
        computer_input = 'r'
        print('ROCK')
    elif ranint == 2:
        computer_input = 'p'
        print('SCISSORS')
    elif ranint == 3:
        computer_input = 's'
        print('SCISSORS')
    return computer_input

def gameLogic(user_input, computer_input):
    global wins, losses, ties
    if user_input == 'r' and computer_input == 'p':
        print('You lose!')
        losses = losses + 1
    if user_input == 'r' and computer_input == 's':
        print('You win!')
        wins = wins + 1
    if user_input == 'p' and computer_input == 'r':
        print('You win!')
        wins = wins + 1
    if user_input == 'p' and computer_input == 's':
        print('You lose!')
        losses = losses + 1
    if user_input == 's' and computer_input == 'r':
        print('You lose!')
        losses = losses + 1
    if user_input == 's' and computer_input == 'p':
        print('You win!')
        wins = wins + 1
    if user_input == computer_input:
        print("It's a tie!")
        ties = ties + 1

while True:
    print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) +  " Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_input = input()    
    gameLogic(userFunc(user_input), comFunc())
        

