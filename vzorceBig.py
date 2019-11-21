#Milan Seliga II.F
from time import sleep
print('Vitajte v programe na ratanie roznych parametroch utvarov.')
print('1. Trojuholnik \n2. Stvoruholnik \n3. Ihlan \n4. Kvader')
odpoved1 = input('Zvolte si utvar:')

if odpoved1 == '1':
    print('Vybrali ste si rovinny utvar znamy pod nazvom trojuholnik.')
    print('Zadajte strany :')
    trojuholnikA = int(input('Zadajte rozmery strany a: '))
    trojuholnikB = int(input('Zadajte rozmery strany b: '))
    trojuholnikC = int(input('Zadajte rozmery strany c ktora je prepona: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    #TODO spravit obvod trojuholnika

    if trojuholnikA + trojuholnikB > trojuholnikC and trojuholnikB + trojuholnikC > trojuholnikA and trojuholnikC + trojuholnikA > trojuholnikB:  #zisti ci sa da vypocitat
        print('Trojuholnik sa da narysovat.')
        print('Obvod je ', trojuholnikA + trojuholnikB + trojuholnikC, 'cm.')
        if trojuholnikA == trojuholnikB and trojuholnikA == trojuholnikC and trojuholnikB == trojuholnikC:
            print('Trojuholnik je rovnostranny.')
        elif trojuholnikA != trojuholnikB and trojuholnikA != trojuholnikC and trojuholnikC != trojuholnikB:
            print('Trojuholnik je roznostranny')
        else:
            print('Trojuholnik je rovnoramenny')
        if trojuholnikC**2 == trojuholnikB**2 + trojuholnikA**2:  #zisti ci je pravouhly
            print('Trojuholnik je pravouhly.')
        else:
            print('Trojuholnik neni pravouhly.')
    else:
        print('Neda sa narysovat.')

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if odpoved1 == '2':
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Vybrali ste si rovinny utvar znamy pod nazvom stvoruholnik.')
    print('Zadajte strany a uhly v stupnoch (0-180): ')
    stvoruholnikA = int(input('a: '))
    stvoruholnikB = int(input('b: '))
    stvoruholnikC = int(input('c: '))
    stvoruholnikD = int(input('d: '))
    alfa = int(input('alfa: '))
    beta = int(input('beta: '))
    gamma = int(input('delta: '))
    delta = int(input('ten stvrty uhol: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if alfa and gamma > 90 < 180 and beta and delta < 90 and stvoruholnikA == stvoruholnikB and stvoruholnikC == stvoruholnikD and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikC and stvoruholnikD == stvoruholnikA and stvoruholnikA:
        print('Je to kosostvorec.')
    #TODO urobit zvysne typy stvoruholnikov najprv uhly, ci su poroti sebe potom
    elif alfa and gamma > 90 < 180 and beta and delta < 90 and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikD:
        print('Je to kosodlznik')
    elif alfa and gamma and beta and delta == 90 and stvoruholnikA == stvoruholnikB and stvoruholnikC == stvoruholnikD and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikC and stvoruholnikD == stvoruholnikA and stvoruholnikA:
        print('Je to stvorec.')
    elif alfa and gamma and beta and delta == 90 and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikD:
        print('Je to obdlznik.')
