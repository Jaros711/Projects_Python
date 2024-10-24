Ten plik README.md opisuje przypadki testowe dla funkcji is_valid() z modułu plates.py. Testy te mają na celu sprawdzenie poprawności logiki, która weryfikuje poprawność tablic rejestracyjnych na podstawie określonych zasad.
Opis funkcjonalności

Funkcja is_valid(s) sprawdza, czy tablica rejestracyjna jest poprawna, na podstawie następujących zasad:

    Zasada długości: Tablica musi mieć od 2 do 6 znaków.
    Zasada początkowa: Tablica musi zaczynać się od co najmniej dwóch liter.
    Zasada numerów: Jeśli występują cyfry, nie mogą znajdować się w środku, muszą być na końcu, a pierwsza cyfra nie może być 0.
    Zasada znaków specjalnych: Tablica nie może zawierać kropek, spacji ani znaków interpunkcyjnych.

Funkcje testujące
1. test_min_and_max()

Ta funkcja sprawdza, czy długość tablicy spełnia wymóg posiadania od 2 do 6 znaków.

    Przypadki poprawne:
        'AA': Minimalna dopuszczalna długość (2 znaki).
        'ABCDEF': Maksymalna dopuszczalna długość (6 znaków).
    Przypadki niepoprawne:
        'A': Zbyt krótka (1 znak).
        'ABCDEFGH': Zbyt długa (8 znaków).

2. test_start_two_letters()

Ta funkcja sprawdza, czy tablica zaczyna się od co najmniej dwóch liter.

    Przypadki poprawne:
        'AA': Zaczyna się od dwóch liter.
    Przypadki niepoprawne:
        'A2': Tylko jedna litera na początku.
        '2A': Zaczyna się od cyfry.
        '22': Brak liter.

3. test_middle()

Ta funkcja sprawdza, czy liczby nie są umieszczone w środku tablicy. Liczby muszą być na końcu.

    Przypadki poprawne:
        'AAA222': Wszystkie liczby na końcu.
    Przypadki niepoprawne:
        'AAA22A': Litera po liczbach.

4. test_first()

Ta funkcja sprawdza, czy pierwsza cyfra w tablicy nie jest 0.

    Przypadki poprawne:
        'CS50': Liczby na końcu, brak 0 na początku.
    Przypadki niepoprawne:
        'CS05': Liczba zaczyna się od 0.

5. test_special()

Ta funkcja sprawdza, czy tablica nie zawiera znaków specjalnych, takich jak kropki, spacje czy inne znaki interpunkcyjne.

    Przypadki niepoprawne:
        'PI3.14': Zawiera kropkę.
        'PI!@#': Zawiera znaki interpunkcyjne.
        'PI ! @#': Zawiera spacje i znaki interpunkcyjne.
