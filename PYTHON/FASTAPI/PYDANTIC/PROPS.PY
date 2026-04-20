from pydantic import BaseModel, ValidationError 
from typing import Optional
import pydantic

class User(BaseModel):
    name: str 
    age: Optional[int] = None 

try:
    user1 = User(name="Alice")
    print(user1.age)
except ValidationError as e:
    print(e)

User(name="Alice", age=None)

from typing import Any 

class Mnemonic(BaseModel):
    requiredIntQuantity: int 
    optionalIntQuantity: int = 10 #optional
    optionalIntQuantityNullable: Optional[int] = 10 
    optionalAnyTypeQuantity: Any = 10

# UUID: Universally unique identiefers

import uuid 

print(uuid.uuid4())

class User(BaseModel):
    id: uuid.UUID 
    name: str

try:
    user = User(id=uuid.uuid4(), name="Allison")
    print(user)
except pydantic.ValidationError as e:
    print(e)

from pydantic import Field 

class User(BaseModel):
    id: uuid.UUID = Field(default_factory=lambda:uuid.uuid4())
    name: str 

User(name="Billy")

#  IMMUTABLES
# - data integrity - accidental or unauthorized modification
# - predictable 
# - conurrent programing 

from pydantic import BaseModel, ValidationError
class User(BaseModel):
    name: str
    age: int 

    class Config:
        frozen = True 

try: 
    user = User(name="Alice",age=30)
    user.name="BILLY"
    # not gonna work - frozen
except:
    pydantic.ValidationError as e:
    print(e)

from pydantic import ConfigDict
class User(BaseModel):
    model_config: ConfigDict = {"frozen":True}
    name: str
    age: int 


class User(BaseModel):
    id: int = Field(frozen=True)
    name: str
    age: int 

    class Config:
        frozen = True 
        extra = "ignore" # base
        extra = "forbid" # no additional fields

# ENUMS
# set of named constants 
from enum import Enum 

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

Color.GREEN 

class Item(BaseModel):
    name:str
    color: Color  # must be inside that class

item = Item(name="chair",color="red")


# LITERALS
from typing import Literal 

Literal["a","b"]

class ItemWithLiteral(BaseModel):
    name: str
    color: Literal["red","green","blue"]

item = ItemWithLiteral(name="Chair","grey")

from pydantic import TypeAdapter 
literal = Literal["red","green,"blue]

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

lit_adapter = TypeAdapter(literal)
enum_adapter = TypeAdapter(Color)

from timeit import timeit 

res1 = timeit(lambda: lit_adapter.validate_python("red"), number = 100)