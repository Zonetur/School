class KlasaA:
    def __init__(self, a, b, wartosc, liczba, tekst, flaga, n, zmienna_przec, lista, slownik):
        self.a = a
        self.b = b
        self.wartosc = wartosc
        self.liczba = liczba
        self.tekst = tekst
        self.flaga = flaga
        self.n = n
        self.zmienna_przec = zmienna_przec
        self.lista = lista
        self.slownik = slownik

    def get_x(self):
        return f"wartość x: {self.a}"

    def sum_values(self):
        return f"suma y + wartosc: {self.b + self.wartosc}"

    def increment(self):
        self.liczba += 1
        return f"zwiększono liczba o 1, teraz wynosi {self.liczba}"

    def first_five(self):
        return f"lista pierwszych 5: {[self.a, self.b, self.wartosc, self.liczba, self.tekst]}"

    def check_flag(self):
        return f"typ flaga to {type(self.flaga)}"

    def square(self):
        return f"n do kwadratu: {self.n ** 2}"

    def get_all(self):
        return f"wszystko: {[self.a, self.b, self.wartosc, self.liczba, self.tekst, self.flaga, self.n, self.zmienna_przec, self.lista, self.slownik]}"


class KlasaB:
    def __init__(self, param_a, param_b, param_c, param_d, param_e, param_f, param_g, param_h, param_i, param_j):
        self.param_a = param_a
        self.param_b = param_b
        self.param_c = param_c
        self.param_d = param_d
        self.param_e = param_e
        self.param_f = param_f
        self.param_g = param_g
        self.param_h = param_h
        self.param_i = param_i
        self.param_j = param_j

    def show_a(self):
        return f"a to: {self.param_a}"

    def show_b_c(self):
        return f"b i c to: {self.param_b}, {self.param_c}"

    def to_upper(self):
        self.param_d = str(self.param_d).upper()
        return f"d na wielkie litery: {self.param_d}"

    def length_e(self):
        return f"długość e: {len(str(self.param_e))}"

    def multiply_f(self):
        return f"f * 10 = {self.param_f * 10}"

    def divide_g(self):
        if isinstance(self.param_g, (int, float)):
            return f"g / 2 = {self.param_g / 2}"
        return "g nie jest liczbą"

    def show_all(self):
        return f"wszystko klasa_b: {[self.param_a, self.param_b, self.param_c, self.param_d, self.param_e, self.param_f, self.param_g, self.param_h, self.param_i, self.param_j]}"


class KlasaC:
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8
        self.p9 = p9
        self.p10 = p10

    def show_first(self):
        return f"p1: {self.p1}"

    def check(self):
        if self.p2 > 0:
            return f"p2 dodatnie ({self.p2})"
        return f"p2 nie dodatnie ({self.p2})"

    def add_five(self):
        self.p3 += 5
        return f"p3 + 5: {self.p3}"

    def combine(self):
        return f"razem p4 i p5: {str(self.p4) + str(self.p5)}"

    def fetch_values(self):
        return f"p6, p7, p8: {self.p6}, {self.p7}, {self.p8}"

    def make_list(self):
        self.p9 = list(str(self.p9))
        return f"p9 lista: {self.p9}"

    def all_values(self):
        return f"wszystko: {[self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8, self.p9, self.p10]}"


def main():
    obj_a1 = KlasaA(1, 2, 3, 4, "jakis tekst", True, 5, 8.9, [1, 2], {"klucz": "wartosc"})
    obj_a2 = KlasaA(10, 20, 30, 40, "cos tam", False, 7, 1.1, [5, 6], {"foo": "bar"})
    obj_a3 = KlasaA(100, 200, 300, 400, "python", True, 11, 2.2, [9, 0], {"xyz": 123})

    obj_b1 = KlasaB("Ala", "ma", "kota", "dom", 123, 5, 3.14, True, None, "koniec")
    obj_b2 = KlasaB("Test", "B2", "B3", "napis", "coś", 10, 42, False, 99, "X")
    obj_b3 = KlasaB("Jan", "Nowak", "Python", "Krakow", "Info", 100, 256, 3.14, 0, "Ostatni")

    inst_c1 = KlasaC(1, 2, 3, "c4", "c5", 6, 7, 8, "txt9", 10)
    inst_c2 = KlasaC(0, -5, 50, 100, 200, "abc", "def", "ghi", "tekst", 99)
    inst_c3 = KlasaC(5, 10, 15, True, False, [1, 2, 3], {"k": "w"}, 3.14, "czesc", "swiat")

    print(obj_a1.get_x())
    print(obj_a1.increment())
    print(obj_a1.get_all())

    print(obj_b1.to_upper())
    print(obj_b1.show_all())

    print(inst_c2.check())
    print(inst_c2.add_five())
    print(inst_c2.all_values())


if __name__ == "__main__":
    main()
