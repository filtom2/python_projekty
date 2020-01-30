from random import *
from time import sleep

koniec = 'a'
while koniec != 'n' and koniec != 'N':
    doKolko = int(input('Do kolko chcete hrat ?: '))
    n = randint(0,doKolko)
    guess = int(input('Hadaj cislo: '))
    pokusy = 1

    while n != guess:
        if n < guess:
            guess = int(input('Hadaj menej: '))
            pokusy += 1
        elif n > guess:
            guess = int(input('Hadaj viac: '))
            pokusy += 1     
    print('Uhadol si cislo.Travalo ti to',pokusy,'pokusov.')
    koniec = input('Prajete si hrat dalej ? a/n : ')

    ##TODO ked skonci tak ked sa chce hrat znova a/n
print('Zbohom.')