tries = 0

while tries != 6:
    tries = int(input('Guess a number from 2 to 12: '))
    if tries < 2 or tries > 12:
        print('Not the range')

print('You got it!')