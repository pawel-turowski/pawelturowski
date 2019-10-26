def nDigit(nDigitOd, nDigitDo):
    nList = []
    for i in range (nDigitOd, nDigitDo):
        for x in range(2,i):
            if ( i % x) == 0:
                break
            else:
                if (x == i-1):
                    nList.append(i)
    if (i == nDigitDo-1):
        print('Liczby pierwsze: ')
        print (nList)

nDigit(0,501)