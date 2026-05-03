'''
Sets are collection of data which are unordered and cannot contain duplications
Index do not work 


'''
s = {1,2}
element = 3
num_set = {1,2,3,4,5}
inny_zbior = (2,3)

# discard index element by value
num_set.discard(1)

# empty set
num_set.clear()

# add element to a set
num_set.add(6)

# add multiple values to a set
num_set.update([7,8])




# ==========================================
# WBUDOWANE METODY DLA ZBIORÓW (SET)
# Użycie: zmienna_zbiorowa.metoda()
# ==========================================

# A = {1, 2, 3}, B = {3, 4, 5}

s.add(element)
# Iniekcja pojedynczej cząstki. Jeśli element już istnieje, zbiór 
# nie ulegnie zmianie (zasada unikalności).

# clear()
# Całkowite opróżnienie układu. Wynik: set().

# copy()
# Tworzy kopię zapasową układu (płytka kopia).

s.difference(inny_zbior)
# Oblicza różnicę $A \setminus B$. Zwraca NOWY zbiór z elementami, 
# które są w A, ale nie ma ich w B.

# difference_update(inny_zbior)
# Moduł destrukcyjny. Usuwa z oryginalnego zbioru A wszystkie elementy 
# występujące w zbiorze B. Zmienia układ "w miejscu".

s.discard(element)
# Usuwa podany element, jeśli istnieje. Jeśli go nie ma – nic nie robi 
# (bezpieczniejsza wersja remove(), nie rzuca błędu).

s.intersection(inny_zbior)
# Szuka części wspólnej $A \cap B$. Zwraca NOWY zbiór z elementami 
# obecnymi w obu układach.

# intersection_update(inny_zbior)
# Ogranicza oryginalny zbiór tylko do elementów wspólnych z innym zbiorem.

# isdisjoint(inny_zbior)
# Sprawdza, czy zbiory są rozłączne ($A \cap B = \emptyset$). 
# Zwraca True, jeśli nie mają żadnych wspólnych elementów.

# issubset(inny_zbior)
# Sprawdza, czy zbiór jest podzbiorem innego ($A \subseteq B$).

# issuperset(inny_zbior)
# Sprawdza, czy zbiór zawiera w sobie inny zbiór ($A \supseteq B$).

# pop()
# Usuwa i zwraca LOSOWY element ze zbioru. Ze względu na brak 
# uporządkowania, nie wiemy, która "cząstka" zostanie usunięta.

# remove(element)
# Usuwa konkretny element. Jeśli elementu nie ma w zbiorze – rzuca błąd (KeyError).

# symmetric_difference(inny_zbior)
# Zwraca NOWY zbiór z elementami, które są w A LUB w B, 
# ale NIE w obu naraz (suma bez części wspólnej).

# symmetric_difference_update(inny_zbior)
# Aktualizuje zbiór, zostawiając w nim tylko elementy z symetrycznej różnicy.

s.union(inny_zbior)
# Suma zbiorów $A \cup B$. Zwraca NOWY zbiór zawierający wszystkie 
# elementy z obu układów (bez duplikatów).

# update(inny_zbior)
# Fuzja układów. Dodaje wszystkie elementy z innego zbioru do 
# obecnego zbioru (modyfikacja w miejscu).