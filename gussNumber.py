# lets make a guess number game:
from random import randint
randomNumber = randint(1, 9)
guessNumber = int(input('Guess number: '))
if randomNumber == guessNumber:
    print('Hurreh! You won')
else:
    print('The random number was', randomNumber)
