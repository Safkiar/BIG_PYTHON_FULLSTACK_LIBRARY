# function input int - output int

def function(a:int) -> int:
    return a * 2

# function input float - output float 

def function(a:float) -> float:
    return a * 2.0

# function input list - output list 

def function(lst:list) -> list:
    return lst * 2

# function input dict - output dict 

def function(d:dict) -> dict:
    return d

# function input union int, float - output int, float
def function(a: int|float) -> int|float:
    return a * 2 

