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
    if trojuholnikA + trojuholnikB > trojuholnikC and trojuholnikB + trojuholnikC > trojuholnikA and trojuholnikC + trojuholnikA > trojuholnikB:
        print('Trojuholnik sa da narysovat.')
        if trojuholnikC ** 2 == trojuholnikB ** 2 + trojuholnikA ** 2:
            print('Trojuholnik je pravouhly.')
        else:
            print('Trojuholnik neni pravouhly.')
    else:
        print('Neda sa narysovat.')

if odpoved1 == '2':
    print('Vybrali ste si rovinny utvar znamy pod nazvom stvoruholnik.')
    print('Zadajte strany :')