Program: Interpreter

Program ten przyjmuje wyrażenie arytmetyczne w formacie "operand1 operator operand2" i oblicza jego wartość. Obsługuje podstawowe operacje matematyczne, takie jak dodawanie, odejmowanie, mnożenie i dzielenie.

Opis działania:

    Pobranie wyrażenia: Użytkownik jest proszony o podanie wyrażenia arytmetycznego w formacie "operand1 operator operand2". Program dzieli tę linię na trzy części: dwa operandy i operator.

    Konwersja operandu: Operandy są konwertowane na liczby całkowite.

    Wykonanie operacji: Program sprawdza operator i wykonuje odpowiednią operację:
        + — dodawanie
        - — odejmowanie
        * — mnożenie
        / — dzielenie

    Zwracanie wyniku: Wynik jest zaokrąglany do jednego miejsca po przecinku i zwracany jako liczba zmiennoprzecinkowa.

Przykład użycia: Enter an arithmetic expression (e.g., '1 + 1'): 3 + 4 7.0

Enter an arithmetic expression (e.g., '1 + 1'): 10 - 2 8.0

Enter an arithmetic expression (e.g., '1 + 1'): 6 / 3 2.0

Technologie:

    Python 3.x

Instrukcje uruchamiania: Uruchom program w terminalu: python3 nazwa_pro
