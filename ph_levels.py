ph = int(input('What is the pH (0-14): '))
if ph > 7:
    print('Basic')
elif ph < 7:
    print('Acidic')    
else:
    print('Neutral')    