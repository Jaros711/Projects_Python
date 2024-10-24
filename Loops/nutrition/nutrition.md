# Opis programu: Nutrition - nutrition.py

Program `nutrition.py` służy do informowania użytkownika o liczbie kalorii zawartych w różnych owocach. Poniżej znajduje się szczegółowy opis działania programu.

## Opis funkcjonalności:

1. **Słownik kalorii owoców**:
   - Program definiuje słownik `fruit_calories`, w którym kluczem jest nazwa owocu (w formacie małych liter), a wartością jest liczba kalorii zawartych w danym owocu. Przykłady zawartości słownika:
     - "apple": 130
     - "banana": 110
     - "orange": 80

2. **Interakcja z użytkownikiem**:
   - Program prosi użytkownika o podanie nazwy owocu. Wprowadzone dane są przetwarzane: 
     - Usuwane są zbędne spacje (metoda `strip()`) oraz konwertowana jest nazwa do formatu małych liter (metoda `lower()`).

3. **Sprawdzenie obecności owocu w słowniku**:
   - Program sprawdza, czy wprowadzony przez użytkownika owoc znajduje się w słowniku `fruit_calories`.
   - Jeśli owoc jest w słowniku, program wyświetla liczbę kalorii przypisaną do tego owocu.

4. **Wyjście**:
   - W przypadku owoców, które nie znajdują się w słowniku, program nie wyświetla żadnych dodatkowych komunikatów.

## Przykład użycia:

1. Użytkownik uruchamia program i wprowadza owoc:

Enter a fruit: apple Calories: 130


2. Użytkownik może również wpisać owoc w innej formie:

Enter a fruit: Banana Calories: 110


Program `nutrition.py` jest prostym narzędziem, które może być użyteczne dla osób chcących kontrolować kaloryczność swojej diety, a także służy jako przykład zastosowania słowników oraz interakcji z użytkownikiem w Pythonie.
