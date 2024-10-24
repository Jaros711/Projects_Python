# Opis programu: adieu

Program `adieu` służy do zbierania imion od użytkownika i wyświetlania ich w formie grzecznościowej po wpisaniu polecenia zakończenia.

## Opis funkcjonalności:

1. **Import biblioteki**:
   - Program korzysta z biblioteki `inflect`, która pozwala na tworzenie zrozumiałych dla użytkownika form zdań i tekstów, szczególnie w kontekście listowania elementów.

2. **Tworzenie listy**:
   - Program inicjalizuje pustą listę `name_list`, w której będą przechowywane wprowadzone imiona.

3. **Pętla wejścia użytkownika**:
   - W nieskończonej pętli program prosi użytkownika o wprowadzenie imienia za pomocą komunikatu: `Name: `.
   - Wprowadzone imię dodawane jest do listy `name_list`.

4. **Obsługa zakończenia**:
   - Program wykrywa sytuację, w której użytkownik wprowadza polecenie zakończenia (np. `CTRL+D`), co kończy pętlę.
   - Po wykryciu zakończenia, program wyświetla pustą linię dla lepszego formatowania.

5. **Wyświetlanie wyników**:
   - Program używa funkcji `p.join(name_list)` z biblioteki `inflect`, aby poprawnie sformułować listę imion w naturalny sposób.
   - Na końcu program wyświetla komunikat w formacie: `Adieu, adieu, to <lista imion>`.

## Przykład użycia:

- **Wejście**:
  - `Name: Alice`
  - `Name: Bob`
  - `Name: Charlie`
  - `CTRL+D`

- **Wyjście**:
  - `Adieu, adieu, to Alice, Bob, and Charlie.`

Program `adieu` jest prostym, ale efektywnym narzędziem do interakcji z użytkownikiem, umożliwiającym zbieranie danych i prezentację ich w przyjazny sposób.

