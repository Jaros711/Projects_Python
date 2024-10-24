# Opis programu: outdated

Program `outdated` jest narzędziem służącym do konwertowania dat w dwóch formatach: `MM/DD/YYYY` oraz `Month Day, Year`. Celem programu jest ułatwienie użytkownikowi wprowadzania dat i ich konwersji do standardowego formatu `YYYY-MM-DD`.

## Funkcje:

1. **Słownik miesięcy**:
   Program definiuje słownik `months`, który przypisuje angielskie nazwy miesięcy do ich dwucyfrowych wartości (np. "January" → "01").

2. **Wprowadzanie danych**:
   Użytkownik jest proszony o wprowadzenie daty, która może być podana w jednym z dwóch akceptowanych formatów. Program działa w pętli, co umożliwia wprowadzenie wielu dat.

3. **Walidacja formatu `MM/DD/YYYY`**:
   - Gdy wprowadzona data zawiera znak `/`, program dzieli ją na miesiąc, dzień i rok.
   - Sprawdza, czy miesiąc jest w zakresie od 1 do 12, dzień w zakresie od 1 do 31, a rok jest liczbą dodatnią.
   - Jeśli wszystkie warunki są spełnione, program zwraca datę w formacie `YYYY-MM-DD`.

4. **Walidacja formatu `Month Day, Year`**:
   - W przypadku formatu `Month Day, Year`, program usuwa przecinki i dzieli tekst na części.
   - Weryfikuje poprawność miesiąca, dnia oraz roku, upewniając się, że oryginalny ciąg zawiera przecinek.
   - Po pomyślnej walidacji program konwertuje datę do formatu `YYYY-MM-DD`.

5. **Obsługa błędów**:
   W przypadku błędnego formatu daty program informuje użytkownika o problemie i prosi o ponowne wprowadzenie daty.

## Przykłady użycia:

- **Wejście**: `02/15/2023`
  - **Wyjście**: `2023-02-15`

- **Wejście**: `February 15, 2023`
  - **Wyjście**: `2023-02-15`

Program `outdated` jest prostym i efektywnym narzędziem do konwersji dat, które zapewnia użytkownikom elastyczność w podawaniu dat w różnych formatach.

