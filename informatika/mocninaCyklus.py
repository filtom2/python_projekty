#Milan Seliga II.F
#vypocet mocnin
n = int(input('Vlozte cislo: '))
mocnina = int(input('Vlozte na ktoru mocninu: '))


cislo = 1

for i in range(1, mocnina + 1):  #urcuje opakovanie
    cislo = n * cislo               

print('Vas vysledok je,', cislo)
