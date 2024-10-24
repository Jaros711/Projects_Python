Opis programu

Program ten pozwala użytkownikowi na wprowadzenie ułamka w formacie x/y, gdzie x to licznik, a y to mianownik. Główne funkcje programu to:

    fraction():
        Wymaga od użytkownika podania ułamka.
        Sprawdza, czy podane wartości są liczbami całkowitymi.
        Upewnia się, że licznik (x) nie jest większy od mianownika (y).
        Obsługuje błędy, takie jak podanie niepoprawnych wartości lub zera jako mianownika, i prosi o ponowne wprowadzenie.

    fraction_to_percent(numerator, denominator):
        Konwertuje podany ułamek na procent.
        Zwraca wynik w postaci liczby całkowitej, zaokrąglając do najbliższej wartości.

Po uzyskaniu wartości ułamka, program konwertuje go na procent i wyświetla wynik:

    Jeżeli wynik jest mniejszy lub równy 1%, program wyświetla "E".
    Jeżeli wynik wynosi 99% lub więcej, program wyświetla "F".
    W przeciwnym razie, program wyświetla wartość procentową.

Program został zaprojektowany w celu zachowania prostoty i użyteczności, zapewniając jednocześnie solidne sprawdzenie błędów wprowadzania danych przez użytkownika.
