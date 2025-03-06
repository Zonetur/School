import random

class Postac:
    def __init__(self, hp, atak):
        self.hp = hp
        self.atak = atak
        self.zyje = True
    def odejmij_hp(self, a):
        self.hp -= a
        if self.hp <= 0:
            self.zyje = False
    def czy_zyje(self):
        return self.zyje
    def basic_atak(self):
        return self.atak

class Sigma(Postac):
    def __init__(self):
        super().__init__(100, 10)
        self.obrona = 5
        self.punkty_zycia_max = 100
        self.energia = 100
        self.magia = 100
        self.mana = 100
        self.sila = 15
        self.furia = 0
        self.poziom = 1
        self.doswiadczenie = 0
        self.zwinnosc = 10
        self.inteligencja = 10
        self.wisdom = 10
        self.aurashield = 0
        self.moc = 20
        self.ladunki = 3
        self.kondycja = 5
    def obrona_bonus(self, dmg):
        return max(0, dmg - self.obrona)
    def odejmij_hp(self, a):
        super().odejmij_hp(self.obrona_bonus(a))
        self.furia += 1
    def ulecz_sie(self, wartosc):
        if self.zyje:
            self.hp = min(self.punkty_zycia_max, self.hp + wartosc)
    def regeneruj_energie(self, wartosc):
        if self.zyje:
            self.energia = min(100, self.energia + wartosc)
    def regeneruj_magie(self, wartosc):
        if self.zyje:
            self.magia = min(100, self.magia + wartosc)
    def regeneruj_mane(self, wartosc):
        if self.zyje:
            self.mana = min(100, self.mana + wartosc)
    def rzuć_zaklęcie(self):
        if self.magia >= 30:
            self.magia -= 30
            return self.atak * 4
        return 0
    def super_atak(self):
        if self.energia >= 50:
            self.energia -= 50
            return self.sila * 5
        return 0
    def teleportacja(self):
        if self.mana >= 40:
            self.mana -= 40
            return "Uniknął ataku!"
        return "Brak many!"
    def gniew(self):
        if self.furia >= 10:
            self.furia = 0
            return self.moc * 2
        return 0
    def wzmocnienie(self):
        if self.ladunki > 0:
            self.ladunki -= 1
            return self.atak + 5
        return self.atak
    def medytacja(self):
        if self.kondycja > 0:
            self.kondycja -= 1
            self.regeneruj_magie(10)
    def awansuj(self):
        self.poziom += 1
        self.doswiadczenie = 0
        self.atak += 2
        self.sila += 2
    def zysk_doswiadczenia(self, ile):
        self.doswiadczenie += ile
        if self.doswiadczenie >= 50:
            self.awansuj()
    def tarcza_aury(self):
        if self.aurashield < 3:
            self.aurashield += 1
    def odejmij_hp_tarcza(self, dmg):
        if self.aurashield > 0:
            self.aurashield -= 1
            dmg = max(0, dmg - 10)
        super().odejmij_hp(dmg)

class Czarodziej(Postac):
    def __init__(self):
        super().__init__(40, 12)
    def magia_ognia(self):
        return self.atak * 3
    def magia_lodu(self):
        return self.atak * 2

class Elf(Postac):
    def __init__(self):
        super().__init__(60, 10)
    def strzal_z_luku(self):
        return self.atak * 1.5
    def strzal_mrozacy(self):
        return self.atak * 1.8

class Rycerz(Postac):
    def __init__(self):
        super().__init__(120, 8)
    def szarza(self):
        return self.atak * 2.5
    def blok(self, dmg):
        return max(0, dmg - 4)

class Demon(Postac):
    def __init__(self):
        super().__init__(150, 20)
    def fala_zniszczenia(self):
        return self.atak * 3.5
    def klatwa(self):
        return self.atak * 2

class Barbarzynca(Postac):
    def __init__(self):
        super().__init__(100, 15)
        self.szal = 0
    def furia(self):
        self.szal += 1
        return self.atak * (1 + self.szal * 0.1)
    def rzut_toporem(self):
        return self.atak * 2

