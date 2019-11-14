#Milan Seliga II.F
print('Vitajte v programe na ratanie roznych parametroch utvarov.')
print('1. Trojuholnik \n2. Stvoruholnik \n3. Ihlan \n4. Kvader')
odpoved1 = input('Zvolte si utvar:')

if odpoved1 == '1':
    print('Vybrali ste si rovinny utvar znamy pod nazvom trojuholnik.')
    print('Zadajte strany :')
    trojuholnikA = int(input('Zadajte rozmery strany a: '))
    trojuholnikB = int(input('Zadajte rozmery strany b: '))
    trojuholnikC = int(input('Zadajte rozmery strany c: '))

                    #TODO spravit obvod trojuholnika

    if trojuholnikA + trojuholnikB > trojuholnikC and trojuholnikB + trojuholnikC > trojuholnikA and trojuholnikC + trojuholnikA > trojuholnikB:  #zisti ci sa da vypocitat
        print('Trojuholnik sa da narysovat.')
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

if odpoved1 == '2':
    print('Vybrali ste si rovinny utvar znamy pod nazvom stvoruholnik.')
    print('Zadajte strany a uhly v stupnoch (0-180): ')
    stvoruholnikA = int(input('a: '))
    stvoruholnikB = int(input('b: '))
    stvoruholnikC = int(input('c: '))
    stvoruholnikD = int(input('d: '))
    stvoruholnikAuhol = int(input('alfa: '))
    stvoruholnikBuhol = int(input('beta: '))
    stvoruholnikCuhol = int(input('delta: '))
    stvoruholnikDuhol = int(input('ten stvrty uhol: '))

    if stvoruholnikA == stvoruholnikB and stvoruholnikA == stvoruholnikC and stvoruholnikA == stvoruholnikD and stvoruholnikAuhol == 90 and stvoruholnikBuhol == 90 and stvoruholnikCuhol == 90 and stvoruholnikDuhol == 90:  #zisti ci je to stvorec
        print(
            'Je to stvorec/ pretoze obe protilahle strany maju rovnaku dlzku  a uhly maju 90 stunpov'
        )
    elif stvoruholnikA == stvoruholnikC and stvoruholnikB == stvoruholnikD:  #zisti ci to je obdlznik
        print('Je to obdlznik.')
    #TODO urobit zvysne typy stvoruholnikov
