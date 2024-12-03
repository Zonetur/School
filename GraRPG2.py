from random import randint
import random

# Stała liczba rund
liczba_rund = 21

def display_grand_tournament():
    art = """
                             GRAND TOURNAMENT
   _______________________________________________________________________
  |                                                                       |
  |                  OSTATECZNE STARCIE NA WIELKIM TURNIEJU CHWAŁY        |
  |_______________________________________________________________________|

                       /|                                                 |\\      
                     //||                                                 ||\\\\
                   //  ||                                                 ||  \\\\
                 //    ||                 **KONFRONTACJA*                 ||    \\\\
               //      ||                                                 ||      \\\\
             //________||_________                                   ______||________\\\\
            //         ||        \\                                 /        ||         \\\\
           //          ||         \\                             /          ||          \\\\
         O=====[======||==========={>>>>>>>>>>>>>>>>>>>>>>>>>==========||======]=====O
         |\\           ||           \\                             /           ||           /|
         | \\          ||            \\                           /            ||          / |
         |  \\_________||___________  \\_________         _______/  __________||_________/  |
         |            ||            |          |       |          |            ||            |
         |   RYCERZ I ||            |          |       |          |            ||   RYCERZ II |
         |___________/||\\___________|          |_______|          |___________/||\\___________|
         |           /||\\            \\________/       \\________/            /||\\           |
         |__________/ || \\_________________________________________________/ || \\__________|
         |_________/  ||  \\_______________________________________________/  ||  \\_________|
                   \\  ||                                                 ||  /
                    \\ ||                                                 || /
                     \\||                                                 ||/
                      ||                                                 ||
                   ___||                                                 ||___
                 _/____\\_______________________________________________/____\\_
                /      /                                               \\      \\
               /______|                                                 |______\\
              //||||||\\                                               //||||||\\\\
             //  ||  ||                                              //  ||  ||\\\\
            //   ||  ||                                             //   ||  ||  \\\\
       ____//____||__||___________________________________________//____||__||____\\\\____
      (____)     ||  ||                                           (____)     ||  || (____)
                  ||  ||                                                     ||  ||
                  ^^  ^^                                                     ^^  ^^

   =======================================================================
                       * WIELKI TURNIEJ RYCERSKI *
   =======================================================================
    """
    print(art)

def display_game_end(winner_name):
    art = f"""
                             GRAND TOURNAMENT
   _______________________________________________________________________
  |                                                                       |
  |                        GRATULACJE, {winner_name.upper()}!             |
  |_______________________________________________________________________|

        _____                                                         _____
       /     \\                                                      /     \\
      /       \\                  JESTEŚ ZWYCIĘZCĄ!                /       \\
      \\       /                                                  \\       /
       \\_____/                                                    \\_____/

               O                                                  O
              /|\\                                                /|\\
             / | \\                                              / | \\
            /  |  \\                                            /  |  \\
       ____/___|___\\__________________________________________/___|___\\____
      /                        WIKTORIA JEST TWOJA!                     \\
     |                                                                         |
      \\_______________________________________________________________________/

                   ^^^                                                ^^^
                  (o_o)                                              (o_o)
                  <| |>                                              <| |>
                  /   \\                                              /   \\

   =======================================================================
                                * CHWAŁA I HONOR *
   =======================================================================
    """
    print(art)

# Wyświetl zachętę
display_grand_tournament()

# Definicja graczy
player_one_name = input('Podaj imię pierwszego rycerza: ')
player_one_hp = 420
player_one_mana = 210
player_one_power = 10
player_one_inicjatywa = randint(1, 100)

player_two_name = input('Podaj imię drugiego rycerza: ')
player_two_hp = 420
player_two_mana = 210
player_two_power = 10
player_two_inicjatywa = randint(1, 100)

# Funkcja do generowania losowego ataku
def czynnik_losowy_ataku():
    return randint(10, 40)

