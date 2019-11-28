#Milan Seliga II.F
#porgram na vypocet utvarov
import math
print('Vitajte v matematickom programe')
print('')

print('Pre výber trojuholníka stlačte 1')
print('Pre výber štvoruholníka stlačte 2')
print('Pre výber ihlana stlačte 3')

print()

w = int(input('Vyberte si prosím útvar: '))
print()

if w == 1:
    print('Vybrali ste si trojuholník(rovinný útvar)')
    print()
    a = int(input('Zadajte dľžku strany a v cm: '))
    b = int(input('Zadajte dľžku strany b v cm: '))
    c = int(input('Zadajte dľžku strany c v cm: '))
    print()
    if a + b > c and b + c > a and c + a > b:
        print('Váš trojuholník sa dá zostrojiť')
        if c == b == a:
            print('Váš trojuholník je rovnostranný')
        elif a == b or b == c or c == a:
            print('Váš trojuholník je rovnoramenný')
        else:
            print('Váš trojuholník je rôznostranný')
        if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == c**2 + a**2:
            print('Váš trojuholník je pravouhlý')
        else:
            print('Váš trojuholník nie je pravouhlý')
        print('Obvod Vášho trojuholníka je: ', a + b + c, 'cm')
    else:
        print('Váš trojuholník sa nedá zostrojiť')

elif w == 2:
    print('Vybrali ste si štvoruholník(rovinný útvar)')
    print()
    a = int(input('Zadajte dľžku strany a v cm: '))
    b = int(input('Zadajte dľžku strany b v cm: '))
    c = int(input('Zadajte dľžku strany c v cm: '))
    d = int(input('Zadajte dľžku strany d v cm: '))
    alfa = int(input('Zadajte veľkosť uhla alfa: '))
    beta = int(input('Zadajte veľkosť uhla beta: '))
    delta = int(input('Zadajte veľkosť uhla delta: '))
    gama = int(input('Zadajte veľkosť uhla gama: '))
    print()
    if alfa == beta == delta == gama == 90 and a == b == c == d:
        print('Štvoruholník je štvorec')
        print('Obsah Vášho štvorca je: ', a**2, 'cm2')
        print('Obvod Vášho štvorca je: ', 4 * a, 'cm')
        print('Dĺžka uhlopriečky Vášho štvorca je: ', a * (math.sqrt(2)), 'cm')
        print('Polomer opísanej kružnice je: ', a / (math.sqrt(2)), 'cm')
        print('Polomer vpísanej kružnice je: ', a / 2, 'cm')
    elif a == c and b == d and alfa == beta == gama == delta == 90 or a == b and d == c and alfa == beta == gama == delta == 90 or a == d and b == c and alfa == beta == gama == delta == 90:
        print('Štvoruholník je obdľžnik')
        print('Obsah Vášho obdľžnika je: ', a * b, 'cm2')
        print('Obvod Vášho obdľžnika je: ', a + b + c + d, 'cm')
        print('Dľžka uhlopriečky Vášho obdľžnika je: ', math.sqrt(a**2 + b**2),
              'cm')
        print('Polomer opísanej kružnice Vášho obdľžnika je: ',
              math.sqrt(a**2 + b**2) / 2, 'cm')
    elif alfa == beta and gama == delta and a == b == c == d and alfa == beta < 90 and gama == delta > 90 < 180 or beta == gama < 90 and delta == alfa > 90 < 180 or delta == beta < 90 and alfa == gama > 90 < 180 or beta == gama < 90 and delta == alfa > 90 < 180 and a == b == c == d and alfa == beta < 90 and gama == delta > 90 < 180 or beta == gama < 90 and delta == alfa > 90 < 180 or delta == beta < 90 and alfa == gama > 90 < 180 or delta == beta < 90 and alfa == gama > 90 < 180 and a == b == c == d and alfa == beta < 90 and gama == delta > 90 < 180 or beta == gama < 90 and delta == alfa > 90 < 180 or delta == beta < 90 and alfa == gama > 90 < 180:
        print('Váš štvoruholník je kosoštvorec')
        v1 = int(
            input(
                'Zadajte dľžku výšky kolmú na stranu a Vášho kosoštvorca v cm: '
            ))
        print('Obsah Vášho kosoštvorca je: ', a * v1, 'cm2')
        print('Obvod Vášho kosoštvorca je: ', 4 * a, 'cm')
    elif a == c and b == d or a == b and d == c or d == a and b == c or alfa == beta < 90 and gama == delta > 90 < 180 or beta == gama < 90 and delta == alfa > 90 < 180 or delta == beta < 90 and alfa == gama > 90 < 180 or beta == gama < 90 and delta == alfa > 90 < 180:
        print('Váš štvoruholník je kosodľžnik')
        v1 = int(
            input(
                'Zadajte dľžku výšky kolmú na stranu a Vášho kosodľžnika v cm: '
            ))
        print('Obvod Vášho kosodľžnika je: ', a + b + c + d, 'cm')
        print('Obsah Vášho kosodľžika je: ', a * v1, 'cm2')
elif w == 3:
    print('Vybrali ste si ihlan')
    a = float(input('Zadajte dľžku strany a v cm: '))
    b = float(input('Zadajte dľžku strany b v cm: '))
    v1 = float(input('Zadajte dľžku výšky v v cm: '))
    Sp = a * b
    if a == b:
        print('Podstava ihlana je štvorec')
    else:
        print('Podstava ihlana je obdľžnik')
    print('Obsah podstavy ihlana je: ', Sp, 'cm2')
    print('Objem Vášho ihlana je: ', (1 / 3) * Sp * v1, 'cm2')
    print(
        'Povrch Vášho ihlana je: ',
        a * b + (a * (math.sqrt(v1 * v1 + (b * b) / 2))) +
        (b * math.sqrt(v1 * v1 + (b * b) / 2)), 'cm2')
