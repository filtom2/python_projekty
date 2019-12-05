#hrac musi zistit cislo ktore pocitac vygeneruje od 0 - 100 a potom hrac hlada a pocitac mu radi viac/menej
from random import randint
n = randint(0,100)
hadanie = int(input('Hadajte nahodne cislo od 0-100: \n'))
while n != 'guess':         #TODO pridanie hori prihorieva atp.
    if hadanie > n:
        hadanie = int(input('Menej, hadaj dalej \n'))
    elif hadanie < n:
        hadanie = int(input('Viacej, hadaj dalej \n'))
    elif hadanie == n:
        print('Uhadol si cislo.')
        break