# Funkcja wyboru artefaktu
def wybierz_artefakt():
    print("\nWybierz artefakt:")
    print("1 - Magiczna kopia (dodaje bonus +5 do siły)")
    print("2 - Ulepszony koń (dodaje bonus +15 do inicjatywy)")
    print("3 - Magiczny naszyjnik (dodaje bonus +30 do many)")
    wybor = input("Wybór (1/2/3): ")

    if wybor == "1":
        return 'kopia'
    elif wybor == "2":
        return 'kon'
    elif wybor == "3":
        return 'naszyjnik'
    else:
        print("Niepoprawny wybór, wybieram magiczną kopię.")
        return 'kopia'

# Funkcja przypisania artefaktu do gracza
def przypisz_artefakt(gracz, artefakt):
    if artefakt == 'kopia':
        gracz['power'] += 5  # Magiczna kopia zwiększa siłę o 5
        print(f"{gracz['name']} otrzymuje Magiczną Kopię! Bonus do siły: +5")
    elif artefakt == 'kon':
        gracz['inicjatywa'] += 15  # Ulepszony koń zwiększa inicjatywę o 15
        print(f"{gracz['name']} otrzymuje Ulepszonego Konia! Bonus do inicjatywy: +15")
    elif artefakt == 'naszyjnik':
        gracz['mana'] += 30  # Magiczny naszyjnik dodaje 30 many
        print(f"{gracz['name']} otrzymuje Magiczny Naszyjnik! Bonus do many: +30")

# Funkcja klasycznego ataku
def klasyczny_atak(rycerz, hp_przeciwnika):
    atak = czynnik_losowy_ataku() + rycerz['power']
    rycerz['mana'] += 10  # Dodawanie 10 many po każdym klasycznym ataku
    print(f"{rycerz['name']} wykonuje klasyczny atak! Zadaje {atak} obrażeń.")
    hp_przeciwnika -= atak
     # Zapewniamy, że HP nie spadnie poniżej 0
    hp_przeciwnika = max(hp_przeciwnika, 0)
    return hp_przeciwnika

# Funkcja magicznego ataku
def magiczny_atak(rycerz, hp_przeciwnika):
    if rycerz['mana'] < 20:
        print("Za mało many na atak magiczny!")
        return hp_przeciwnika, rycerz['mana']
    atak = czynnik_losowy_ataku() + rycerz['power'] * 2  # Atak magiczny jest silniejszy
    print(f"{rycerz['name']} wykonuje magiczny atak! Zadaje {atak} obrażeń.")
    hp_przeciwnika -= atak
    rycerz['mana'] -= 20  # Zmniejszanie many po ataku magicznym
    # Zapewniamy, że HP nie spadnie poniżej 0
    hp_przeciwnika = max(hp_przeciwnika, 0)
    return hp_przeciwnika, rycerz['mana']

# Funkcja leczenia
def leczenie(rycerz):
    if rycerz['mana'] < 30:
        print("Za mało many na leczenie!")
        return rycerz['hp'], rycerz['mana']
    leczenie = 50  # Odzyskuje 50 HP
    rycerz['hp'] += leczenie
    rycerz['mana'] -= 30  # Koszt leczenia
    print(f"Leczenie! Odzyskujesz {leczenie} HP.")
    return rycerz['hp'], rycerz['mana']

# Funkcja zwiększenia inicjatywy
def zwieksz_inicjatywe(rycerz):
    if rycerz['mana'] < 30:
        print("Za mało many na zwiększenie inicjatywy!")
        return rycerz['inicjatywa'], rycerz['mana']
    zwiekszenie = 10  # Zwiększenie inicjatywy o 10
    rycerz['inicjatywa'] += zwiekszenie
    rycerz['mana'] -= 30  # Koszt zwiększenia inicjatywy
    print(f"Inicjatywa zwiększona o {zwiekszenie}!")
    return rycerz['inicjatywa'], rycerz['mana']

