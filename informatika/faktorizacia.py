#Milan Seliga II.F 
#vypocet faktorialu
n = int(input('Vlozte cislo: '))
fakt = 1
for i in range(n,0,-1):
    fakt = fakt * i
    print(fakt)
print('Vas vysledok je,',fakt)
    