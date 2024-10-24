# Opis programu: Gra w Matematyczne Dodawanie

Program `Gra w Matematyczne Dodawanie` to edukacyjna gra, która ma na celu poprawę umiejętności dodawania dla różnych poziomów trudności. Użytkownik będzie miał za zadanie rozwiązanie dziesięciu równań matematycznych, a za każdą poprawną odpowiedź przyznawany będzie punkt.

## Opis funkcjonalności:

1. **Importowanie biblioteki**:
   - Program korzysta z biblioteki `random`, aby generować losowe liczby w różnych zakresach.

2. **Stałe dla poziomów**:
   - Program definiuje trzy poziomy trudności:
     - **Poziom 1**: zakres od 0 do 9
     - **Poziom 2**: zakres od 10 do 99
     - **Poziom 3**: zakres od 100 do 999

3. **Słownik zakresów**:
   - `RANGES` to słownik, który przechowuje zakresy dla każdego z poziomów trudności.

4. **Główna funkcja**:
   - `main()`: wywołuje funkcje do uzyskania poziomu oraz symulacji quizu, a następnie wyświetla uzyskany wynik.

5. **Uzyskiwanie poziomu**:
   - `get_level()`: funkcja ta prosi użytkownika o wprowadzenie poziomu trudności.
   - Użytkownik musi wprowadzić wartość od 1 do 3. W przypadku wprowadzenia nieprawidłowej wartości (np. tekstu lub liczby spoza zakresu) program będzie ponownie prosił o poprawne wprowadzenie.

6. **Generowanie liczb całkowitych**:
   - `generate_integer(level)`: funkcja generuje dwie losowe liczby całkowite w zależności od wybranego poziomu trudności, korzystając z zdefiniowanych zakresów.

7. **Rozwiązywanie równań**:
   - `solve_equation(x, y)`: funkcja ta wyświetla równanie w formie "x + y = ?" i prosi użytkownika o wprowadzenie odpowiedzi.
   - Użytkownik ma trzy próby na udzielenie poprawnej odpowiedzi. W przypadku niepoprawnej odpowiedzi lub błędnego wprowadzenia (np. tekstu) program wyświetli komunikat "EEE".
   - Po trzech nieudanych próbach program pokaże prawidłową odpowiedź.

8. **Symulacja quizu**:
   - `simulate(level)`: funkcja ta generuje 10 problemów matematycznych. Jeśli użytkownik rozwiąże zadanie poprawnie, jego wynik wzrasta o jeden punkt.

9. **Wywołanie głównej funkcji**:
   - Na końcu, jeśli program jest uruchamiany jako główny, wywoływana jest funkcja `main()`.

## Przykład użycia:

1. Użytkownik uruchamia program:

Level: 1 3 + 4 = 7 (poprawna odpowiedź) 2 + 5 = 8 (niepoprawna odpowiedź, 3 próby) 1 + 1 = 2 (poprawna odpowiedź) ... Score: 3 (wynik końcowy)


Program ten jest doskonałym narzędziem edukacyjnym dla uczniów i wszystkich, którzy chcą poprawić swoje umiejętności w zakresie dodawania.