class Kaplanka(Postac):
    def __init__(self):
        super().__init__(50, 5)
        self.moc_uzdrawiania = 10
    def modlitwa_uzdrowienia(self):
        return self.moc_uzdrawiania
    def piorunujaca_latarnia(self):
        return self.atak * 3

class Palladyn(Postac):
    def __init__(self):
        super().__init__(110, 9)
        self.swieta_tarcza = 2
    def swiety_blask(self):
        return self.atak * 2
    def tarcza_boska(self, dmg):
        if self.swieta_tarcza > 0:
            self.swieta_tarcza -= 1
            return max(0, dmg - 8)
        return dmg

class Zabojca(Postac):
    def __init__(self):
        super().__init__(80, 12)
    def cios_w_plecy(self):
        return self.atak * 2.2
    def trucizna(self):
        return 5

class Golem(Postac):
    def __init__(self):
        super().__init__(200, 5)
        self.twardosc = 10
    def kamienna_skora(self, dmg):
        return max(0, dmg - self.twardosc)

class Iluzjonista(Postac):
    def __init__(self):
        super().__init__(55, 9)
        self.ilosc_iluzji = 3
    def stworz_iluzje(self):
        if self.ilosc_iluzji > 0:
            self.ilosc_iluzji -= 1
            return self.atak * 2
        return 0
    def hipnotyzuj(self):
        return self.atak * 1.7
    def zaslona_dymna(self):
        return 'Zniknął w kłębach dymu!'
    def reset_iluzji(self):
        self.ilosc_iluzji = 3
    def ukrycie(self):
        return 'Iluzjonista ukrywa się za jedną z iluzji.'
    def oslabienie_umyslu(self):
        return self.atak + 2
    def wzmocnienie_iluzji(self):
        return self.atak * 1.3
    def labirynt_umyslu(self):
        return self.atak * 3
    def destrukcyjna_mysl(self):
        return self.atak * 2.5
    def powielenie_ataku(self):
        return self.atak * 2

class MistrzMiecza(Postac):
    def __init__(self):
        super().__init__(110, 12)
        self.kombinacja = 0
    def ciag_ciosow(self):
        self.kombinacja += 1
        return self.atak + (self.kombinacja * 2)
    def reset_kombinacji(self):
        self.kombinacja = 0
    def ciemne_ostrze(self):
        return self.atak * 2.2
    def blyskawiczne_potezne_ciecie(self):
        return self.atak * 3.1
    def precyzyjny_blok(self, dmg):
        return max(0, dmg - 6)
    def miecz_duszy(self):
        return self.atak * 2
    def riposta(self):
        return self.atak * 1.8
    def bojowe_skupienie(self):
        return self.atak + 3
    def nieugieta_wola(self):
        return self.atak * 1.6
    def mistrzowski_finisher(self):
        return self.atak * 4

def generuj_przeciwnika():
    przeciwnicy = [
        Czarodziej,
        Elf,
        Rycerz,
        Demon,
        Barbarzynca,
        Kaplanka,
        Palladyn,
        Zabojca,
        Golem, Iluzjonista, MistrzMiecza
    ]
    return random.choice(przeciwnicy)()