# Funkcja zwiększenia siły
def zwieksz_sile(rycerz):
    if rycerz['mana'] < 50:
        print("Za mało many na zwiększenie siły!")
        return rycerz['power'], rycerz['mana']
    zwiekszenie = 5  # Zwiększenie siły o 5
    rycerz['power'] += zwiekszenie
    rycerz['mana'] -= 50  # Koszt zwiększenia siły
    print(f"Siła zwiększona o {zwiekszenie}!")
    return rycerz['power'], rycerz['mana']

# Funkcja losujących wydarzeń
def losowe_wydarzenie():
    wydarzenia = [
        'doping', 'burza', 'smok', 'kurtyzany', 'morowe_powietrze',
        'ksiezniczka', 'wiedzma', 'tornado', 'zakochany_pies'
    ]
    wydarzenie = random.choice(wydarzenia)

    if wydarzenie == 'doping':
        losowy_gracz = randint(1, 2)
        if losowy_gracz == 1:
            bonus_sila = randint(1, 5)  # Losowy bonus siły (1 do 5)
            bonus_inicjatywa = randint(1, 10)  # Losowy bonus inicjatywy (1 do 10)
            gracz = gracz_1
            print(f"Tłum jest zachwycony rycerzem {gracz['name']}! Przez doping zyskuje +{bonus_sila} siły i +{bonus_inicjatywa} inicjatywy!")
            gracz['power'] += bonus_sila
            gracz['inicjatywa'] += bonus_inicjatywa
        else:
            bonus_sila = randint(1, 5)  # Losowy bonus siły (1 do 5)
            bonus_inicjatywa = randint(1, 10)  # Losowy bonus inicjatywy (1 do 10)
            gracz = gracz_2
            print(f"Tłum jest zachwycony rycerzem o imieniu {gracz['name']}! Przez doping zyskuje +{bonus_sila} siły i +{bonus_inicjatywa} inicjatywy!")
            gracz['power'] += bonus_sila
            gracz['inicjatywa'] += bonus_inicjatywa

    elif wydarzenie == 'burza':
        print("\nNagle nad polem walki pojawia się groźna burza! Oboje rycerze muszą zmierzyć się z jej potężnym wiatrem.")
        gracz_1['hp'] = gracz_1['hp'] - randint(10, 40)
        gracz_2['hp'] = gracz_2['hp'] - randint(10, 40)
        print(f"Rycerze tracą trochę zdrowia przez burzę! {gracz_1['name']} HP: {gracz_1['hp']}, {gracz_2['name']} HP: {gracz_2['hp']}")

    elif wydarzenie == 'smok':
        print("\nZ nieba spada smok! Jego ognisty oddech zagraża wszystkim.")
        if randint(1, 2) == 1:
            gracz_1['hp'] -= 50
            print(f"Smok atakuje {gracz_1['name']}! Traci 50 HP.")
        else:
            gracz_2['hp'] -= 50
            print(f"Smok atakuje {gracz_2['name']}! Traci 50 HP.")

    elif wydarzenie == 'kurtyzany':
        print("\nZjawiają się kurtyzany, które zaczynają śpiewać i tańczyć wokół rycerzy.")
        bonus_inicjatywa = randint(1, 5)
        if randint(1, 2) == 1:
            gracz_1['inicjatywa'] += bonus_inicjatywa
            print(f"{gracz_1['name']} zyskuje bonus do inicjatywy dzięki urokowi kurtyzan! +{bonus_inicjatywa}")
        else:
            gracz_2['inicjatywa'] += bonus_inicjatywa
            print(f"{gracz_2['name']} zyskuje bonus do inicjatywy dzięki urokowi kurtyzan! +{bonus_inicjatywa}")

    elif wydarzenie == 'ksiezniczka':
        print("\nZakochana księżniczka ogląda pojedynek i rzuca kwiaty w stronę rycerzy.")
        if randint(1, 2) == 1:
            gracz_1['mana'] += 20
            print(f"{gracz_1['name']} zyskuje 20 many dzięki błogosławieństwu księżniczki!")
        else:
            gracz_2['mana'] += 20
            print(f"{gracz_2['name']} zyskuje 20 many dzięki błogosławieństwu księżniczki!")

    elif wydarzenie == 'wiedzma':
        print("\nWiedźma pojawia się w trakcie bitwy, aby przepowiedzieć wynik.")
        if randint(1, 2) == 1:
            print(f"Wiedźma przepowiada, że rycerzowi {gracz_1['name']} uda się zwyciężyć!")
        else:
            print(f"Wiedźma przepowiada, że rycerzowi {gracz_2['name']} uda się zwyciężyć!")

    elif wydarzenie == 'tornado':
        print("\nPojawia się wielkie tornado, które zmienia przebieg bitwy!")
        tornado = randint(1, 2)
        if tornado == 1:
            gracz_1['hp'] -= 30
            print(f"Tornado uderza w {gracz_1['name']}! Traci 30 HP.")
        else:
            gracz_2['hp'] -= 30
            print(f"Tornado uderza w {gracz_2['name']}! Traci 30 HP.")

    elif wydarzenie == 'morowe_powietrze':
        print("\nGigant, który siedzi na trybunach zjadł coś niedobrego - niestety strasznie nasmrodził! Aż w oczy szczypie!")
        oddzialywanie_na_gracza_1 = randint(1,100)
        oddzialywanie_na_gracza_2 = randint(1,100)
        gracz_1['inicjatywa'] -= oddzialywanie_na_gracza_1
        print(f"{gracz_1['name']} traci {oddzialywanie_na_gracza_1} inicjatywy!")
        gracz_2['inicjatywa'] -= oddzialywanie_na_gracza_2
        print(f"{gracz_2['name']} traci {oddzialywanie_na_gracza_2} inicjatywy!")

    elif wydarzenie == 'zakochany_pies':
        print("\nZakochany pies wbiega na pole bitwy, szukając swojego właściciela.")
        if randint(1, 2) == 1:
            gracz_1['hp'] += 10
            print(f"Pies przynosi odrobinę szczęścia {gracz_1['name']}! Zyskuje 10 HP.")
        else:
            gracz_2['hp'] += 10
            print(f"Pies przynosi odrobinę szczęścia {gracz_2['name']}! Zyskuje 10 HP.")
    input("Naciśnij dowolny klawisz, aby kontynuować...")

