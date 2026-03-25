'''
Isolates code and do only certains aspect of it when
this functionallity is called
'''

def func():
    pass

def func2(arg):
    print(f"This is argument: {arg}")

value = "This value is outside"
def func3():
    value = "This vallue will be called inside"
    print(value)
print(value) # This value is outside

def func4(first, second):
    pass
func4(second=1,first=2)

def func5(cost):
    return cost + tax(cost)
def func6(cost):
    tax = .03
    return cost * tax