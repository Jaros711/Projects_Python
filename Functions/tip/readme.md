# Opis programu: tip

Program `tip` oblicza wysokość napiwku na podstawie kosztu posiłku oraz procentu napiwku, który użytkownik chce zostawić.

## Funkcje:

1. **Pobieranie danych**:
   - Program prosi użytkownika o wprowadzenie kwoty za posiłek za pomocą komunikatu: `How much was the meal?`.
   - Następnie prosi o wprowadzenie procentu napiwku za pomocą komunikatu: `What percentage would you like to tip?`.

2. **Konwersja dolarów**:
   - Funkcja `dollars_to_float` przekształca wprowadzoną kwotę, usuwając znak `$` i zwracając wartość jako liczbę zmiennoprzecinkową (float).

3. **Konwersja procentów**:
   - Funkcja `percent_to_float` przekształca wprowadzony procent, usuwając znak `%` i zwracając wartość jako liczbę zmiennoprzecinkową (float) w postaci ułamka.

4. **Obliczenie napiwku**:
   - Program oblicza napiwek mnożąc kwotę posiłku przez procent napiwku, a następnie wyświetla wynik w formacie: `Leave $<napiwek>` z dwoma miejscami po przecinku.

## Przykład użycia:

- **Wejście**: 
  - `How much was the meal? $50`
  - `What percentage would you like to tip? 20%`
  
- **Wyjście**: 
  - `Leave $10.00`

Program `tip` jest prostym narzędziem, które ułatwia obliczanie napiwków w restauracji.

