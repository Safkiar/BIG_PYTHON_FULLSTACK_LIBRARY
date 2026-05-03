'''
mutable and unordered
access with [] or .get() 
no value [] produce error, get not
'''



example_dictionary = {
    'string':'string',
    'num': 10,
}

d={"klucz":"wartosść"}
d['nowy klucz'] = 'nowość'

# get value from dictionary
example_dictionary.get("string")

# add value to dictionary
example_dictionary["new value"] = True

# remove value from dictionary
example_dictionary.pop('num')

# clear all values fom dictionary
example_dictionary.clear()

# delete entirely dictionary
del example_dictionary

# Copied value dic = dic2 
# values from dic2 will be also altered in dic

# Copy dictionary
clone_dictionary = new_dictionary.copy()



# ==========================================
# WBUDOWANE METODY DLA SŁOWNIKÓW (DICT)
# Użycie: zmienna_slownikowa.metoda()
# ==========================================

# mars = {"nazwa": "Mars", "g": 3.71, "ksiezyce": 2}

# clear()
# Całkowite czyszczenie bazy danych. Słownik staje się pusty: {}.

# copy()
# Tworzy kopię bezpieczeństwa słownika. Bardzo ważne, gdy chcemy 
# zmieniać parametry układu bez modyfikacji danych źródłowych.

# fromkeys(sekwencja, wartosc)
# Metoda statyczna. Tworzy nowy słownik na podstawie listy kluczy, 
# przypisując każdemu tę samą, podaną wartość początkową.

d.get(klucz)
# Bezpieczny odczyt. Szuka wartości dla klucza. Jeśli go nie ma, 
# nie wyrzuca błędu (jak zwykłe []), lecz zwraca None lub 
# podaną wartość domyślną. Jak czujnik, który zamiast się psuć, 
# zwraca zero przy braku sygnału.

d.items()
# Zwraca widok wszystkich par (klucz, wartosc) jako krotki. 
# Pozwala "przejrzeć" całą zawartość szafy archiwalnej.

d.keys()
# Zwraca listę (widok) wszystkich etykiet (kluczy) w słowniku. 
# Informuje nas, jakie "wymiary" mierzymy w danym obiekcie.

d.pop(klucz)
# Usuwa parę o podanym kluczu i ZWRACA jej wartość. 
# Jeśli klucza nie ma – zwraca wartość domyślną lub rzuca błąd.

# popitem()
# Usuwa i zwraca OSTATNIĄ dodaną parę (klucz, wartosc) w formacie krotki. 
# Działa zgodnie z zasadą LIFO (Last In, First Out) od wersji Python 3.7.

# setdefault(klucz, domyslna)
# Próbuje pobrać wartość. Jeśli klucz nie istnieje, dodaje go 
# do słownika z podaną wartością domyślną.

# update(inny_slownik)
# Aktualizacja bazy danych. Nadpisuje istniejące klucze wartościami 
# z nowego słownika i dodaje te, których wcześniej nie było. 
# To jak synchronizacja danych z dwóch różnych czujników.

d.values()
# Zwraca widok wszystkich wartości przechowywanych w słowniku, 
# ignorując ich klucze (etykiety).