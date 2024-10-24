# Opis programu: taqueria

Program `taqueria` jest interaktywnym narzędziem do zamawiania potraw z menu taquerii. Użytkownik może wprowadzać nazwy potraw, a program oblicza całkowity koszt zamówienia na podstawie cen ustalonych w słowniku. Program działa w pętli, umożliwiając dodawanie wielu pozycji do zamówienia.

## Funkcje:

1. **Słownik menu**:
   Program definiuje słownik `menu`, który zawiera różne potrawy dostępne w taquerii oraz ich ceny. Przykładowe potrawy to:
   - Baja Taco: $4.25
   - Burrito: $7.50
   - Bowl: $8.50
   - Nachos: $11.00
   - Quesadilla: $8.50

2. **Wprowadzanie danych**:
   Użytkownik jest proszony o wprowadzenie nazwy potrawy. Program odczytuje dane wejściowe i usuwa nadmiarowe białe znaki.

3. **Normalizacja wejścia**:
   Wprowadzone dane są przetwarzane na format "title case" (pierwsza litera każdego wyrazu jest wielka), co ułatwia porównanie z kluczami w słowniku menu.

4. **Sprawdzanie dostępności potrawy**:
   - Program sprawdza, czy wprowadzona potrawa znajduje się w menu.
   - Jeśli tak, dodaje jej cenę do łącznego kosztu zamówienia.
   - W przypadku nieprawidłowej nazwy potrawy, użytkownik jest informowany i zachęcany do spróbowania ponownie (tylko jeśli dane wejściowe nie są puste).

5. **Wyświetlanie całkowitego kosztu**:
   Program wyświetla całkowity koszt zamówienia, sformatowany do dwóch miejsc po przecinku.

6. **Obsługa błędów**:
   Program jest zaprojektowany do wykrywania sytuacji EOF (end-of-file) i odpowiednio kończy działanie, zapewniając estetyczne wyjście.

## Przykłady użycia:

- **Wejście**: `Baja Taco`
  - **Wyjście**: `Total: $4.25`

- **Wejście**: `Burrito`
  - **Wyjście**: `Total: $11.75`

- **Wejście**: `Pizza`
  - **Wyjście**: `Item not on the menu, please try again.`

Program `taqueria` jest prostym, ale skutecznym narzędziem do śledzenia zamówień w taquerii, które pozwala użytkownikom na interaktywne dodawanie potraw do swojego zamówienia i obliczanie całkowitego kosztu.

