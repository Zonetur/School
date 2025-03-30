def list_books(biblioteka: list) -> None:
    if not biblioteka:
        print("Biblioteka jest pusta.")
        return
    for book in biblioteka:
        for key, value in book.items():
            print(f"{key}: {value}")
        print("-" * 20)

def add_book(biblioteka: list, book: dict) -> None:
    biblioteka.append(book)
    print("Książka dodana.")

def remove_book(biblioteka: list, book_id: str) -> bool:
    for i, book in enumerate(biblioteka):
        if book["id"] == book_id:
            del biblioteka[i]
            return True
    return False

def edit_book(biblioteka: list, book_id: str, new_data: dict) -> bool:
    for book in biblioteka:
        if book["id"] == book_id:
            book.update(new_data)
            return True
    return False

def get_book(biblioteka: list, book_id: str) -> dict:
    for book in biblioteka:
        if book["id"] == book_id:
            return book
    return None

def search_books_by_title(biblioteka: list, title: str) -> list:
    results = []
    for book in biblioteka:
        if title.lower() in book.get("nazwa", "").lower():
            results.append(book)
    return results

def sort_books_by_page_count(biblioteka: list, reverse: bool = False) -> list:
    return sorted(biblioteka, key=lambda x: x.get("liczbaStron", 0), reverse=reverse)

def count_books(biblioteka: list) -> int:
    return len(biblioteka)

def clear_library(biblioteka: list) -> None:
    biblioteka.clear()
    print("Biblioteka została wyczyszczona.")
