# Opis programu: Automat do napojów - coke.py

Program `coke.py` symuluje automat do napojów, który wymaga od użytkownika wprowadzenia monet w celu zakupu napoju. Poniżej znajduje się szczegółowy opis działania programu.

## Opis funkcjonalności:

1. **Kwota do zapłaty**:
   - Program ustala, że całkowita kwota do zapłaty wynosi 50 centów (zmienna `amount_due`).

2. **Akceptowane monety**:
   - Program definiuje listę akceptowanych monet (zmienna `valid_coins`), która obejmuje monety o nominałach: 25, 10 oraz 5 centów.

3. **Pętla do wprowadzania monet**:
   - Program wchodzi w pętlę, która będzie kontynuowana, dopóki `amount_due` jest większe od zera. W każdej iteracji:
     - Wyświetlana jest aktualna kwota do zapłaty.
     - Program prosi użytkownika o wprowadzenie monety.
     - Wprowadzone monety są sprawdzane pod kątem ich ważności:
       - Jeśli moneta jest akceptowalna (tj. znajduje się na liście `valid_coins`), jej wartość jest odejmowana od `amount_due`.
       - Jeśli moneta nie jest ważna, program ignoruje wprowadzenie i kontynuuje.

4. **Obliczanie reszty**:
   - Po zakończeniu pętli, program sprawdza, czy kwota do zapłaty (`amount_due`) jest mniejsza od zera:
     - Jeśli tak, oblicza i wyświetla kwotę reszty, którą automat powinien wydać.
     - Jeśli kwota do zapłaty jest równa zeru, program informuje, że nie ma reszty do wydania.

## Przykład użycia:

1. Użytkownik uruchamia program i wprowadza monety:

Amount Due: 50 Insert Coin: 25 Amount Due: 25 Insert Coin: 10 Amount Due: 15 Insert Coin: 5 Amount Due: 10 Insert Coin: 5 Amount Due: 5 Insert Coin: 25 Change Owed: 20


Program ten stanowi prosty przykład interakcji z użytkownikiem oraz obsługi monet w kontekście automatu do napojów. Może być użyty jako ćwiczenie w programowaniu, aby nauczyć się zarządzania pętlami, warunkami oraz interakcją z użytkownikiem
