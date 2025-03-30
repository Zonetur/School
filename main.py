from  book import create_book
import library

biblioteka = []

def print_menu():
    print("\n==== MENU BIBLIOTEKI ====")
    print("l - Lista książek")
    print("d - Dodaj książkę")
    print("u - Usuń książkę")
    print("e - Edytuj książkę")
    print("s - Wyszukaj książkę po tytule")
    print("o - Sortuj książki według liczby stron")
    print("c - Wyczyść bibliotekę")
    print("q - Wyjście z programu")
    print("=========================")

def add_book_flow():
    nazwa = input("Podaj nazwę książki: ")
    liczba_stron = int(input("Podaj liczbę stron: "))
    new_book = create_book(nazwa, liczba_stron)
    library.add_book(biblioteka, new_book)

def remove_book_flow():
    book_id = input("Podaj ID książki do usunięcia: ")
    if library.remove_book(biblioteka, book_id):
        print("Książka usunięta.")
    else:
        print("Nie znaleziono książki o podanym ID.")

def edit_book_flow():
    book_id = input("Podaj ID książki do edycji: ")
    book = library.get_book(biblioteka, book_id)
    if book:
        print("Obecne dane książki:")
        for key, value in book.items():
            print(f"{key}: {value}")
        nazwa = input("Podaj nową nazwę (pozostaw puste, aby nie zmieniać): ")
        liczba_stron_input = input("Podaj nową liczbę stron (pozostaw puste, aby nie zmieniać): ")
        new_data = {}
        if nazwa:
            new_data["nazwa"] = nazwa
        if liczba_stron_input:
            new_data["liczbaStron"] = int(liczba_stron_input)
        if new_data:
            library.edit_book(biblioteka, book_id, new_data)
            print("Książka zaktualizowana.")
        else:
            print("Brak zmian.")
    else:
        print("Nie znaleziono książki o podanym ID.")

def search_book_flow():
    tytul = input("Podaj tytuł do wyszukania: ")
    results = library.search_books_by_title(biblioteka, tytul)
    if results:
        print(f"Znaleziono {len(results)} książek:")
        for book in results:
            for key, value in book.items():
                print(f"{key}: {value}")
            print("-" * 20)
    else:
        print("Nie znaleziono książek o podanym tytule.")

def sort_books_flow():
    order = input("Sortować rosnąco (a) czy malejąco (d)? ").strip().lower()
    reverse = True if order == 'd' else False
    sorted_books = library.sort_books_by_page_count(biblioteka, reverse)
    if sorted_books:
        print("Książki posortowane według liczby stron:")
        for book in sorted_books:
            for key, value in book.items():
                print(f"{key}: {value}")
            print("-" * 20)
    else:
        print("Biblioteka jest pusta.")

def clear_library_flow():
    confirm = input("Czy na pewno chcesz wyczyścić bibliotekę? (t/n): ").strip().lower()
    if confirm == 't':
        library.clear_library(biblioteka)
    else:
        print("Anulowano operację czyszczenia biblioteki.")

def main():
    while True:
        print_menu()
        command = input("Wybierz komendę: ").strip().lower()
        if command == 'l':
            library.list_books(biblioteka)
        elif command == 'd':
            add_book_flow()
        elif command == 'u':
            remove_book_flow()
        elif command == 'e':
            edit_book_flow()
        elif command == 's':
            search_book_flow()
        elif command == 'o':
            sort_books_flow()
        elif command == 'c':
            clear_library_flow()
        elif command == 'q':
            print("Program zakończy działanie.")
            break
        else:
            print("Nie ma takiej komendy.")

if __name__ == "__main__":
    main()
