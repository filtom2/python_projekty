#Milan Seliga II.F 
# sucet aritmetickeho radu
n = int(input('Vlozte cislo: '))
suma = 0
medzivysledky = input('Prajete si medzivysledky ? y/n ')

if medzivysledky == 'y':
    for i in range(1,n+1):
        suma = suma + i
        print(suma)
    print('Vysledne cislo je:',suma,'Priemer je,',suma/n)

elif medzivysledky == 'n':
    for i in range(1,n+1):
        suma = suma + i
    print(suma,'A priemer je,', suma/n)

else:
    print('Chyba spustite este raz.')