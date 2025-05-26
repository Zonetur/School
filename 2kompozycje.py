import os
import random
import time

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.id = str(time.time()) + str(random.randint(1, 100000))
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def inf(self):
        return f"[{self.id}] {self.imie} {self.nazwisko}, {self.wiek} lat"

    def to_string(self):
        return f"{self.id}|{self.imie}|{self.nazwisko}|{self.wiek}"

    @staticmethod
    def from_string(data):
        id_, imie, nazwisko, wiek = data.strip().split("|")
        osoba = Osoba(imie, nazwisko, int(wiek))
        osoba.id = id_
        return osoba

class Uczen:
    def __init__(self, osoba, klasa):
        self.osoba = osoba
        self.klasa = klasa
        self.oceny = {}
        self.absencje = []
        self.aktywne = True

    def dodaj_ocene(self, przedmiot, ocena):
        if przedmiot not in self.oceny:
            self.oceny[przedmiot] = []
        self.oceny[przedmiot].append(ocena)

    def usun_oceny(self, przedmiot):
        if przedmiot in self.oceny:
            del self.oceny[przedmiot]

    def srednia(self):
        wszystkie = [o for lista in self.oceny.values() for o in lista]
        return round(sum(wszystkie) / len(wszystkie), 2) if wszystkie else 0.0

    def dodaj_absencje(self, data):
        self.absencje.append(data)

    def zmien_status(self, status):
        self.aktywne = status

    def inf(self):
        print(self.osoba.inf())
        print(f"Klasa: {self.klasa}")
        for przedmiot, oceny in self.oceny.items():
            print(f"  {przedmiot}: {oceny}")
        print(f"Średnia: {self.srednia():.2f}")
        if self.absencje:
            print(f"Nieobecności: {', '.join(self.absencje)}")
        else:
            print("Brak nieobecności")
        print("Status: " + ("Aktywny" if self.aktywne else "Nieaktywny"))

    def to_string(self):
        base = self.osoba.to_string()
        oceny_str = ",".join(f"{p}:{','.join(map(str,o))}" for p,o in self.oceny.items())
        absencje_str = ";".join(self.absencje)
        return f"{base}|{self.klasa}|{oceny_str}|{absencje_str}|{int(self.aktywne)}"

    @staticmethod
    def from_string(data):
        parts = data.strip().split("|")
        osoba = Osoba.from_string("|".join(parts[:4]))
        klasa = parts[4]
        uczen = Uczen(osoba, klasa)
        if len(parts) > 5 and parts[5]:
            for przedmiot_oceny in parts[5].split(","):
                if ":" in przedmiot_oceny:
                    przedmiot, oceny_str = przedmiot_oceny.split(":")
                    oceny = list(map(int, oceny_str.split(",")))
                    uczen.oceny[przedmiot] = oceny
        if len(parts) > 6 and parts[6]:
            uczen.absencje = parts[6].split(";")
        if len(parts) > 7:
            uczen.aktywne = bool(int(parts[7]))
        return uczen

class Dziennik:
    def __init__(self):
        self.uczniowie = []

    def dodaj_ucznia(self, uczen):
        self.uczniowie.append(uczen)

    def znajdz_ucznia(self, nazwisko):
        return [u for u in self.uczniowie if u.osoba.nazwisko.lower() == nazwisko.lower()]

    def usun_ucznia(self, nazwisko):
        self.uczniowie = [u for u in self.uczniowie if u.osoba.nazwisko.lower() != nazwisko.lower()]

    def sortuj_po_sredniej(self):
        self.uczniowie.sort(key=lambda u: u.srednia(), reverse=True)

    def filtruj_klase(self, klasa):
        return [u for u in self.uczniowie if u.klasa.lower() == klasa.lower()]

    def znajdz_najlepszego(self):
        if not self.uczniowie:
            print("Brak uczniów.")
            return
        najlepszy = max(self.uczniowie, key=lambda u: u.srednia())
        print("Uczeń z najwyższą średnią:")
        najlepszy.inf()

    def znajdz_najgorszego(self):
        if not self.uczniowie:
            print("Brak uczniów.")
            return
        najgorszy = min(self.uczniowie, key=lambda u: u.srednia())
        print("Uczeń z najniższą średnią:")
        najgorszy.inf()

    def aktywni_uczniowie(self):
        return [u for u in self.uczniowie if u.aktywne]

    def zapisz_do_pliku(self, nazwa):
        with open(nazwa, "w", encoding="utf-8") as f:
            for u in self.uczniowie:
                f.write(u.to_string() + "\n")

    def wczytaj_z_pliku(self, nazwa):
        if not os.path.exists(nazwa):
            return
        with open(nazwa, "r", encoding="utf-8") as f:
            for linia in f:
                uczen = Uczen.from_string(linia.strip())
                self.dodaj_ucznia(uczen)

    def pokaz_wszystkich(self):
        if not self.uczniowie:
            print("Brak uczniów w dzienniku.")
            return
        for u in self.uczniowie:
            print("=" * 30)
            u.inf()

