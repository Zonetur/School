import random
import math

# 1. Napisz funkcję, która wygeneruje listę liczb z zakresu od -1 do 1000 i zwróci tę listę.
def zad1():
    return list(range(-1, 1001))

wynik1 = zad1()
print("Zadanie 1:", wynik1[:10], "...", wynik1[-10:])  # Podgląd pierwszych i ostatnich 10 wartości

# 2. Napisz funkcję, która zwróci listę zawierającą wszystkie NWD dla liczb z zakresu n i m. Dzielnikiem jest k.
def zad2(n, m, k):
    return [math.gcd(x, k) for x in range(n, m + 1)]

wynik2 = zad2(1, 10, 5)
print("Zadanie 2:", wynik2)

# 3. Napisz funkcję, która powie, ile jest liczb pierwszych z zakresu n i m.
def zad3(n, m):
    def czy_pierwsza(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for x in range(n, m + 1) if czy_pierwsza(x))

wynik3 = zad3(-10, 5)
print("Zadanie 3:", wynik3)

# 4. Napisz funkcję, która zwróci najmniejszą wspólną wielokrotność (NWW) dwóch liczb.
def zad4(a, b):
    return abs(a * b) // math.gcd(a, b)

wynik4 = zad4(78, 66)
print("Zadanie 4:", wynik4)

# 5. Napisz funkcję, która zwróci minimalną wartość w liście, bez użycia wbudowanych metod.
def zad5(lista):
    min_wartosc = lista[0]
    for x in lista:
        if x < min_wartosc:
            min_wartosc = x
    return min_wartosc

wynik5 = zad5([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Zadanie 5:", wynik5)

# 6. Napisz funkcję, która dzieli odcinek a na 5 losowe wartości i zwraca listę zawierającą te wartości.
def zad6(a):
    podzial = sorted([random.randint(1, a - 1) for _ in range(4)])
    return [podzial[0], podzial[1] - podzial[0], podzial[2] - podzial[1], podzial[3] - podzial[2], a - podzial[3]]

wynik6 = zad6(100)
print("Zadanie 6:", wynik6)