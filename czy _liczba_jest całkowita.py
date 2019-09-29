liczba = input('podaj liczbę całkowita: ')
try:
    liczba = int(liczba)
except ValueError:
    print('Miała być całkowita!!!')
    exit()