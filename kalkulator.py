import sys

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def zapisz_wynik(wynik):
    with open('/tmp/wynik.txt', 'w') as file:
        file.write(str(wynik))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Użycie: python3 calc.py <liczba_1> <+/-/*> <liczba_2>")
        sys.exit(1)

    liczba_1 = float(sys.argv[1])
    operacja = sys.argv[2]
    liczba_2 = float(sys.argv[3])

    if operacja == '+':
        wynik = dodaj(liczba_1, liczba_2)
    elif operacja == '-':
        wynik = odejmij(liczba_1, liczba_2)
    else:
        print("Nieobsługiwana operacja. Obsługiwane operatory to '+' i '-'.")
        sys.exit(1)

    print("Wynik:", wynik)
    zapisz_wynik(wynik)

