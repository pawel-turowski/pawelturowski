import math

class FunkcjaKwadratowa:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f'{self.a}*x^2 + {self.b} * x + {self.c} ')

    def oblicz_wartość(self, x):
        return self.a * x * x + self.b * x + self.c

FunkcjaKwadratowa()