def menu():
    dziennik = Dziennik()
    dziennik.wczytaj_z_pliku("dziennik.txt")
    while True:
        print("\n MENU")
        print("1. Dodaj ucznia")
        print("2. Dodaj ocenę")
        print("3. Dodaj nieobecność")
        print("4. Wyświetl uczniów")
        print("5. Szukaj ucznia po nazwisku")
        print("6. Usuń ucznia")
        print("7. Sortuj po średniej")
        print("8. Filtruj po klasie")
        print("9. Najlepszy uczeń")
        print("10. Najgorszy uczeń")
        print("11. Zmień status ucznia")
        print("12. Zapisz do pliku")
        print("13. Wyjdź")
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            imie = input("Imię: ")
            nazwisko = input("Nazwisko: ")
            wiek = int(input("Wiek: "))
            klasa = input("Klasa: ")
            osoba = Osoba(imie, nazwisko, wiek)
            uczen = Uczen(osoba, klasa)
            dziennik.dodaj_ucznia(uczen)
        elif wybor == "2":
            nazwisko = input("Nazwisko ucznia: ")
            uczniowie = dziennik.znajdz_ucznia(nazwisko)
            if uczniowie:
                przedmiot = input("Przedmiot: ")
                ocena = int(input("Ocena: "))
                for uczen in uczniowie:
                    uczen.dodaj_ocene(przedmiot, ocena)
            else:
                print("Nie znaleziono ucznia.")
        elif wybor == "3":
            nazwisko = input("Nazwisko ucznia: ")
            uczniowie = dziennik.znajdz_ucznia(nazwisko)
            if uczniowie:
                data = input("Data nieobecności (dd-mm-rrrr): ")
                for uczen in uczniowie:
                    uczen.dodaj_absencje(data)
            else:
                print("Nie znaleziono ucznia.")
        elif wybor == "4":
            dziennik.pokaz_wszystkich()
        elif wybor == "5":
            nazwisko = input("Nazwisko: ")
            znalezieni = dziennik.znajdz_ucznia(nazwisko)
            if znalezieni:
                for u in znalezieni:
                    u.inf()
            else:
                print("Brak wyników.")
        elif wybor == "6":
            nazwisko = input("Nazwisko do usunięcia: ")
            dziennik.usun_ucznia(nazwisko)
        elif wybor == "7":
            dziennik.sortuj_po_sredniej()
        elif wybor == "8":
            klasa = input("Podaj klasę: ")
            wyniki = dziennik.filtruj_klase(klasa)
            for u in wyniki:
                u.inf()
        elif wybor == "9":
            dziennik.znajdz_najlepszego()
        elif wybor == "10":
            dziennik.znajdz_najgorszego()
        elif wybor == "11":
            nazwisko = input("Nazwisko ucznia: ")
            uczniowie = dziennik.znajdz_ucznia(nazwisko)
            if uczniowie:
                status = input("Podaj nowy status (aktywny/nieaktywny): ").lower()
                for u in uczniowie:
                    u.zmien_status(status == "aktywny")
            else:
                print("Nie znaleziono ucznia.")
        elif wybor == "12":
            dziennik.zapisz_do_pliku("dziennik.txt")
            print("Zapisano do pliku.")
        elif wybor == "13":
            dziennik.zapisz_do_pliku("dziennik.txt")
            print("Zamykam program.")
            break
        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    menu()