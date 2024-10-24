# Opis programu: figlet

Program `figlet` generuje tekst w stylu ASCII art z wykorzystaniem różnych czcionek, umożliwiając użytkownikom stylizowanie wprowadzonego tekstu w kreatywny sposób.

## Opis funkcjonalności:

1. **Importowanie bibliotek**:
   - Program wykorzystuje bibliotekę `pyfiglet`, która pozwala na generowanie tekstu w formacie ASCII.
   - Biblioteki `sys` i `random` służą do obsługi argumentów wiersza poleceń oraz losowego wyboru czcionki.

2. **Definiowanie funkcji `main`**:
   - Funkcja `main` zawiera główną logikę działania programu.
   - Tworzy obiekt `Figlet`, który jest używany do generowania stylizowanego tekstu.

3. **Sprawdzanie argumentów wiersza poleceń**:
   - Program sprawdza liczbę argumentów przekazanych w wierszu poleceń:
     - **Brak argumentów**: Jeśli żaden argument nie został podany, program losuje czcionkę z dostępnych czcionek.
     - **Dwa argumenty**: Program oczekuje, że pierwszym argumentem będzie `-f` lub `--font`, a drugim nazwą czcionki.
       - Jeśli podana czcionka nie jest dostępna, program kończy działanie z komunikatem "Invalid usage".

4. **Ustawianie czcionki**:
   - Wybrana czcionka jest ustawiana na obiekcie `Figlet`.

5. **Wprowadzanie tekstu**:
   - Program prosi użytkownika o wprowadzenie tekstu, który ma być przekształcony w styl ASCII.

6. **Generowanie i wyświetlanie wyniku**:
   - Program generuje stylizowany tekst za pomocą metody `renderText` i drukuje go na ekranie.

## Przykład użycia:

- Użytkownik uruchamia program bez argumentów: 

python figlet.py Enter text: Hello, World!


- Program losowo wybiera czcionkę i wyświetla przekształcony tekst.

- Użytkownik uruchamia program z argumentami: 

python figlet.py -f slant Enter text: Hello, World!


- Program używa czcionki "slant" do stylizacji tekstu i wyświetla wynik.

Program ten jest przydatny do kreatywnego prezentowania tekstu w formie ASCII art w różnych stylach czcionek
