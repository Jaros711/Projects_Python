Program: Extensions

Program ten prosi użytkownika o podanie nazwy pliku i zwraca typ MIME na podstawie rozszerzenia pliku. Umożliwia to szybkie rozpoznawanie formatu pliku, co jest przydatne w różnych aplikacjach.

Opis działania:

    Pobranie nazwy pliku: Użytkownik jest proszony o podanie nazwy pliku. Odpowiedź jest przetwarzana, aby usunąć nadmiarowe białe znaki i przekształcić tekst na małe litery.

    Sprawdzenie rozszerzenia: Program analizuje rozszerzenie pliku i zwraca odpowiedni typ MIME:
        .jpg i .jpeg zwracają image/jpeg
        .gif zwraca image/gif
        .png zwraca image/png
        .pdf zwraca application/pdf
        .txt zwraca text/plain
        .zip zwraca application/zip
        W przypadku nieznanego rozszerzenia program zwraca application/octet-stream.

Przykład użycia: Write the name of file: image.jpg image/jpeg

Write the name of file: document.pdf application/pdf

Write the name of file: archive.zip application/zip

Technologie:

    Python 3.x

Instrukcje uruchamiania: Uruchom program w terminalu: python3 nazwa_programu.py
