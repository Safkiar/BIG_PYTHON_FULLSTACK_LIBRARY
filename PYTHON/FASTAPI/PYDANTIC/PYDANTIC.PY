# data modeling library, data parsing, error handling

#  define data models, validation 

#GOOD FOR:

# DECLARATIVE DEFINITIONS OF DATA MODELS AND CONSTRAINTS 
# ENSURING INCOMING AND OUTGOING DATA ADHERES TO MODEL DEFINITIONS AND CONSTRAINTS
# AUTOMATIC GENERATION OF DOCUMENTATION, EASY INTEGRATION WITH TYPE CHECKERS, HIGHER CODE CLARITY
# EASILY CONVERT MODELS TO AND FROM VARIUS FORMATS LIKE JSON, YAML, XML, ETC.

# 1. DEFINE DATA MODEL, PYTHON CLASS THAT INHERITS FROM BASEMODEL
# 2. CREATE INSTANCES OF THAT MODEL BY PASSING DATA TO THE MODEL CONSTRUCTOR (SERIALIZE)
# 3. ONCE INSTANTIED, MANIPULATE THE ATTRIBUTES JUST LIKE ANY OTHER PYTHON OBJECT
# 4. OPTIONALLY, DESERIALIZE THE DATA OBJECT BACK OUT ACCORDING TO BUSINESS LOGIC

# BASEMODEL = Automatic validation, types, error handling,  serialization 
# !pip install pydantic==2.5.3
import pydantic
print(pydantic.VERSION)
from pydantic import BaseModel 

class User(BaseModel):
    name: str 
    age: int 
    email: str 

# that disables automatic converting to class
    class Config:
        strict = True 

# pydantic tries to convert the data to specific type 
int("25")
# succeed

try:
    user = User(name="John Doe", age=25,email="pony@gmail.com")
except pydantic.ValidationError as e:
    print(e)

from pydantic import StrictInt 

class User(BaseModel):
    name:str
    age: StrictInt # this turn off automatic converting
    email: str 

from pydantic import Field, EmailStr 

class User(BaseModel):
    name:str = Field(min_length=5, max_length=50)
    age: StrictInt = Field(ge=18,le=120) #greater than 18 and less than 120
    email: EmailStr 

# pip install pydantic[email]
# pip install email-validation=2.1.0