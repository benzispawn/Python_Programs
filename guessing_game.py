import random

number = input('Choose a number between 1 and 9: ')
ran = random.randrange(1,9)
count = 0

if number > 0 and number <10:
    while number != ran:
        print(ran)
        number = input('You miss! Try again, choose again another number: ')
        ran = random.randrange(1,9)
        count += 1

    print('You have got it! You guess the right number!')
    print('Number of tries: %s' % count)
else:
    print('You have type numbers between 1 and 9!!!')
