Program: Meal

Program ten przyjmuje czas w formacie 24-godzinnym i informuje użytkownika, czy jest czas na śniadanie, lunch czy kolację.

Opis działania:

    Pobranie czasu: Użytkownik jest proszony o podanie czasu w formacie 24-godzinnym (##:##).

    Konwersja czasu: Program dzieli czas na godziny i minuty, a następnie konwertuje go na wartość zmiennoprzecinkową, gdzie godziny są reprezentowane w pełnych godzinach i minutach.

    Sprawdzenie czasu posiłków: Program określa, czy podany czas mieści się w przedziałach:
        Śniadanie: 7:00 - 8:00
        Lunch: 12:00 - 13:00
        Kolacja: 18:00 - 19:00

Przykład użycia: What is the time (in 24h format ##:##): 07:30 breakfast time

What is the time (in 24h format ##:##): 12:15 lunch time

What is the time (in 24h format ##:##): 18:45 dinner time

Technologie:

    Python 3.x

Instrukcje uruchamiania: Uruchom program w terminalu: python3 nazwa_programu.py
