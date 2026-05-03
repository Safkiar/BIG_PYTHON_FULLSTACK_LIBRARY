# ==========================================
# PODSTAWOWE FUNKCJE WBUDOWANE W PYTHONIE
# ==========================================

example = 0
l1 = []
l2 = []

abs()
# Zwraca wartość bezwzględną (moduł) liczby. Dla -5 zwróci 5. 
# Fizycznie: odległość na osi liczbowej od zera, bez względu na kierunek.

all()
# Zwraca True (Prawda), jeśli wszystkie elementy w podanym zbiorze (np. liście) 
# są prawdziwe. Jeśli zbiór jest pusty, również zwraca True.

any()
# Zwraca True (Prawda), jeśli przynajmniej jeden element w zbiorze jest prawdziwy.

# ascii()
# Zwraca tekstową (string) reprezentację obiektu, zamieniając znaki 
# spoza alfabetu łacińskiego (np. polskie 'ą', 'ę') na specjalne kody (escape characters).

# bin()
# Zamienia liczbę całkowitą na jej binarną (dwójkową) reprezentację w formie tekstu.

# bool()
# Przekształca wartość na typ logiczny (Prawda lub Fałsz). 
# Zwraca True lub False na podstawie standardowych reguł prawdy w Pythonie.

# breakpoint()
# Zatrzymuje działanie programu w danym miejscu, uruchamiając narzędzie 
# do szukania błędów (debugger). Bardzo przydatne przy diagnozowaniu kodu.

# bytearray()
# Zwraca nową, modyfikowalną tablicę bajtów. Operuje na danych bardzo niskiego poziomu.

# bytes()
# Zwraca nowy, "niezmienny" (immutable) obiekt typu bajtowego. 
# Podobne do bytearray(), ale nie można go potem modyfikować.

# callable()
# Sprawdza, czy dany obiekt można "wywołać" (jak funkcję). Zwraca True lub False.

# chr()
# Przyjmuje liczbę całkowitą (kod Unicode) i zwraca odpowiadający jej znak (np. literę).

# classmethod()
# Służy do tworzenia "metody klasy" w programowaniu obiektowym. 
# Wiąże funkcję z samą klasą, a nie z jej konkretnym egzemplarzem (obiektem).

# compile()
# Kompiluje tekst (kod źródłowy) do obiektu kodu, który może zostać 
# później wykonany przez funkcję exec() lub eval().

# complex()
# Tworzy liczbę zespoloną z części rzeczywistej i urojonej. 
# W fizyce kwantowej i obwodach prądu zmiennego to absolutna podstawa!

# delattr()
# Usuwa podany atrybut (cechę) z konkretnego obiektu.

# dict()
# Tworzy słownik (dictionary), czyli strukturę danych przechowującą 
# informacje w parach "klucz: wartość".

# dir()
# Zwraca listę wszystkich dostępnych właściwości i metod dla danego obiektu. 
# Świetne do sprawdzania, co potrafi dana zmienna lub moduł.

# divmod()
# Przyjmuje dwie liczby i zwraca parę (wynik dzielenia całkowitego, reszta z dzielenia).

# enumerate()
# "Numeruje" elementy zbioru. Przyjmuje np. listę i zwraca pary (indeks, wartość),
# dzięki czemu wiesz, na której pozycji znajduje się dany element.

# eval()
# Wykonuje (oblicza) wyrażenie podane jako tekst (string) tak, jakby to był kod Pythona.

# exec()
# Wykonuje blok kodu Pythona podany w formie tekstu (stringa) lub skompilowanego obiektu.

# filter()
# "Filtruje" dany zbiór elementów za pomocą innej funkcji. Zostawia tylko te elementy, 
# dla których podana funkcja zwraca prawdę (True).

# float()
# Zamienia liczbę całkowitą lub tekst na liczbę zmiennoprzecinkową (ułamkową). 
# Fundamentalne przy precyzyjnych pomiarach fizycznych!

# format()
# Formatuje podaną wartość zgodnie z wybranym wzorcem (np. określenie liczby miejsc po przecinku).

# frozenset()
# Zwraca nowy zbiór (set), którego elementów nie można już po utworzeniu zmieniać ("zamrożony").

# getattr()
# Pobiera wartość konkretnego atrybutu z danego obiektu.

# globals()
# Zwraca słownik reprezentujący wszystkie aktualnie dostępne zmienne globalne w programie.

# hasattr()
# Zwraca True, jeśli dany obiekt posiada podany atrybut (cechę), w przeciwnym razie False.

# hash()
# Zwraca wartość "skrótu" (hash) dla podanego obiektu. Używane wewnątrz Pythona 
# np. do szybkiego wyszukiwania elementów w słownikach.

# help()
# Uruchamia wbudowany system pomocy. Jeśli wpiszesz help(print), 
# Python wyświetli Ci instrukcję obsługi funkcji print.

# hex()
# Zamienia liczbę całkowitą na system szesnastkowy (heksadecymalny) w postaci tekstu.

# id()
# Zwraca unikalny identyfikator podanego obiektu w pamięci komputera. 
# Każda zmienna ma swój własny "adres fizyczny" w pamięci RAM.

