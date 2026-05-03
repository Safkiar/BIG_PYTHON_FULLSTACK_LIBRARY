"""
sequences of characters with letter, number, symbol, punctuation
"" or ''
combined with +
repeated with *
"""

# ==========================================
# WBUDOWANE METODY DLA ŁAŃCUCHÓW ZNAKÓW (STR)
# Użycie: zmienna_tekstowa.metoda()
# ==========================================

# x = "moje laboratorium fizyczne"

# capitalize()
# Zmienia pierwszą literę całego tekstu na wielką, a resztę na małe.
# Np. "moje laboratorium" -> "Moje laboratorium"

# casefold()
# Agresywna wersja zamiany na małe litery. Używana głównie do porównywania 
# tekstów z różnych języków (np. niemieckie 'ß' zamienia na 'ss').

# center(szerokosc)
# Wyśrodkowuje tekst w nowym łańcuchu o podanej szerokości, wypełniając boki spacjami.

# count(szukany_fragment)
# Działa jak detektor. Liczy, ile razy podany fragment tekstu występuje w całości.

# encode()
# Koduje tekst do postaci surowych bajtów (domyślnie w standardzie UTF-8).

# endswith(fragment)
# Zwraca True (Prawda), jeśli tekst kończy się dokładnie podanym fragmentem.

# expandtabs(rozmiar)
# Zamienia wszystkie znaki tabulacji (Taby, czyli '\t') na odpowiednią liczbę spacji.

# find(fragment)
# Szuka fragmentu i zwraca indeks (pozycję) pierwszego wystąpienia. 
# Jeśli nie znajdzie, zwraca -1 (brak sygnału).

# format()
# Potężne narzędzie do wstawiania zmiennych w konkretne miejsca w tekście 
# oznaczone klamrami {}. Np. "Wynik to {} J".format(5) -> "Wynik to 5 J".

# format_map(slownik)
# Podobne do format(), ale pobiera wartości do wstawienia bezpośrednio ze słownika.

# index(fragment)
# Działa identycznie jak find(), ale jeśli nie znajdzie szukanego fragmentu, 
# powoduje błąd programu (awarię) zamiast zwracać -1.

# isalnum()
# Zwraca True, jeśli tekst składa się TYLKO z liter i cyfr (bez spacji i znaków specjalnych).

# isalpha()
# Zwraca True, jeśli tekst składa się TYLKO z liter alfabetu.

# isascii()
# Zwraca True, jeśli wszystkie znaki w tekście należą do standardowego kodu ASCII.

# isdecimal()
# Zwraca True, jeśli wszystkie znaki są cyframi dziesiętnymi (0-9).

# isdigit()
# Zwraca True, jeśli znaki są cyframi (obsługuje też małe cyfry w indeksach, np. '²').

# isidentifier()
# Zwraca True, jeśli tekst jest prawidłową nazwą zmiennej w Pythonie 
# (nie zaczyna się od cyfry, nie ma spacji itp.).

# islower()
# Zwraca True, jeśli wszystkie litery w tekście są małe.

# isnumeric()
# Zwraca True, jeśli znaki reprezentują wartości liczbowe (nawet ułamki zapisane jednym znakiem jak '½').

# isprintable()
# Zwraca True, jeśli wszystkie znaki można wydrukować (np. ukryte znaki nowej linii '\n' zwrócą False).

# isspace()
# Zwraca True, jeśli tekst składa się WYŁĄCZNIE z tzw. białych znaków (spacje, taby, enter).

# istitle()
# Zwraca True, jeśli każde słowo w tekście zaczyna się wielką literą.

# isupper()
# Zwraca True, jeśli wszystkie litery w tekście są wielkie.

# join(zbior_elementow)
# Używa naszego tekstu jako "kleju" do połączenia elementów z innej listy.
# Np. "-".join(["A", "B", "C"]) stworzy nowy tekst "A-B-C".

# ljust(szerokosc)
# Dosuwa tekst do lewej strony w ramach podanej szerokości, wypełniając prawą stronę spacjami.

# lower()
# Transformuje cały tekst na małe litery.

# lstrip()
# Przycina (usuwa) wszystkie białe znaki (spacje) znajdujące się po LEWEJ stronie tekstu.

# maketrans() i translate()
# Tworzy tabelę mapowania, a następnie tłumaczy znaki według tej tabeli. 
# Mechanizm podobny do prostej maszyny szyfrującej Enigma.

# partition(separator)
# Rozbija tekst na trzy części wokół pierwszego znalezionego separatora 
# i zwraca krotkę: (lewa_czesc, separator, prawa_czesc).

# removeprefix(prefiks)
# Usuwa podany fragment z początku tekstu (jeśli tam jest).

# removesuffix(sufiks)
# Usuwa podany fragment z końca tekstu (jeśli tam jest).

# replace(stary_fragment, nowy_fragment)
# Zastępuje wszystkie wystąpienia starego fragmentu nowym w całym tekście.

# rfind(fragment) / rindex(fragment)
# Działa jak find() i index(), ale szuka od PRAWEJ strony (od końca tekstu).

# rjust(szerokosc)
# Dosuwa tekst do prawej strony, wypełniając lewą stronę spacjami.

# rpartition(separator)
# Działa jak partition(), ale szuka separatora od PRAWEJ strony tekstu.

# rsplit()
# Działa jak split(), ale zaczyna rozdzielać słowa od prawej strony (istotne przy ograniczeniu liczby podziałów).

# rstrip()
# Przycina (usuwa) wszystkie białe znaki z PRAWEJ strony (z końca) tekstu.

# split(separator)
# Niezwykle ważna metoda! Rozbija cały tekst na kawałki (np. słowa) w miejscach, 
# gdzie występuje separator (domyślnie spacja), i zwraca je jako Listę.

# splitlines()
# Rozbija tekst wielolinijkowy na Listę, gdzie każdym elementem jest jedna linijka.

# startswith(fragment)
# Zwraca True, jeśli tekst zaczyna się dokładnie od podanego fragmentu.

# strip()
# Usuwa wszelkie białe znaki (spacje, taby, entery) z OBU stron tekstu naraz (z lewej i z prawej).

# swapcase()
# Odwraca wielkość liter: małe stają się wielkimi, a wielkie małymi.

# title()
# Zmienia pierwszą literę KAŻDEGO słowa w tekście na wielką.

# upper()
# Transformuje cały tekst na wielkie litery. Zwiększa "stan energetyczny" liter na maksimum.

# zfill(szerokosc)
# Wypełnia tekst zerami (0) z lewej strony, aż osiągnie podaną szerokość. 
# Bardzo przydatne przy formatowaniu wyników liczbowych, np. "42" -> "00042".