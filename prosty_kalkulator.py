import math



def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnożenie(a, b ):
    return a * b

def dzielenie(a, b):
    return a/b

def potęgowanie(a, b):
    return a**b

def pierwiastek(c):
    return math.sqrt(c)  # c = a + b

def logarytm(a, b):
    return math.log(a, b)




if __name__ == '__main__':
    user_a = int(input('podaj liczbę: '))
    user_b = int(input('podaj liczbę: '))
    user_c = user_a + user_b
    wynik_dodawania = dodawanie(user_a, user_b)
    wynik_odejmowania = odejmowanie(user_a, user_b)
    wynik_mnożenia = mnożenie(user_a, user_b)
    wynik_dzielenia = dzielenie(user_a, user_b)
    wynik_potęgowania = potęgowanie(user_a, user_b)
    wynik_pierwiastkowania = pierwiastek(user_c)
    wynik_logarytmu = logarytm(user_a, user_b)
    print(f'dodawanie: {wynik_dodawania}')
    print(f'odejmowanie: {wynik_odejmowania}')
    print(f'mnożenie: {wynik_mnożenia}')
    print(f'dzielenie: {wynik_dzielenia}')
    print(f'potęgowanie: {wynik_potęgowania}')
    print(f'pierwiastek: {wynik_pierwiastkowania}')
    print(f'logarytm: {wynik_logarytmu}')
