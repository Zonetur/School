def cz_to_tr(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def cz_to_prostokatny(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False

def delta(a, b, c):
    return b**2 - 4*a*c

def BMI(w, h):
    bmi = w / h**2
    if bmi < 16:
        return "wygłodzenie"
    elif 16 <= bmi < 16.99:
        return "wychudzenie"
    elif 16.99 <= bmi < 18.49:
        return "niedowaga"
    elif 18.49 <= bmi < 24.99:
        return "waga prawidłowa"
    elif 24.99 <= bmi < 29.99:
        return "nadwaga"
    elif 29.99 <= bmi < 34.99:
        return "otyłość I stopnia"
    else:
        return "otyłość II stopnia lub wyższa"

def main():
    a = float(input("Podaj długość pierwszego boku trójkąta: "))
    b = float(input("Podaj długość drugiego boku trójkąta: "))
    c = float(input("Podaj długość trzeciego boku trójkąta: "))

    if cz_to_tr(a, b, c):
        print("Można zbudować trójkąt.")
        if cz_to_prostokatny(a, b, c):
            print("Trójkąt jest prostokątny.")
        else:
            print("Trójkąt nie jest prostokątny.")
    else:
        print("Nie można zbudować trójkąta.")

    w = float(input("Podaj wagę w kilogramach: "))
    h = float(input("Podaj wzrost w metrach: "))
    print(f"Twoje BMI wynosi: {BMI(w, h)}")

if __name__ == "__main__":
    main()
