
import random

gameloopbool = True
while gameloopbool:
    Flag = True
    while Flag:
        num = input('Type a number for an upper bound:')
        num2 = input('Type a number for a lower bound:')
        triesnum = input('Input number of tries')
        isnumfinished = False
        isnum2finished = False
        istriesnumfinished = False

        if num.isdigit():
            print('')
            num = int(num)
            isnumfinished = True
        else:
            print('Invalid Input Try Again')

        if num2.isdigit():
            print('')
            print('Lets Play!')
            num2 = int(num2)
            isnum2finished = True
        else:
            print('Invalid Input Try Again')

        if triesnum.isdigit():
            print('')
            triesnum = int(triesnum)
            istriesnumfinished = True
        else:
            print('Invalid Input Try Again')

        if isnumfinished and isnum2finished and istriesnumfinished == True:
            Flag = False

    secret = random.randint(num2, num)

    guess = None
    count = 0
    high = False
    high_str = ''
    failed = None
    won = None
    flag2 = True
    shouldplayagainbool = None

    while guess != secret and flag2 == True:
        guess = input('Please Guess a number between 1, and ' + str(num) + ':')
        if guess.isdigit():
            guess = int(guess)

        if guess == secret:
            won = True
            print('Congratulation you guessed right! it took you ' + count + ' tries!')


        if guess > secret:
            high = True
            high_str = 'lower'
        elif guess < secret:
            high = False
            high_str = 'higher'

        if count >= triesnum:
            print('Sorry you did not guess the number in ' + str(triesnum) + ' tries the number was ' + str(
                secret) + ' better luck next time')
            failed = True


        if guess != secret and failed != True and won != True:
            count += 1
            print('')
            print('Incorrect that was guess ' + str(count) + ' you need to guess ' + high_str + ' you have ' + str(
                triesnum - count) + ' guesses left ')

        if failed or won == True:
            shouldplayagain = input('Do you want to play again:')
            if shouldplayagain == 'Yes':
                shouldplayagainbool = True
                print('')
                print('Okay lets play again')
                print('')
                flag2 = False
                Flag = True

            if shouldplayagain == 'No':
                shouldplayagain = False
                print('')
                print('Closing Program')
                gameloopbool = False
                Flag = False
                flag2 = False

            if shouldplayagain != 'Yes' or 'No':
                print('')
                print('Could not identify text, closing program')
                gameloopbool = False
                Flag = False
                flag2 = False








