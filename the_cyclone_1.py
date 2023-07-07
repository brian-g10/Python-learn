# The Cyclon_1

height = int(input('What is your height? '))
credit = int(input('How many credits do you have? '))
with_taller_person = True

if credit < 10:
    print('You don\'t have enough credits to ride')
elif height >= 137 and credit >= 10:
    print('Enjoy the ride!')
elif height < 137:
    if height < 100 or not with_taller_person:
        print('You are not tall enough to ride')
    elif height > 100 and with_taller_person:
        print('Enjoy the ride, folks!')
else:
    print('Invalid data')

    # doesn't work properly_ 11with taller person11