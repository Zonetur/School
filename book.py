import uuid

def create_book(nazwa: str, liczba_stron: int) -> dict:
    book_id = str(uuid.uuid4())
    return {"id": book_id, "nazwa": nazwa, "liczbaStron": liczba_stron}

def validate_book_data(nazwa: str, liczba_stron: int) -> bool:
    if not nazwa:
        return False
    if not isinstance(liczba_stron, int) or liczba_stron <= 0:
        return False
    return True

if __name__ == "__main__":
    print("Testowanie modułu book.py")
    test_book = create_book("Przykładowa Książka", 123)
    print("Utworzona książka:", test_book)
    valid = validate_book_data("Przykładowa Książka", 123)
    print("Czy dane są poprawne?", valid)
