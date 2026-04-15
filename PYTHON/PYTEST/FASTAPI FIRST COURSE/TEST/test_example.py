def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1
# it check if pass as a whole

# instances:
def test_is_instance():
    assert isInstance('this is a string',str)
    assert not isInstance('10',int)

# booleans:
def test_boolean():
    validated = True
    assert validated is True 
    assert ('hello' == 'world') is False 

# types:
def test_type():
    assert type('Hello' is str)
    assert type('World' is not int)

# greater less:
def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10

# validate types 
def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)


import pytest 
class Student:
    def __init__(self, first_name:str, last_name:str,major:str,years:int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major 
        self.years = years

# old way
def test_person_initialization():
    p = Student('John','Doe','Computer Science',3)
    assert p.first_name == 'John', 'First name should be John'
    assert p.last_name == 'Doe', 'Last name should be Doe'
    assert p.major == 'Computer Science'
    assert p.years == 3

# new way
@pytest.fixture
def default_employee():
    return Student('John','Doe','Computer Science',3)

def test_person_initialization(default_employee):
    p = Student('John','Doe','Computer Science',3)
    assert default_employee.first_name == 'John', 'First name should be John'
    assert default_employee.last_name == 'Doe', 'Last name should be Doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3
