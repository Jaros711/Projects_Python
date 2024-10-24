# Opis programu: twttr.py

Program `twttr.py` ma na celu przetwarzanie tekstu wprowadzoną przez użytkownika, usuwając z niego wszystkie samogłoski. Jest to inspiracja do tworzenia krótszych, bardziej zwięzłych wiadomości, podobnych do tych, które mogą być używane na platformach społecznościowych, takich jak Twitter.

## Opis funkcjonalności:

1. **Interakcja z użytkownikiem**:
   - Program rozpoczyna się od zapytania użytkownika o wprowadzenie tekstu:
     ```
     Input: 
     ```

2. **Usuwanie samogłosk**:
   - Po wprowadzeniu tekstu przez użytkownika, program wywołuje funkcję `remove_vowels(text)`, aby usunąć wszystkie samogłoski z wprowadzonego tekstu.

3. **Zasady usuwania samogłosk**:
   - Funkcja `remove_vowels(text)` definiuje zbiór samogłosk, które mają być usunięte. Obejmuje zarówno małe, jak i wielkie litery:
     ```python
     vowels = "aeiouAEIOU"
     ```
   - Program tworzy pusty ciąg `result`, do którego będą dodawane wszystkie znaki z tekstu, które nie są samogłoskami.
   - W pętli program sprawdza każdy znak w wprowadzonym tekście:
     ```python
     for char in text:
         if char not in vowels:
             result += char
     ```

4. **Wynik**:
   - Po przetworzeniu tekstu, program wyświetla wynik bez samogłosk:
     ```
     Output: [wynik bez samogłosk]
     ```

## Wykorzystanie:
Program ten może być użyty do tworzenia zwięzłych wiadomości lub jako część większego projektu przetwarzania tekstu, gdzie istnieje potrzeba redukcji długości tekstu poprzez usunięcie samogłosk.