# Funkcja losowej narracji o widowni
def losowa_narracja():
    narracje = [
        f"Krasnoludy na trybunach zaczęły bluzgać {gracz_1['name']} za słabą obronę! Nie podoba im się jego styl walki.",
        f"Ogromny aplauz z trybun, kiedy {gracz_2['name']} wykonał perfekcyjny cios! Widownia jest pod wrażeniem!",
        f"Grupa goblinów na widowni zaczęła się kłócić, bo postawili zakład na {gracz_1['name']} i teraz tracą pieniądze!",
        f"Tłum wiwatuje, a elfy zaczęły śpiewać pieśń pochwalną na cześć {gracz_2['name']}! Widać ich poparcie.",
        f"Ogromne zaskoczenie na trybunach, kiedy {gracz_1['name']} wykonał niespodziewany atak! Widownia wstrzymała oddech.",
        f"Troll z trybun krzyczy w stronę {gracz_2['name']}: 'Wstyd! Pokonaj go!' Tłum zaczyna go wspierać.",
        f"Z trybun rozbrzmiewa śmiech grupy kurtyzan, które uwielbiają oglądać każdy ruch gracza {gracz_1['name']}. To chyba ich ulubiony rycerz!",
        f"Z oddali można usłyszeć pieśń o miłości, którą śpiewa zakochana księżniczka w imieniu {gracz_2['name']}! Tłum jest wzruszony.",
        f"Z nieba spada ogromny cień – to smoki przelatują nad areną, ale nie zagrażają rycerzom. Tłum wiwatuje na ich widok!",
        f"Na trybunach pojawiła się tajemnicza postać - wiedźma z wielkim kapeluszem, która szeptała, że zwycięzca tej bitwy będzie błogosławiony przez same bogi!",
        f"Na widowni widać kilku wędrownych wojowników, którzy składają zakłady o wyniku walki. Kibicują obojgu rycerzom, ale patrzą z zaciekawieniem na {gracz_1['name']}.",
        f"Zbiorowisko krasnoludów zaczęło rzucać kamieniami w stronę areny, ale nie trafiły one ani w {gracz_2['name']}, ani w jego przeciwnika. Wygląda na to, że to tylko ich sposób na rozrywkę.",
        f"W tłumie dostrzega się niewielką grupę drowów, którzy szeptają między sobą o legendzie starożytnego artefaktu, który miałby pojawić się, jeśli ten pojedynek skończy się remisem.",
        f"Olbrzymia chmura dymu unosi się nad areną, przypominając chmurę po wielkiej bitwie, ale tylko niektórzy widzowie zauważają, że to tylko zabawa magików na trybunach!"
    ]
    print(random.choice(narracje))
    input("Naciśnij dowolny klawisz, aby kontynuować...")

