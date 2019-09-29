import string

cyfry = ('zero', 'jeden',
         'dwa', 'trzy',
         'cztery', 'pięć',
         'sześć', 'siedem',
         'osiem', 'dziewięć')
ciag = input('Podaj ciag cyfr: ')

for x in ciag:
    if x not in string.digits:
        continue
    print(cyfry[int(x)])
