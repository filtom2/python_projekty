

vstup = int(input('Vlozte rok: '))

if vstup % 4 == 0:
    if vstup % 100 != 0:
        print('Je prechodny.')
    elif vstup % 100 == 0:
        if vstup % 400 == 0:
            print('Je prechodny.')
        else:
            print('Neni prechodny.')

    else:
        print('Rok neni prechodny.')
else:
    print('Rok neni prechodny.')
