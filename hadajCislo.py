#hrac musi zistit cislo ktore pocitac vygeneruje od 0 - 100 a potom hrac hlada a pocitac mu radi viac/menej
from random import randint                #importuje sa kniznica ktora obsahuje iba prikaz randint aby sa setrila pamat kedze ostatne programy sa nevyuziju
n = randint(0,100)              #vygeneruje nadhodne cislo od 0 do 100
hadanie = int(input('Hadajte nahodne cislo od 0-100: \n'))             #uzivatelov vstup kde hada cislo
while n != 'guess':         #TODO pridanie hori prihorieva atp.   #program je v loope pretoze sa musi hadat stale a musi to byt v cykle az pokial sa cislo neuhadne
    if hadanie > n: 
        hadanie = int(input('Menej, hadaj dalej \n'))
    elif hadanie < n:
        hadanie = int(input('Viacej, hadaj dalej \n'))
    elif hadanie == n:
        print('Uhadol si cislo.')
        break                            #Ukonci while cyklus
