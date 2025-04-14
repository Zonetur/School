import time
import random

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.id = str(time.time()) + str(random.randint(1, 100000))
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def inf(self):
        print(f"[Osoba] ID: {self.id}")
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Wiek: {self.wiek}")

class Uczen(Osoba):
    def __init__(self, imie, nazwisko, wiek, klasa):
        super().__init__(imie, nazwisko, wiek)
        self.klasa = klasa
        self.oceny = {}

    def dodaj_ocene(self, przedmiot, ocena):
        if przedmiot not in self.oceny:
            self.oceny[przedmiot] = []
        self.oceny[przedmiot].append(ocena)

    def srednia(self, przedmiot=None):
        if przedmiot:
            if przedmiot in self.oceny and self.oceny[przedmiot]:
                return sum(self.oceny[przedmiot]) / len(self.oceny[przedmiot])
            return 0.0
        wszystkie = [o for oceny in self.oceny.values() for o in oceny]
        return sum(wszystkie) / len(wszystkie) if wszystkie else 0.0

    def inf(self):
        super().inf()
        print(f"Klasa: {self.klasa}")
        print("Oceny:")
        for p, oceny in self.oceny.items():
            print(f"  {p}: {oceny}")
        print(f"Średnia ogólna: {self.srednia():.2f}")

class Dziennik:
    def __init__(self):
        self.lista_uczniow = []

    def dodaj_ucznia(self, uczen):
        self.lista_uczniow.append(uczen)

    def znajdz_ucznia(self, nazwisko):
        return [u for u in self.lista_uczniow if u.nazwisko == nazwisko]

    def wyswietl_wszystkich(self):
        for u in self.lista_uczniow:
            print("=" * 30)
            u.inf()

dziennik = Dziennik()
imiona = ["Anna", "Jan", "Kamil", "Ola", "Ewa"]
nazwiska = ["Kowalska", "Nowak", "Wiśniewski", "Zielińska", "Krawczyk"]
klasy = ["1A", "2B", "3C", "1A", "2B"]

for i in range(5):
    u = Uczen(imiona[i], nazwiska[i], 15 + i, klasy[i])
    u.dodaj_ocene("matematyka", random.randint(2, 5))
    u.dodaj_ocene("fizyka", random.randint(2, 5))
    u.dodaj_ocene("informatyka", random.randint(2, 5))
    dziennik.dodaj_ucznia(u)

dziennik.wyswietl_wszystkich()

print("\nSzukam ucznia o nazwisku 'Nowak':")
znalezieni = dziennik.znajdz_ucznia("Nowak")
for u in znalezieni:
    u.inf()