# input()
# Czeka, aż użytkownik coś wpisze z klawiatury i zatwierdzi Enterem. Zwraca to jako tekst (string).

# int()
# Zamienia ułamek (odcinając część po przecinku) lub tekst na liczbę całkowitą (integer).

isinstance()
# Sprawdza, czy podany obiekt jest konkretnego typu (np. czy x to liczba całkowita). Zwraca True/False.

# issubclass()
# Sprawdza, czy dana klasa jest "dzieckiem" (podklasą) innej klasy. Związane z programowaniem obiektowym.

# iter()
# Tworzy obiekt "iteratora", co pozwala na przechodzenie (iterowanie) krok po kroku po elementach zbioru.

# len()
# Zwraca liczbę elementów w danym obiekcie (długość listy, liczbę znaków w słowie itp.).

list()
# Tworzy nową listę – podstawową i najbardziej elastyczną strukturę do przechowywania danych w rzędzie.

# locals()
# Zwraca słownik zawierający wszystkie zmienne lokalne w obecnym zasięgu programu.

# map()
# "Mapuje", czyli stosuje podaną funkcję do każdego elementu w wybranym zbiorze (np. liście), 
# tworząc nowy zbiór z wynikami.

max()
# Wybiera i zwraca największą wartość z podanego zbioru (np. z listy liczb).

# memoryview()
# Zwraca specjalny obiekt "widoku pamięci", pozwalający pracować na pamięci bajtów 
# bezpośrednio, bez jej kopiowania. Bardzo zaawansowane.

min()
# Wybiera i zwraca najmniejszą wartość z podanego zbioru.

# next()
# Pobiera kolejny (następny) element z tzw. iteratora.

# object()
# Zwraca nowy, pusty obiekt. Klasa 'object' jest ojcem wszystkich innych klas w Pythonie.

# oct()
# Zamienia liczbę całkowitą na system ósemkowy (oktalny) w postaci tekstu.

# open()
# Otwiera plik na dysku twardym i pozwala na z niego czytać lub do niego pisać (zapisywać wyniki eksperymentu).

# ord()
# Przyjmuje pojedynczy znak tekstu i zwraca jego numer (kod Unicode). Odwrotność funkcji chr().

# pow()
# Potęguje liczbę. pow(x, y) oznacza x podniesione do potęgi y ($x^y$).

# print()
# Wyświetla dane w konsoli. Główne narzędzie komunikacji programu z Tobą.

# property()
# Narzędzie zaawansowane, używane w klasach do zarządzania odczytem i zapisem własności (atrybutów) obiektów.

range()
range(3,10,2)
# Generuje ciąg liczb całkowitych w zadanym przedziale. Często używane do kontrolowania pętli (powtórzeń).

# repr()
# Zwraca "oficjalną" tekstową reprezentację obiektu, przydatną głównie dla programistów przy szukaniu błędów.

# reversed()
# Odwraca kolejność elementów w danym zbiorze (np. liście).

# round()
# Zaokrągla podaną liczbę do określonej liczby miejsc po przecinku. Bardzo ważne przy podawaniu błędów pomiarowych!

# set()
# Tworzy "zbiór" matematyczny, w którym każdy element jest unikalny (nie ma powtórzeń).

# setattr()
# Ustawia wartość danego atrybutu (cechy) w konkretnym obiekcie.

# slice()
# Tworzy obiekt "wycinka". Używane, gdy chcemy "odciąć" i pobrać tylko konkretny fragment z listy czy tekstu.

sorted()
sorted(example,reverse=True)
# Przyjmuje jakiś zbiór, układa jego elementy w kolejności (np. rosnąco) i zwraca jako nową listę.

# staticmethod()
# Tworzy metodę statyczną w programowaniu obiektowym – funkcja, która "żyje" wewnątrz klasy, ale nie wymaga tworzenia jej obiektu.

str()
# Przekształca wartość na tekst (string). Np. ze zmiennej liczbowej robi ciąg znaków, który można wyświetlić.

sum()
# Sumuje ze sobą wszystkie elementy w podanym zbiorze (np. dodaje do siebie wszystkie liczby w liście). Wartość $\Sigma$.

# super()
# Zwraca obiekt reprezentujący klasę nadrzędną. Używane w skomplikowanych hierarchiach programowania obiektowego.

# tuple()
# Tworzy "krotkę" (tuple), czyli strukturę podobną do listy, ale niezmienną po jej utworzeniu (immutable).

type()
# Zwraca "typ" obiektu, czyli informuje, czy dana zmienna to tekst, liczba całkowita, czy np. lista.

# vars()
# Zwraca specjalny atrybut '__dict__' modułu, klasy czy obiektu (czyli wszystko to, co ten obiekt zawiera).

zip()
list(zip(l1,l2))
for a,b in zip(l1,l2):
    pass
# Bierze kilka list i "zszywa" je ze sobą (jak suwak), tworząc z nich pary. Z pierwszej listy bierze element pierwszy, 
# z drugiej też pierwszy i łączy je ze sobą, i tak dalej.

# __import__()
# Niskopoziomowa, zaawansowana funkcja używana "pod maską" przez instrukcję 'import'. 
# Służy do dołączania zewnętrznych bibliotek (modułów) do programu.