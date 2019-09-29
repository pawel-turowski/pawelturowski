class change_digital:
    def int_to_Roman(self, num) -> object:
        intg = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // intg[i]):
                roman_num += rom[i]
                num -= intg[i]
            i += 1
        return roman_num

if __name__ == '__main__':
    change=int(input('Liczba:'))

    print(change_digital().int_to_Roman(change))

