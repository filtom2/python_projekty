#Milan Seliga II.F skusanieZiakov
# vypyta kolko prikladov chce ratat potom s akymi operaciami
#a aku obtiaznost a na konci je output kolko mal spravne
from random import *
import time
#/////////////////////#




start = True
while start == True:
    start_time = time.time()
    print('==================')

    print('Vitajte v programe.')
    print()
    print('Zvolte si operaciu: \n 1.Scitanie\n 2.Odcit1anie\n 3.Nasobenie\n 4.Delenie\n')
    print('==================')

    operacia = int(input('Vyber si cislom operaciu: '))
    pocetPrikladov = int(input('Kolko prikladov chcete ?: '))
    pocetPrikladovNemenne = pocetPrikladov

    def koniecInfo():

        time.sleep(0.3)
        print('==================')
        time.sleep(0.2)
        print(' ================')
        time.sleep(0.1)
        print('  ===============')
        print('\n   ', spravne, '/', pocetPrikladovNemenne, '\n   ',
              spravne / pocetPrikladovNemenne * 100, '%\n')
        print('Z', pocetPrikladovNemenne, 'ste mali dobre:', spravne,
              'priklady a zle:', zle, 'priklad/dov.\n')
        print('Trvalo vam to,',round(time.time()- start_time,1),'sekund.\n')
        time.sleep(0.1)
        print('  ==============')
        time.sleep(0.1)
        print(' ================')
        time.sleep(0.2)
        print('==================')

    if operacia == 1:
        print('Vybrali ste si scitanie.')
    
        spravne = 0
        zle = 0
        pocet = 0

        while pocetPrikladov != 0:
            a = randint(0, 10)
            b = randint(0, 10)
            pocetPrikladov -= 1
            print(a, '+', b)
            vysledok = int(input('= '))
            if vysledok == a + b:
                spravne += 1
                pocet += 1
                continue
            else:
                while a + b != vysledok:
                    print('Zle skus este raz: \n')
                    print(a, '+', b)
                    vysledok = int(input('= '))

                zle += 1
                pocet += 1
                continue

        koniecInfo()

    elif operacia == 2:
        print('Vybrali ste si odcitanie.')
        odcitanieAjZaporne = input('Prajete si aj zaporne cisla ? a/n  ')
        if odcitanieAjZaporne == 'a':

            spravne = 0
            zle = 0
            pocet = 0

            while pocetPrikladov != 0:
                a = randint(0, 10)
                b = randint(0, 10)
                pocetPrikladov -= 1
                print(a, '-', b)
                vysledok = int(input('= '))
                if vysledok == a - b:
                    spravne += 1
                    pocet += 1
                    continue
                else:
                    while a - b != vysledok:
                        print('Zle skus este raz: \n')
                        print(a, '-', b)
                        vysledok = int(input('= '))

                    zle += 1
                    pocet += 1
                    continue
            koniecInfo()

        elif odcitanieAjZaporne == 'n':

            spravne = 0
            zle = 0
            pocet = 0

            while pocetPrikladov != 0:
                a = randint(0, 10)
                b = randint(0, 10)
                while not a > b:
                    b = randint(0, 10)

                pocetPrikladov -= 1
                print(a, '-', b)
                vysledok = int(input('= '))

                if vysledok == a - b:
                    spravne += 1
                    pocet += 1
                    continue
                else:
                    while a - b != vysledok:
                        print('Zle skus este raz: \n')
                        print(a, '-', b)
                        vysledok = int(input('= '))

                    zle += 1
                    pocet += 1
                    continue
            koniecInfo()

    elif operacia == 3:
        print('Vybrali ste si nasobenie.')

        spravne = 0
        zle = 0
        pocet = 0

        while pocetPrikladov != 0:
            a = randint(0, 10)
            b = randint(0, 10)
            pocetPrikladov -= 1
            print(a, '*', b)
            vysledok = int(input('= '))
            if vysledok == a * b:
                spravne += 1
                pocet += 1
                continue
            else:
                while a * b != vysledok:
                    print('Zle skus este raz: \n')
                    print(a, '*', b)
                    vysledok = int(input('= '))
                zle += 1
                pocet += 1

                pocetPrikladov -= 1
                print(a, '*', b)
                vysledok = int(input('= '))

                if vysledok == a * b:
                    spravne += 1
                    pocet += 1
                    continue
                else:
                    while a * b != vysledok:
                        print('Zle skus este raz: \n')
                        print(a, '*', b)
                        vysledok = int(input('= '))
                    continue
        koniecInfo()

    elif operacia == 4:
        print('Vybrali ste si delenie.')

        spravne = 0
        zle = 0
        pocet = 0

        while pocetPrikladov != 0:
            a = randint(0, 20)
            b = randint(1, 20)
            while not a % b == 0:
                b = randint(1, 10)

            pocetPrikladov -= 1
            print(a, '/', b)
            vysledok = int(input('= '))
            if a > b:
                if vysledok == a / b:
                    spravne += 1
                    pocet += 1
                    continue
                else: 
                    while a / b != vysledok:
                        print('Zle skus este raz: \n')
                        print(a, '/', b)
                        vysledok = int(input('= '))
                    zle += 1
                    pocet += 1
                    continue
            else:
                continue
        koniecInfo()

    esteRaz = input('Chces hrat znova ?: a/n ')
    if esteRaz == 'a' or esteRaz == 'A':
        continue
    elif esteRaz == 'n' or esteRaz == 'N':
        print('\nDobre zbohom...')
        time.sleep(0.2)
        break