class Arena:
    def __init__(self, sigma):
        self.sigma = sigma
        self.licznik_zabitych = 0
    def walka(self):
        while self.sigma.czy_zyje():
            print("Walka rozpoczęta")
            przeciwnik = generuj_przeciwnika()
            print(f"Nowy przeciwnik wkroczył do gry: {przeciwnik.__class__.__name__}")
            while przeciwnik.czy_zyje() and self.sigma.czy_zyje():
                # Rozszerzona logika walki
                dmg_przeciwnik = przeciwnik.basic_atak()
                dmg_sigma = self.sigma.basic_atak()
                if isinstance(przeciwnik, Barbarzynca):
                    dmg_przeciwnik += przeciwnik.furia()
                if isinstance(przeciwnik, Palladyn):
                    dmg_sigma = przeciwnik.tarcza_boska(dmg_sigma)
                if isinstance(przeciwnik, Zabojca):
                    dmg_sigma += przeciwnik.cios_w_plecy()
                    dmg_sigma += przeciwnik.trucizna()
                if isinstance(przeciwnik, Iluzjonista) and przeciwnik.czy_zyje():
                    dmg_przeciwnik += przeciwnik.stworz_iluzje()
                    self.sigma.odejmij_hp(przeciwnik.hipnotyzuj())
                    print(przeciwnik.zaslona_dymna())
                    dmg_sigma += przeciwnik.destrukcyjna_mysl()
                if isinstance(przeciwnik, MistrzMiecza) and przeciwnik.czy_zyje():
                    dmg_przeciwnik += przeciwnik.ciag_ciosow()
                    dmg_sigma = przeciwnik.precyzyjny_blok(dmg_sigma)
                    dmg_przeciwnik += przeciwnik.bojowe_skupienie()
                    dmg_przeciwnik += przeciwnik.mistrzowski_finisher()
                    przeciwnik.reset_kombinacji()
                if self.sigma.poziom > 5:
                    dmg_przeciwnik *= 0.9
                if self.sigma.hp < 50 and self.sigma.energia > 20:
                    self.sigma.energia -= 20
                    print('Sigma wykonuje desperacki atak!')
                    przeciwnik.odejmij_hp(self.sigma.atak * 3)
                if isinstance(przeciwnik, Iluzjonista) and przeciwnik.ilosc_iluzji == 0:
                    przeciwnik.reset_iluzji()
                if isinstance(przeciwnik, MistrzMiecza) and przeciwnik.czy_zyje():
                    dmg_przeciwnik += przeciwnik.miecz_duszy()
                    dmg_przeciwnik += przeciwnik.riposta()
                if self.sigma.aurashield > 0 and dmg_przeciwnik > 0:
                    dmg_przeciwnik = max(0, dmg_przeciwnik - 3)
                if self.sigma.poziom > 2:
                    self.sigma.sila += 1
                if self.sigma.furia > 5 and self.sigma.kondycja > 0:
                    self.sigma.kondycja -= 1
                    dmg_sigma += self.sigma.furia
                # Koniec rozszerzonej logiki
                self.sigma.odejmij_hp(dmg_przeciwnik)
                przeciwnik.odejmij_hp(dmg_sigma)
                if isinstance(przeciwnik, Demon) and przeciwnik.czy_zyje():
                    self.sigma.odejmij_hp(przeciwnik.fala_zniszczenia())
                    dmg_sigma += przeciwnik.klatwa()
                if isinstance(przeciwnik, Kaplanka) and przeciwnik.czy_zyje():
                    self.sigma.odejmij_hp(przeciwnik.piorunujaca_latarnia())
                if self.sigma.magia >= 30:
                    przeciwnik.odejmij_hp(self.sigma.rzuć_zaklęcie())
                if self.sigma.energia >= 50:
                    przeciwnik.odejmij_hp(self.sigma.super_atak())
                if self.sigma.furia >= 10:
                    przeciwnik.odejmij_hp(self.sigma.gniew())
                atak_wzmocniony = self.sigma.wzmocnienie()
                if atak_wzmocniony != self.sigma.atak:
                    przeciwnik.odejmij_hp(atak_wzmocniony)
                if self.sigma.poziom < 5:
                    self.sigma.zysk_doswiadczenia(10)
                self.sigma.medytacja()
                self.sigma.tarcza_aury()
            if self.sigma.czy_zyje():
                self.licznik_zabitych += 1

                self.sigma.ulecz_sie(5)
                self.sigma.regeneruj_energie(10)
                self.sigma.regeneruj_magie(5)
                self.sigma.regeneruj_mane(5)
def main():
    sigma = Sigma()
    arena = Arena(sigma)
    arena.walka()
    print(f"Liczba zabitych przeciwników: {arena.licznik_zabitych}")

if __name__ == "__main__":
    main()
