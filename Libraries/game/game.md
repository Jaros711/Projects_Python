# Opis programu: Gra w Zgadywanie Liczb

Program `Gra w Zgadywanie Liczb` to interaktywna gra, w której użytkownik stara się odgadnąć losowo wybraną liczbę. Gra zapewnia proste instrukcje i informuje gracza, czy jego zgadywana liczba jest za duża, za mała, czy też idealnie pasuje.

## Opis funkcjonalności:

1. **Importowanie biblioteki**:
   - Program korzysta z biblioteki `random`, która umożliwia generowanie losowych liczb.

2. **Pobieranie wartości poziomu**:
   - Program wchodzi w pętlę, w której prosi użytkownika o podanie wartości poziomu, co reprezentuje górną granicę dla losowanej liczby.
   - Użytkownik musi wprowadzić liczbę całkowitą większą niż 0.
   - Jeśli użytkownik wprowadzi wartość nieprawidłową (np. tekst lub liczbę mniejszą niż 1), program będzie ponownie prosił o poprawne wprowadzenie.

3. **Generowanie losowej liczby**:
   - Po uzyskaniu prawidłowej wartości, program generuje losową liczbę w zakresie od 1 do podanej wartości (włącznie).

4. **Zgadywanie liczby**:
   - Program przechodzi do kolejnej pętli, w której użytkownik jest proszony o wprowadzenie zgadywanej liczby.
   - Użytkownik może wprowadzać tylko liczby całkowite większe od 0.
   - Program sprawdza, czy zgadnięcie jest:
     - **Zbyt duże**: Jeśli zgadywana liczba jest większa niż losowa liczba, wyświetla komunikat "Too large!".
     - **Zbyt małe**: Jeśli zgadywana liczba jest mniejsza, wyświetla komunikat "Too small!".
     - **Poprawne**: Jeśli zgadywana liczba jest równa losowej liczbie, wyświetla komunikat "Just right!" i kończy działanie.

## Przykład użycia:

1. Użytkownik uruchamia program:

Level: 10 Guess: 5 Too small! Guess: 8 Too large! Guess: 7 Just right!


Program ten jest świetnym sposobem na zabawę i doskonalenie umiejętności zgadywania, a także na naukę obsługi błędów w wprowadzaniu danych.
