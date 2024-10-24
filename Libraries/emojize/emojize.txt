# Opis programu: emojize

Program `emojize` umożliwia użytkownikowi zamianę tekstowych aliasów emotikonów na ich graficzne reprezentacje.

## Opis funkcjonalności:

1. **Import biblioteki `emoji`**:
   - Program korzysta z biblioteki `emoji`, która zawiera funkcje do konwersji tekstu na emotikony.

2. **Definiowanie funkcji `main`**:
   - Program rozpoczyna się od zdefiniowania funkcji `main`, która jest odpowiedzialna za główną logikę działania programu.
   - Użytkownik jest proszony o wprowadzenie tekstu, który może zawierać aliasy emotikonów (np. `:smile:`).

3. **Konwersja za pomocą `emoji.emojize`**:
   - Wprowadzone dane są przekazywane do funkcji `emoji.emojize`, która zamienia tekstowe aliasy na odpowiednie emotikony.
   - Użycie argumentu `language='alias'` zapewnia, że zamiana będzie oparta na aliasach.

4. **Wyświetlanie wyniku**:
   - Program drukuje wynik na ekranie, pokazując zamieniony tekst z emotikonami.

## Przykład użycia:

- Użytkownik wprowadza: `I love :smile: and :pizza:!`
- Program zwraca: `I love 😄 and 🍕!`

Program ten jest użyteczny dla osób, które chcą wzbogacić swoje wiadomości o emotikony przy użyciu prostych aliasów.

