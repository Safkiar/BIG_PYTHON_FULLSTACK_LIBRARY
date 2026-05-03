'''
Cannot change item oraz add a functionality.
Can be indexed.
parentheses are optional

ordered and immmutable containers of elements
'''

num_tuple = (1,2,3,4,5)



# ==========================================
# WBUDOWANE METODY DLA KROTEK (TUPLE)
# Użycie: zmienna_krotkowa.metoda()
# ==========================================

# pomiary = (12.5, 13.0, 12.5, 14.1) - nasz układ o stałej masie i strukturze

# count(element)
# Pełni funkcję licznika Geigera dla konkretnej wartości. 
# Przeszukuje całą krotkę i zwraca dokładną liczbę wystąpień podanego elementu.
# Np. pomiary.count(12.5) zwróci wynik 2, ponieważ to napięcie występuje dwa razy.

# index(element)
# Pełni funkcję radaru pozycyjnego. Zwraca indeks (położenie liczone od zera) 
# pierwszego napotkanego elementu o podanej wartości.
# Np. pomiary.index(13.0) zwróci 1, ponieważ wartość 13.0 znajduje się na drugiej pozycji w krotce.