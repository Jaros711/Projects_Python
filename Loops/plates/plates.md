# Opis programu: plates.py

Program `plates.py` ma na celu walidację numerów rejestracyjnych pojazdów w oparciu o określone zasady. Poniżej znajduje się szczegółowy opis funkcji i zasad działania programu.

## Opis funkcjonalności:

1. **Interakcja z użytkownikiem**:
   - Program rozpoczyna się od zapytania użytkownika o wprowadzenie numeru rejestracyjnego:
     ```
     Plate: 
     ```

2. **Walidacja numeru rejestracyjnego**:
   - Po wprowadzeniu numeru rejestracyjnego, program wywołuje funkcję `is_valid(s)`, aby sprawdzić, czy numer spełnia określone zasady.

3. **Zasady walidacji**:
   - **Zasada 1**: Numer rejestracyjny musi zaczynać się od co najmniej dwóch liter.
     - Sprawdzane za pomocą: `if not s[0:2].isalpha():`
   - **Zasada 2**: Długość numeru rejestracyjnego musi wynosić od 2 do 6 znaków.
     - Sprawdzane za pomocą: `if not (2 <= len(s) <= 6):`
   - **Zasada 3**: Cyfry nie mogą znajdować się w środku, muszą być na końcu, a numer nie może zaczynać się od zera.
     - W tym celu program iteruje przez znaki w numerze i sprawdza:
       ```python
       if char.isdigit():
           if not number_found and char == '0':
               return False  # Numbers can't start with '0'
           number_found = True
       elif number_found:
           return False  # No letters allowed after numbers start
       ```
   - **Zasada 4**: Numer rejestracyjny nie może zawierać kropek, spacji ani znaków interpunkcyjnych.
     - Sprawdzane za pomocą: `if not s.isalnum():`

4. **Wynik walidacji**:
   - Jeśli numer rejestracyjny jest poprawny, program wyświetli:
     ```
     Valid
     ```
   - W przeciwnym razie wyświetli:
     ```
     Invalid
     ```

## Wykorzystanie:
Program ten może być użyteczny w różnych systemach rejestracji pojazdów, gdzie wymagane są unikalne i zgodne z regułami numery rejestracyjne.

