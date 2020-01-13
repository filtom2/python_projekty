cislo = 1
suma = 0
pokusy = 0
while cislo != 0:
    cislo = int(input('Vlozte cislo :'))
    print(cislo)
    suma += cislo
    pokusy += 1 

print('Celkovy sucet pokusov je',suma,'a priemer je',suma/(pokusy-1),'a pocet pokusov je',pokusy)
