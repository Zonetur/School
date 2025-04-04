class Zwierze:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def dzwiek(self):
        return "Nieznany dźwięk"

    def info(self):
        return f"{self.__class__.__name__}: {self.imie}, wiek: {self.wiek} lat"

class Krowa(Zwierze):
    def dzwiek(self):
        return "Muu"

class Owca(Zwierze):
    def dzwiek(self):
        return "Bee"

class Swinia(Zwierze):
    def dzwiek(self):
        return "Chrum"

class Farma:
    def __init__(self):
        self.zwierzeta = []

    def dodaj_zwierze(self, zwierze):
        self.zwierzeta.append(zwierze)
        print(f"Dodano zwierzę: {zwierze.info()}")

    def wszystkie_zwierzeta(self):
        for zwierze in self.zwierzeta:
            print(zwierze.info(), "- wydaje dźwięk:", zwierze.dzwiek())

# Przykład użycia:
farma = Farma()

krowa1 = Krowa("Mila", 5)
owca1 = Owca("Bela", 3)
swinia1 = Swinia("Gruby", 2)

farma.dodaj_zwierze(krowa1)
farma.dodaj_zwierze(owca1)
farma.dodaj_zwierze(swinia1)

print("\nWszystkie zwierzęta na farmie:")
farma.wszystkie_zwierzeta()