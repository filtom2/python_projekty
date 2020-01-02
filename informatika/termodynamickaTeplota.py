#Milan Seliga II.F
#vypocet tabulky

vstup = int(input('Zadajte zaciatocnu cislo: '))
koniec = int(input('Zadajte koncovu teplotu: '))
kroky = int(input('Zadajte po kolko chcete zvacsovat: '))

print('Stupne Celzia:           Kelviny: ')
print('       ----------------------------')

for i in range(vstup - 1, koniec + 1, kroky):
    print('{:11} {:20}'.format(i, i + 273))

