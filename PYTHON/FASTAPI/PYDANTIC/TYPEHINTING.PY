from datetime import date 
# 2024-01-01

import pydantic
from pydantic import BaseModel 

class Event(BaseModel):
    event_date: date 

try:
    event = Event(event_date="2024-03-03")
except pydantic.ValidationError as e:
    print(e)

from datetime import time 

class Event(BaseModel):
    event_date: date
    event_time: time 

try: 
    event = Event(event_date="2024-03-03", event_time="14:30:00")
except pydantic.ValidationError as e:
    print(e)


from datetime import datetime 

class Appointment(BaseModel):
    start_time: datetime 

try: 
    appt = Appointment(start_time =datetime.now())
except pydantic.ValidationError as e:
    print(e)

appt.start_time 


# LIST !!!!!!!!!!! ORDER COLLECTION OF ITEMS
[2,4,6]
[x for x in range(1,11) if x % 2 == 0]''

from typing import List
class ShoppingList(BaseModel):
    items: List[str]

try:
    shopping_list = ShoppingList(items=['apple','banana'])
    print(shopping_list)
except pydantic.ValidationError as e:
    print(e)

from pydantic import Field 
class ShoppingList(BaseModel):
    items: List[str] = Field(max_items=5, min_items=2)

class Matrix(BaseModel):
    grid: List[List[int]]

try:
    matrix = Matrix(grid=[[1,2,3],[3,4,9]])
    print(matrix)
except pydantic.ValidationError as e:
    print(e)

class Ingedient(BaseModel):
    name: str
    quantity: float

class Repice(BaseModel):
    ingredients: List[Ingedient]

try:
    recipe = Repice(ingredients=[
        Ingedient(name="salt",quantity=0.3),
        Ingedient(name="pepper",quantity=0.6)
    ])
    print(recipe)
except pydantic.ValidationError as e:
    print(e)

# DICTIONARIES 

from pydantic import BaseModel 
from typing import Dict 

class UserProfiles(BaseModel):
    profiles: Dict[str,int] 

try:
    user_profiles = UserProfiles(profiles={"alice":25,"bob":25})
except pydantic.ValidationError as e:
    print(e)

len(user_profiles.profiles)

from pydantic import Field
class UserProfiles(BaseModel):
    profiles: Dict[str,int] = Field(min_items=2)

class Product(BaseModel):
    name: str
    price: float 

class ProductCatalog(BaseModel):
    products: Dict[str, Product]

try:
    catalog = ProductCatalog(
        products={
            'pl': Product(name='tea',price=4.99)
            'p2': {"name":"pasta","price":13.09}
        }
    )
except pydantic.ValidationError as e:
    print(e)

class Order(BaseModel):
    product_id: str
    quantity: int 

class OrderBook(BaseModel):
    products: Dict[str,Dict[str,Order]]

order_book = OrderBook(
    orders={
        "o1":Order{product_id:"A1",quantity=2}
    }
)

# SETS

set(), tuple()

from pydantic import BaseModel, Field, ValidationError
from typing import Set

class UniqueNumbers(BaseModel):
    values: Set[int] = Field(max_items=10,min_items=2)

try:
    unique_numbers = UniqueNumbers(values={1,2,3,4,"4"})
    print(unique_numbers)
except ValidationError as e:
    print(e)

from typing import Tuple

class Coordinates(BaseModel):
    point: Tuple[float,float,float]
coordinates = Coordinates(point=(1.0,2.0,3.0))

print(coordinates)

class UserInfo(BaseModel):
    details: Tuple[int,str,bool]
user_info = UserInfo(details=(42,"Answer",True))

class GroceryList(BaseModel):
    details: Tuple[str, ...]
GroceryList(items=("apples",))


# UNIONS

from pydantic import BaseModel

class Car(BaseModel):
    make: str
    model: str 
    seat_count: int

class Motorcycle(BaseModel):
    make: str 
    model: str 
    has_sidecar: bool 

class Truck(BaseModel):
    make:str 
    model: str 
    payload_capacity: float 

from typing import Union

class Vehicle(BaseModel):
    owner: str 
    vehicle_details: Union[Car, Motorcycle,Truck]

Vehicle(owner="Alice",vehicle_details=Car(make="Tesla",model="S",seat_count=5))