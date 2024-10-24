# Opis programu: faces

Program `faces` konwertuje tekstowe reprezentacje emotikonów na odpowiadające im graficzne emotikony. Użytkownik może wprowadzić tekst, a program zamienia w nim wszystkie wystąpienia uśmiechniętych i smutnych twarzy w formie tekstowej na ich graficzne odpowiedniki.

## Funkcje:

1. **Funkcja `convert(text)`**:
   - Przyjmuje łańcuch tekstowy jako argument.
   - Zastępuje wystąpienia ':)' graficzną emotikoną uśmiechu (🙂).
   - Zastępuje wystąpienia ':(' graficzną emotikoną smutku (🙁).
   - Zwraca przetworzony łańcuch tekstowy.

2. **Funkcja `main()`**:
   - Prosi użytkownika o wprowadzenie łańcucha tekstowego.
   - Wywołuje funkcję `convert()` w celu przetworzenia tekstu.
   - Wyświetla wynik z zamienionymi emotikonami.

## Przykład użycia:

- **Wejście**: `Enter a string: Hello there! :) How are you? :(`
- **Wyjście**: `Hello there! 🙂 How are you? 🙁`

Program `faces` jest prostym narzędziem do wzbogacenia komunikacji tekstowej o graficzne emocje, co czyni ją bardziej wyrazistą i atrakcyjną wizualnie.

