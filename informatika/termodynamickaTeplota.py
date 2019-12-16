#Milan Seliga II.F
#vypocet tabulky

vstup = int(input('Zadajte zaciatocnu cislo: '))
koniec = int(input('Zadajte koncovu teplotu: '))
kroky = int(input('Zadajte po kolko chcete zvacsovat: '))
for i in range(vstup - 1, koniec + 1, kroky):
    print(i, i + 273)
