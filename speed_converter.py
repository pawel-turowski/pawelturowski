START_SPEED = 60            # Pierwsza wartość na liście.
END_SPEED = 131             # Górna granica listy.
INCREMENT = 10              # Wielkość kroku.
CONVERSION_FACTOR = 0.6214  # Współczynnik konwersji.

print('KPH\tMPH')
print('--------------')

for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))