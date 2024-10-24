# Opis programu: Konwersja camelCase na snake_case

Program `camel.py` to prosty skrypt, który konwertuje napisy w formacie camelCase na format snake_case. CamelCase to styl pisania, w którym kolejne słowa są łączone bez spacji, a każde nowe słowo zaczyna się od wielkiej litery (np. `thisIsCamelCase`). Snake_case to styl, w którym wszystkie litery są małe, a słowa są oddzielone podkreślnikiem (np. `this_is_snake_case`).

## Opis funkcjonalności:

1. **Funkcja konwersji**:
   - `camel_to_snake(camel_case)`: ta funkcja przyjmuje jeden argument, `camel_case`, który jest napisem w formacie camelCase.
   - Funkcja inicjalizuje pusty ciąg `snake_case`, w którym będzie przechowywana końcowa wartość.

2. **Iteracja po znakach**:
   - Program przechodzi przez każdy znak w ciągu wejściowym.
   - Dla każdego znaku sprawdza, czy jest on wielką literą:
     - Jeśli tak, dodaje do `snake_case` znak podkreślenia oraz małą wersję tego znaku.
     - Jeśli nie, po prostu dodaje znak do `snake_case`.

3. **Zwracanie wyniku**:
   - Funkcja zwraca przetworzony ciąg `snake_case`.

4. **Interakcja z użytkownikiem**:
   - Program prosi użytkownika o wprowadzenie napisu w formacie camelCase.
   - Po wprowadzeniu, wywołuje funkcję `camel_to_snake` i wyświetla wynik konwersji.

## Przykład użycia:

1. Użytkownik uruchamia program:

Enter a camelCase string: thisIsCamelCase The snake_case is: this_is_camel_case


Program ten jest przydatnym narzędziem dla programistów, którzy chcą szybko przekształcić nazwy zmiennych lub funkcji z formatu camelCase na snake_case, co jest często wymagane w różnych konwencjach kodowania.
