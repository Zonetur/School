def czy_parzysta(liczba:int)->bool:
    if liczba % 2 == 0:
        return True
    else:
        return False
    

def ile_parzystych(lista:list)->int:
    n = 0
    for element in lista:
        if czy_parzysta(element):
            n += 1
    return n
  #------------------------------------------
  import wejsciowka

liczby = [1, 2]

print(wejsciowka.ile_parzystych(liczby))