# Funkcja do wykonania tury (wybór ataku lub działania)
def wykonaj_ture(gracz, przeciwnik_hp):
    print(f"\n{gracz['name']} wykonuje ruch!")
    print("Wybierz akcję:")
    print("1 - Atak klasyczny - odpoczynek od czarów dodaje 10 many")
    print("2 - Atak magiczny (kosztuje 20 many)")
    print("3 - Rzuć czar leczenie +50 (kosztuje 30 many)")
    print("4 - Rzuć czar zwiększenie inicjatywy +10 (kosztuje 30 many)")
    print("5 - Rzuć czar zwiększenie siły +5 (kosztuje 50 many)")
    wybor = input("Wybór (1/2/3/4/5): ")

    if wybor == "1":
        przeciwnik_hp = klasyczny_atak(gracz, przeciwnik_hp)
    elif wybor == "2":
        if gracz['mana'] >= 20:
            przeciwnik_hp, gracz['mana'] = magiczny_atak(gracz, przeciwnik_hp)
        else:
            print("Za mało many na atak magiczny! Wykonano atak klasyczny.")
            przeciwnik_hp = klasyczny_atak(gracz, przeciwnik_hp)
    elif wybor == "3":
        gracz['hp'], gracz['mana'] = leczenie(gracz)
    elif wybor == "4":
        gracz['inicjatywa'], gracz['mana'] = zwieksz_inicjatywe(gracz)
    elif wybor == "5":
        gracz['power'], gracz['mana'] = zwieksz_sile(gracz)
    else:
        print("Niepoprawny wybór, wykonano atak klasyczny.")
        przeciwnik_hp = klasyczny_atak(gracz, przeciwnik_hp)

    return przeciwnik_hp

# sprawdź kto zaczyna rundę na podstawie inicjatywy
def kto_zaczyna():
    if player_one_inicjatywa > player_two_inicjatywa:
        return 'gracz_1'
    elif player_two_inicjatywa > player_one_inicjatywa:
        return 'gracz_2'
    else:
        # Jeśli inicjatywa jest taka sama, rzut losowy
        return 'gracz_1' if randint(1, 2) == 1 else 'gracz_2'

# Wybór artefaktów dla graczy
print(f"\n{player_one_name}, wybierz swój artefakt:")
artefakt_gracz_1 = wybierz_artefakt()
gracz_1 = {
    'name': player_one_name,
    'hp': player_one_hp,
    'mana': player_one_mana,
    'power': player_one_power,
    'inicjatywa': player_one_inicjatywa
}
przypisz_artefakt(gracz_1, artefakt_gracz_1)

