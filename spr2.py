import random
import math

# 1. Napisz funkcję, która wygeneruje listę liczb z zakresu od -1 do 1000 i zwróci tę listę.
def zad1():
    return list(range(-1, 1001))

wynik1 = zad1()
print("Zadanie 1:", wynik1[:10], "...", wynik1[-10:])  # Podgląd pierwszych i ostatnich 10 wartości

# 2. Napisz funkcję, która przepisze wszystkie liczby pierwsze z listy z zadania 1 i zwróci tę listę.
def zad2(lista):
    def czy_pierwsza(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x for x in lista if czy_pierwsza(x)]

wynik2 = zad2(wynik1)
print("Zadanie 2:", wynik2[:10])  # Podgląd pierwszych 10 wartości

# 3. Napisz funkcję, która zwróci liczbę liczb pierwszych w liście z zadania 2.
def zad3(lista):
    return len(lista)

wynik3 = zad3(wynik2)
print("Zadanie 3:", wynik3)

# 4. Napisz funkcję, która znajdzie największy wspólny dzielnik (NWD) dwóch liczb.
def zad4(a, b):
    return math.gcd(a, b)

wynik4 = zad4(78, 66)
print("Zadanie 4:", wynik4)

# 5. Napisz funkcję, która znajdzie najmniejszą wspólną wielokrotność (NWW) dwóch liczb.
def zad5(a, b):
    return abs(a * b) // math.gcd(a, b)

wynik5 = zad5(78, 66)
print("Zadanie 5:", wynik5)

# 6. Napisz funkcję, która dzieli odcinek a na 3 losowe wartości i zwraca listę zawierającą te wartości.
def zad6(a):
    podzial = sorted([random.randint(1, a - 2) for _ in range(2)])
    return [podzial[0], podzial[1] - podzial[0], a - podzial[1]]

wynik6 = zad6(100)
print("Zadanie 6:", wynik6)