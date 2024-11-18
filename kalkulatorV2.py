import math

def kalkulator_figur_bryl():
    print("Wybierz kategorię:")
    print("1. Figury płaskie")
    print("2. Bryły")
    wybor_kategorii = input("Wprowadź numer kategorii: ")

    if wybor_kategorii == "1":
        print("\nWybierz figurę:")
        print("1. Koło")
        print("2. Prostokąt")
        print("3. Kwadrat")
        print("4. Trójkąt")
        print("5. Romb")
        print("6. Równoległobok")
        print("7. Trapez")
        print("8. Deltoid")
        print("9. Przekątna kwadratu")
        print("10. Twierdzenie Pitagorasa")
        wybor_figury = input("Wprowadź numer figury: ")

        if wybor_figury == "1":
            r = float(input("Podaj promień koła: "))
            pole = math.pi * r**2
            obwod = 2 * math.pi * r
            print(f"Pole koła: {pole:.2f}")
            print(f"Obwód koła: {obwod:.2f}")

        elif wybor_figury == "2":
            a = float(input("Podaj długość pierwszego boku prostokąta: "))
            b = float(input("Podaj długość drugiego boku prostokąta: "))
            pole = a * b
            obwod = 2 * (a + b)
            print(f"Pole prostokąta: {pole:.2f}")
            print(f"Obwód prostokąta: {obwod:.2f}")

        elif wybor_figury == "3":
            a = float(input("Podaj długość boku kwadratu: "))
            pole = a**2
            obwod = 4 * a
            print(f"Pole kwadratu: {pole:.2f}")
            print(f"Obwód kwadratu: {obwod:.2f}")

        elif wybor_figury == "4":
            print("1. Pole z wysokością")
            print("2. Pole ze wzoru")
            print("3. Obwód")
            pod_wybor = input("Wybierz rodzaj obliczeń: ")
            if pod_wybor == "1":
                a = float(input("Podaj długość podstawy: "))
                h = float(input("Podaj wysokość: "))
                pole = 0.5 * a * h
                print(f"Pole trójkąta: {pole:.2f}")
            elif pod_wybor == "2":
                a = float(input("Podaj długość pierwszego boku: "))
                b = float(input("Podaj długość drugiego boku: "))
                c = float(input("Podaj długość trzeciego boku: "))
                if a + b > c and a + c > b and b + c > a:
                    s = (a + b + c) / 2
                    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    print(f"Pole trójkąta: {pole:.2f}")
                else:
                    print("Nie można utworzyć trójkąta z podanych boków.")
            elif pod_wybor == "3":
                a = float(input("Podaj długość pierwszego boku: "))
                b = float(input("Podaj długość drugiego boku: "))
                c = float(input("Podaj długość trzeciego boku: "))
                print(f"Obwód trójkąta: {a + b + c:.2f}")

        elif wybor_figury == "5":
            e = float(input("Podaj długość pierwszej przekątnej: "))
            f = float(input("Podaj długość drugiej przekątnej: "))
            pole = 0.5 * e * f
            a = float(input("Podaj długość boku rombu: "))
            obwod = 4 * a
            print(f"Pole rombu: {pole:.2f}")
            print(f"Obwód rombu: {obwod:.2f}")

        elif wybor_figury == "6":
            a = float(input("Podaj długość podstawy: "))
            h = float(input("Podaj wysokość: "))
            b = float(input("Podaj długość drugiego boku: "))
            pole = a * h
            obwod = 2 * (a + b)
            print(f"Pole równoległoboku: {pole:.2f}")
            print(f"Obwód równoległoboku: {obwod:.2f}")

        elif wybor_figury == "7":
            a = float(input("Podaj długość pierwszej podstawy: "))
            b = float(input("Podaj długość drugiej podstawy: "))
            h = float(input("Podaj wysokość: "))
            pole = 0.5 * (a + b) * h
            print(f"Pole trapezu: {pole:.2f}")

        elif wybor_figury == "8":
            e = float(input("Podaj długość pierwszej przekątnej: "))
            f = float(input("Podaj długość drugiej przekątnej: "))
            pole = 0.5 * e * f
            print(f"Pole deltoidu: {pole:.2f}")

        elif wybor_figury == "9":
            a = float(input("Podaj długość boku kwadratu: "))
            d = a * math.sqrt(2)
            print(f"Długość przekątnej kwadratu: {d:.2f}")

        elif wybor_figury == "10":
            a = float(input("Podaj długość pierwszej przyprostokątnej: "))
            b = float(input("Podaj długość drugiej przyprostokątnej: "))
            c = math.sqrt(a**2 + b**2)
            print(f"Długość przeciwprostokątnej: {c:.2f}")

    elif wybor_kategorii == "2":
        print("\nWybierz bryłę:")
        print("1. Kula")
        print("2. Stożek")
        print("3. Walec")
        wybor_bryly = input("Wprowadź numer bryły: ")

        if wybor_bryly == "1":
            r = float(input("Podaj promień kuli: "))
            pole = 4 * math.pi * r**2
            objetosc = (4 / 3) * math.pi * r**3
            print(f"Pole kuli: {pole:.2f}")
            print(f"Objętość kuli: {objetosc:.2f}")

        elif wybor_bryly == "2":
            r = float(input("Podaj promień podstawy stożka: "))
            h = float(input("Podaj wysokość stożka: "))
            l = math.sqrt(r**2 + h**2)  # Tworząca
            pole_boczne = math.pi * r * l
            pole_calkowite = math.pi * r * (r + l)
            objetosc = (1 / 3) * math.pi * r**2 * h
            print(f"Pole boczne stożka: {pole_boczne:.2f}")
            print(f"Pole całkowite stożka: {pole_calkowite:.2f}")
            print(f"Objętość stożka: {objetosc:.2f}")

        elif wybor_bryly == "3":
            r = float(input("Podaj promień podstawy walca: "))
            h = float(input("Podaj wysokość walca: "))
            pole_boczne = 2 * math.pi * r * h
            pole_calkowite = 2 * math.pi * r * (r + h)
            objetosc = math.pi * r**2 * h
            print(f"Pole boczne walca: {pole_boczne:.2f}")
            print(f"Pole całkowite walca: {pole_calkowite:.2f}")
            print(f"Objętość walca: {objetosc:.2f}")

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

# Uruchomienie kalkulatora
kalkulator_figur_bryl()