print(f"\n{player_two_name}, wybierz swój artefakt:")
artefakt_gracz_2 = wybierz_artefakt()
gracz_2 = {
    'name': player_two_name,
    'hp': player_two_hp,
    'mana': player_two_mana,
    'power': player_two_power,
    'inicjatywa': player_two_inicjatywa
}
przypisz_artefakt(gracz_2, artefakt_gracz_2)

# Główna pętla gry - zmiana tur

while gracz_1['hp'] > 0 and gracz_2['hp'] > 0:
    podsumowanie = f"| {gracz_1['name']} HP: {gracz_1['hp']} | Mana: {gracz_1['mana']} | Inicjatywa: {gracz_1['inicjatywa']} | Siła: {gracz_1['power']} | {gracz_2['name']} HP: {gracz_2['hp']} | Mana: {gracz_2['mana']} | Inicjatywa: {gracz_2['inicjatywa']} | Siła: {gracz_2['power']} |"
    dlugosc_podsumowania = len(podsumowanie)
    print("-" * dlugosc_podsumowania)
    print(podsumowanie)
    print("-" * dlugosc_podsumowania)

    # Sprawdzanie, kto zaczyna turę
    kto_pierwszy = kto_zaczyna()

    if kto_pierwszy == 'gracz_1':
        # Gracz 1 wykonuje atak lub akcję
        gracz_2['hp'] = wykonaj_ture(gracz_1, gracz_2['hp'])
        print(f"{gracz_2['name']} pozostało {gracz_2['hp']} HP | Mana: {gracz_2['mana']}")
        # Sprawdzenie, czy gra się skończyła
        if gracz_2['hp'] <= 0:
            print(f"{gracz_2['name']} przegrał! {gracz_1['name']} wygrywa!")
            display_game_end(gracz_1['name'])
            break

        # Gracz 2 wykonuje atak lub akcję
        gracz_1['hp'] = wykonaj_ture(gracz_2, gracz_1['hp'])
        print(f"{gracz_1['name']} pozostało {gracz_1['hp']} HP | Mana: {gracz_1['mana']}")
        # Sprawdzenie, czy gra się skończyła
        if gracz_1['hp'] <= 0:
            print(f"{gracz_1['name']} przegrał! {gracz_2['name']} wygrywa!")
            display_game_end(gracz_2['name'])
            break

    else:
        # Gracz 2 wykonuje atak lub akcję
        gracz_1['hp'] = wykonaj_ture(gracz_2, gracz_1['hp'])
        print(f"{gracz_1['name']} pozostało {gracz_1['hp']} HP | Mana: {gracz_1['mana']}")
        # Sprawdzenie, czy gra się skończyła
        if gracz_1['hp'] <= 0:
            print(f"{gracz_1['name']} przegrał! {gracz_2['name']} wygrywa!")
            display_game_end(gracz_2['name'])
            break

        # Gracz 1 wykonuje atak lub akcję
        gracz_2['hp'] = wykonaj_ture(gracz_1, gracz_2['hp'])
        print(f"{gracz_2['name']} pozostało {gracz_2['hp']} HP | Mana: {gracz_2['mana']}")
        # Sprawdzenie, czy gra się skończyła
        if gracz_2['hp'] <= 0:
            print(f"{gracz_2['name']} przegrał! {gracz_1['name']} wygrywa!")
            display_game_end(gracz_1['name'])
            break

    # Wydarzenie co 4 rundy
    if liczba_rund % 4 == 0:
        losowe_wydarzenie()

    # Narracja co 3 rundy ale nie ma narracji gdy jest wydarzenie
    if liczba_rund % 3 == 0 and liczba_rund % 4 != 0:
        losowa_narracja()

    # zmniejszenie liczby rund o 1
    liczba_rund -= 1
    print(f'pozostało {liczba_rund} rund do końca')

    # Sprawdzenie rundy
    if liczba_rund == 0:
        print("Koniec rund! Gra zakończona remisem!")
        break
