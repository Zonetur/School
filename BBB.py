
with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = [int(num) for num in file.read().split()]

with open("even.txt", "w", encoding="utf-8") as file:
    for num in numbers:
        if num % 2 == 0:
            file.write(f"{num}\n")

print("Liczby parzyste zostały zapisane do pliku even.txt.")





with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = [int(num) for num in file.read().split()]

with open("odd.txt", "w", encoding="utf-8") as file:
    for num in numbers:
        if num % 2 != 0:
            file.write(f"{num}\n")

print("Liczby nieparzyste zostały zapisane do pliku odd.txt.")