import random

# Zad 1
with open("zad1.txt", "w") as plik:
    for _ in range(1000):
        liczba = random.randint(2, 1000)
        binarna = bin(liczba)[2:]
        plik.write(binarna + "\n")

# Zad 2
with open("zad1.txt", "r") as plik_we, open("zad2.txt", "w") as plik_wy:
    for linia in plik_we:
        binarna = linia.strip()
        dziesietna = int(binarna, 2)
        plik_wy.write(str(dziesietna) + "\n")

# Zad 3
liczby = []
with open("zad2.txt", "r") as plik:
    for linia in plik:
        liczby.append(int(linia.strip()))

dlugosc = len(liczby)
for i in range(dlugosc):
    for j in range(0, dlugosc - i - 1):
        if liczby[j] > liczby[j + 1]:
            tymczasowa = liczby[j]
            liczby[j] = liczby[j + 1]
            liczby[j + 1] = tymczasowa

with open("zad3.txt", "w") as plik:
    for l in liczby:
        plik.write(str(l) + "\n")

# Zad 4
with open("zad2.txt", "r") as plik_we, open("zad4.txt", "w") as plik_wy:
    for linia in plik_we:
        n = int(linia.strip())
        oryginalna = n
        czynniki = []
        dzielnik = 2
        while n > 1:
            while n % dzielnik == 0:
                czynniki.append(dzielnik)
                n = n // dzielnik
            dzielnik += 1

        czynniki.sort(reverse=True)
        wynik = str(oryginalna)
        for c in czynniki:
            wynik += "-" + str(c)
        plik_wy.write(wynik + "\n")

# Zad 5
with open("zad1.txt", "r") as plik_we, open("zad5.txt", "w") as plik_wy:
    for linia in plik_we:
        napis = linia.strip()
        if napis == napis[::-1]:
            plik_wy.write(napis + "\n")

# PRACA DOMOWA 20p

# Zad 6
with open("zad2.txt", "r") as plik_we, open("zad6.txt", "w") as plik_wy:
    for linia in plik_we:
        liczba = int(linia.strip())
        binarna = bin(liczba)[2:]
        plik_wy.write(str(liczba) + " - " + binarna + "\n")

# Zad 7
with open("zad2.txt", "r") as plik_we, open("zad7.txt", "w") as plik_wy:
    for linia in plik_we:
        liczba = int(linia.strip())
        if liczba % 3 == 0 and liczba % 5 == 0:
            plik_wy.write(str(liczba) + "\n")

# Zad 8
with open("zad2.txt", "r") as plik_we, open("zad8.txt", "w") as plik_wy:
    for linia in plik_we:
        tekst_liczby = linia.strip()
        suma_cyfr = 0
        for cyfra in tekst_liczby:
            suma_cyfr += int(cyfra)
        plik_wy.write(tekst_liczby + " - " + str(suma_cyfr) + "\n")

# Zad 9
liczby = []
with open("zad2.txt", "r") as plik:
    for linia in plik:
        liczby.append(linia.strip())

with open("zad9.txt", "w") as plik:
    for i in range(len(liczby) - 1, -1, -1):
        plik.write(liczby[i] + "\n")

# Zad 10
liczby = []
with open("zad2.txt", "r") as plik:
    for linia in plik:
        liczby.append(int(linia.strip()))

with open("zad10.txt", "w") as plik:
    for i in range(len(liczby)):
        for j in range(i + 1, len(liczby)):
            if liczby[i] + liczby[j] == 100:
                plik.write(str(liczby[i]) + " - " + str(liczby[j]) + "\n")
