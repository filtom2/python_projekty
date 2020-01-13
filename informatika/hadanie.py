from random import *
from time import sleep

n = randint(0,100)
guess = int(input('Hadaj cislo od 0 do 100: '))

while n != guess:
    if n < guess:
        guess = int(input('Hadaj menej: '))
    elif n > guess:
        guess = int(input('Hadaj viac: '))
print('Uhadol si cislo.')