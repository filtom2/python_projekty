#Milan Seliga II.F
from time import sleep
print('Vitajte v programe na ratanie roznych parametroch utvarov.')
print('1. Trojuholnik \n2. Stvoruholnik \n3. Ihlan \n4. Kvader')
odpoved1 = input('Zvolte si utvar:')

if odpoved1 == '1':
    sleep(1)
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
            if True:
                print('Obsah je',trojuholnikA*trojuholnikB / 2,'cm2.')
        else:
            print('Trojuholnik neni pravouhly.')
    else:
        print('Neda sa narysovat.')

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if odpoved1 == '2':
    sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Vybrali ste si rovinny utvar znamy pod nazvom stvoruholnik.')
    print('Zadajte strany a uhly v stupnoch (0-180) Zadavajte postupne!: ')
    stvoruholnikA = int(input('a: '))
    stvoruholnikB = int(input('b: '))
    stvoruholnikC = int(input('c: '))
    stvoruholnikD = int(input('d: '))
    alfa = int(input('alfa: '))
    beta = int(input('beta: '))
    gamma = int(input('delta: '))
    delta = int(input('ten stvrty uhol: '))
    obsahstvorec = stvoruholnikA * stvoruholnikB
    obvod = stvoruholnikB +stvoruholnikC +stvoruholnikA+stvoruholnikD
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if alfa and gamma > 90 < 180 and beta and delta < 90 and stvoruholnikA == stvoruholnikB and stvoruholnikC == stvoruholnikD and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikC and stvoruholnikD == stvoruholnikA and stvoruholnikA:
        print('Je to kosostvorec.')
        print(obvod,'<-- obvod v cm')
    #TODO urobit zvysne typy stvoruholnikov najprv uhly, ci su poroti sebe potom
    elif alfa and gamma > 90 < 180 and beta and delta < 90 and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikD:
        print('Je to kosodlznik')
        print(obvod,'<-- obvod v cm')
    elif alfa and gamma and beta and delta == 90 and stvoruholnikA == stvoruholnikB and stvoruholnikC == stvoruholnikD and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikC and stvoruholnikD == stvoruholnikA and stvoruholnikA:
        print('Je to stvorec.')
        print(obvod,'<-- obvod v cm')
        print(obsahstvorec,'<-- obsah v cm2')
    elif alfa and gamma and beta and delta == 90 and stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikD:
        print('Je to obdlznik.')
        print(obsah,'<-- obsah v cm2')
        print(obvod,'<-- obvod v cm')
    elif alfa < 90 < gamma < 180 and beta < 90 < delta < 180 and alfa == beta and stvoruholnikD == stvoruholnikB and stvoruholnikA > 0 and stvoruholnikD > 0:
        print('Je to lichobeznik.')
        print(obvod,'<-- obvod v cm')