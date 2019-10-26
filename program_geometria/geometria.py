# program geometria
import circle
import rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Wybierz opcję: '))

        # Wykonanie wybranej akcji.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Podaj promień okręgu: "))
            print('Pole powierzchni wynosi', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Podaj promień okręgu: "))
            print('Obwód wynosi',
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Podaj długość prostokąta: "))
            length = float(input("Podaj szerokość prostokąta: "))
            print('Pole powierzchni wynosi', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Podaj długość prostokąta: "))
            length = float(input("Podaj szerokość prostokąta: "))
            print('Obwód wynosi',
                  rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Zakończenie działania programu...')
        else:
            print('Błąd: nieprawidłowa opcja.')

# menu.
def display_menu():
    print(' MENU')
    print('1) Pole powierzchni okręgu')
    print('2) Obwód okręgu')
    print('3) Pole powierzchni prostokąta')
    print('4) Obwód prostokąta')
    print('5) Koniec')

# Wywołanie funkcji main().
main()