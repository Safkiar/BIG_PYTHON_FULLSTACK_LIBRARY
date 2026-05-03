'''
Lists are a collection of data
Ordered sequences of elements 
each element has an index starting at 0

'''

num_list = [1,2,3,4,5]
str_list = ["Abc","Def","Ghi"]
dict_list = {"key":1}
l = []
element = 1
indeks = 0

# takes the first value "1" 
num_list[0]

# takes the last value "5"
num_list[-1]

# takes first value and ends at specified point  "1,2"
num_list[0:2]

'''
List comprehension
'''
[x for x in num_list]
[x**2 for x in num_list]
[x for x in num_list if x % 2 == 1]
[x for x in dict_list if x.get('key')  >= 10]

# ==========================================
# WBUDOWANE METODY DLA LIST (LIST)
# Użycie: zmienna_listowa.metoda()
# ==========================================

# x = [10, 20, 30] - nasz początkowy układ

l.append(element)
# Dodaje pojedynczy, nowy element na sam koniec listy. 
# Zwiększa długość układu o 1. Np. x.append(40) da nam [10, 20, 30, 40].

# clear()
# Całkowita anihilacja danych. Usuwa wszystkie elementy z listy, 
# zostawiając pusty układ: [].

# copy()
# Zwraca płytką kopię (shallow copy) listy. Ważne w fizyce/programowaniu: 
# jeśli chcesz poeksperymentować na danych, zrób kopię, aby nie zniszczyć 
# oryginalnych wyników bazowych!

# count(element)
# Działa jak detektor cząstek. Zlicza i zwraca informację o tym, 
# ile razy dokładnie taki sam element występuje w naszym układzie.

# extend(inny_zbior)
# Fuzja dwóch układów. W przeciwieństwie do append(), nie dodaje całej 
# listy jako jednego elementu, ale wyciąga z niej cząstki i dołącza je 
# po kolei na koniec naszej listy.

# index(element)
# Sonda pozycjonująca. Szuka podanego elementu i zwraca jego indeks 
# (współrzędną położenia na liście). Uwaga: zwraca tylko pierwsze trafienie. 
# Jeśli elementu nie ma, wyrzuca błąd.

# insert(indeks, element)
# Precyzyjna iniekcja. Wstawia podany element dokładnie we wskazane 
# miejsce (indeks), przesuwając resztę elementów w prawo (wymusza 
# relokację cząstek, co kosztuje czas procesora).

"".join(element)
# join elements of the list with the item between breackets

l.pop(indeks)
l.pop(-1)
# Ekstrakcja cząstki. Usuwa element z podanego indeksu i ZWRACA go nam 
# (możemy go przypisać do innej zmiennej). Jeśli nie podasz indeksu, 
# domyślnie "odrywa" i zwraca ostatni element (najsłabiej związany z układem).

l.remove(element)
# Usuwa pierwsze wystąpienie konkretnej WARTOŚCI z listy. 
# W przeciwieństwie do pop(), musisz wiedzieć co usuwasz, a nie gdzie to jest.

# reverse()
# Modyfikacja wektora czasu. Odwraca kolejność wszystkich elementów 
# na liście (ostatni staje się pierwszym). Zmienia układ "w miejscu".

# sort()
# Uporządkowanie entropii układu. Sortuje elementy na liście 
# (domyślnie od najmniejszego do największego). Działa "w miejscu". 
# Można dodać parametr (reverse=True), aby posortować malejąco.