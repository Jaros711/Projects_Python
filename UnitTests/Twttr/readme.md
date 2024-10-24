# Opis programu: test_twttr.py

Program `test_twttr.py` jest zestawem testów jednostkowych dla funkcji `shorten` znajdującej się w module `twttr`. Jego celem jest weryfikacja, czy funkcja `shorten` poprawnie skraca ciągi tekstowe przez usunięcie samogłosków.

## Opis funkcjonalności:

1. **Import modułu**:
   - Program importuje funkcję `shorten` z modułu `twttr`:
     ```python
     from twttr import shorten
     ```

2. **Funkcja główna**:
   - `main()` to główna funkcja, która uruchamia wszystkie testy:
     ```python
     def main():
         test_upper_lower()
         test_numbers()
         test_punctuation()
     ```

3. **Testy jednostkowe**:
   - Program zawiera trzy funkcje testowe, które sprawdzają różne scenariusze dla funkcji `shorten`.

   ### 3.1. `test_upper_lower()`:
   - Sprawdza, czy funkcja `shorten` poprawnie usuwa samogłoski z tekstów zawierających litery małe i wielkie:
     ```python
     assert shorten("twitter") == "twttr"
     assert shorten("TWITTER") == "TWTTR"
     ```

   ### 3.2. `test_numbers()`:
   - Sprawdza, czy funkcja `shorten` zwraca niezmieniony ciąg tekstowy, gdy wejście składa się wyłącznie z cyfr:
     ```python
     assert shorten("9876") == "9876"
     ```

   ### 3.3. `test_punctuation()`:
   - Sprawdza, czy funkcja `shorten` zwraca niezmieniony ciąg tekstowy, gdy wejście składa się z znaków interpunkcyjnych:
     ```python
     assert shorten("<>?") == "<>?"
     ```

4. **Uruchomienie testów**:
   - Program uruchamia testy jednostkowe, wywołując funkcję `main()` tylko wtedy, gdy skrypt jest uruchamiany bezpośrednio:
     ```python
     if __name__ == "__main__":
         main()
     ```

## Wykorzystanie:
Program `test_twttr.py` jest użyteczny do automatycznego testowania funkcji `shorten` w module `twttr`, co zapewnia, że funkcja działa zgodnie z oczekiwaniami i poprawnie przetwarza różne typy wejść.

