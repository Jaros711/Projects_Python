# Opis programu: test_bank.py

Program `test_bank.py` jest zestawem testów jednostkowych dla funkcji `value` znajdującej się w module `bank`. Celem tych testów jest weryfikacja, czy funkcja `value` poprawnie klasyfikuje wprowadzone teksty na podstawie określonych zasad.

## Opis funkcjonalności:

1. **Import modułu**:
   - Program importuje funkcję `value` z modułu `bank`:
     ```python
     from bank import value
     ```

2. **Funkcja główna**:
   - `main()` to główna funkcja, która uruchamia wszystkie testy:
     ```python
     def main():
         test_greeting_starts_hello()
         test_greeting_starts_h()
         test_greeting_starts_unique()
     ```

3. **Testy jednostkowe**:
   - Program zawiera trzy funkcje testowe, które sprawdzają różne scenariusze dla funkcji `value`.

   ### 3.1. `test_greeting_starts_hello()`:
   - Sprawdza, czy funkcja `value` zwraca 0 dla tekstów, które zaczynają się od "hello" (i jej wariantów, takich jak "Hello"):
     ```python
     assert value("hello") == 0
     assert value("hello 123") == 0
     assert value("Hello") == 0
     ```

   ### 3.2. `test_greeting_starts_h()`:
   - Sprawdza, czy funkcja zwraca 20 dla tekstów, które zaczynają się od litery "h" (np. "h123", "hey", "hi"):
     ```python
     assert value("h123") == 20
     assert value("hey") == 20
     assert value("hi") == 20
     ```

   ### 3.3. `test_greeting_starts_unique()`:
   - Sprawdza, czy funkcja zwraca 100 dla tekstów, które nie zaczynają się od "hello" ani "h", np. ciągów składających się tylko z liter, cyfr lub znaków specjalnych:
     ```python
     assert value("JHJGF") == 100
     assert value("1234") == 100
     assert value("<>?") == 100
     ```

4. **Uruchomienie testów**:
   - Program uruchamia testy jednostkowe, wywołując funkcję `main()` tylko wtedy, gdy skrypt jest uruchamiany bezpośrednio:
     ```python
     if __name__ == "__main__":
         main()
     ```

## Wykorzystanie:
Program `test_bank.py` jest przydatny do automatycznego testowania funkcji `value` w module `bank`, co zapewnia, że funkcja działa zgodnie z oczekiwaniami i jest odporna na błędy.

