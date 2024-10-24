Opis programu grocery.py

Program grocery.py służy do tworzenia listy zakupów, która zlicza ilości poszczególnych przedmiotów wprowadzonych przez użytkownika. Główne funkcje programu to:

    Zarządzanie listą zakupów:
        Program wykorzystuje słownik (grocery_list), aby przechowywać nazwy przedmiotów oraz ich ilości.
        Użytkownik wprowadza nazwy przedmiotów, a program traktuje je bez względu na wielkość liter (np. "jabłko" i "JABŁKO" są traktowane jako ten sam przedmiot).

    Wprowadzanie danych:
        Program odczytuje wejście od użytkownika w pętli, aż do napotkania końca pliku (EOF).
        Wprowadzone przedmioty są dodawane do słownika. Jeżeli przedmiot już istnieje, jego ilość jest zwiększana o jeden.

    Wyświetlanie wyników:
        Po zakończeniu wprowadzania danych program sortuje listę przedmiotów alfabetycznie i wyświetla ilość każdego przedmiotu w formacie: ilość przedmiot.

Przykładowe użycie

Użytkownik może wprowadzać nazwy produktów jeden po drugim, a następnie zakończyć wprowadzanie, np. poprzez naciśnięcie Ctrl+D (na Unixie) lub Ctrl+Z (na Windowsie), co kończy wprowadzanie danych. Po zakończeniu program wyświetli zaktualizowaną, posortowaną listę zakupów.
Przykład wejścia i wyjścia

Wejście:

jabłko
banan
jabłko
pomarańcza
banan

Wyjście:

2 BANAN
2 JABŁKO
1 POMARAŃCZA

Program grocery.py jest prostym narzędziem do zarządzania listą zakupów, które umożliwia użytkownikom łatwe śledzenie przedmiotów do kupienia.
