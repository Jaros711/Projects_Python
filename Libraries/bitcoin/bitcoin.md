# Opis programu: bitcoin

Program `bitcoin` służy do obliczania wartości w dolarach amerykańskich określonej ilości bitcoinów na podstawie aktualnego kursu rynkowego pobranego z API serwisu Coindesk.

## Opis funkcjonalności:

1. **Importowanie bibliotek**:
   - Program korzysta z bibliotek: 
     - `requests` do wykonywania żądań HTTP,
     - `sys` do obsługi argumentów wiersza poleceń,
     - `json` do przetwarzania danych w formacie JSON.

2. **Sprawdzanie argumentów wiersza poleceń**:
   - Program oczekuje jednego argumentu (ilości bitcoinów) podczas uruchamiania.
   - Jeżeli liczba argumentów nie wynosi 2, program wyświetla komunikat o błędzie: `Missing command-line argument` i kończy działanie.
   - Program próbuje przekonwertować podany argument na typ `float`. Jeśli konwersja się nie powiedzie (np. gdy użytkownik poda tekst), wyświetli komunikat: `Command-line argument is not a number` i kończy działanie.

3. **Pobieranie aktualnej ceny bitcoina**:
   - Program wysyła zapytanie GET do API Coindesk (`https://api.coindesk.com/v1/bpi/currentprice.json`) w celu uzyskania aktualnej ceny bitcoina w dolarach amerykańskich.
   - Odpowiedź API jest parsowana jako JSON, a aktualna cena bitcoina (w USD) jest wyciągana z odpowiedzi.

4. **Obliczanie wartości bitcoinów**:
   - Program oblicza wartość w dolarach amerykańskich ilości bitcoinów podanej jako argument wiersza poleceń, mnożąc wartość bitcoina przez ilość bitcoinów.
   - Wynik jest formatowany do czterech miejsc po przecinku i wyświetlany w formacie `$X.XXXX`.

5. **Obsługa błędów**:
   - Program obsługuje wyjątki związane z żądaniami HTTP. Jeśli wystąpi błąd (np. problem z połączeniem), program wyświetli komunikat `RequestException` i zakończy działanie.

## Przykład użycia:

- Uruchomienie programu w terminalu:
python bitcoin.py 2.5
