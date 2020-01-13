from random import *
from time import sleep
pokusy = 1

n = randint(0,100)
guess = int(input('Hadaj cislo od 0 do 100: '))

while n != guess:
    if n < guess:
        guess = int(input('Hadaj menej: '))
        pokusy += 1
    elif n > guess:
        guess = int(input('Hadaj viac: '))
        pokusy += 1
print('Uhadol si cislo.Travalo ti to',pokusy,'pokusov.')