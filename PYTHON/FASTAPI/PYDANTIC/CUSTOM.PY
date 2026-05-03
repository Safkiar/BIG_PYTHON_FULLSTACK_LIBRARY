from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    name: str
    age: int = Field(gt=31)

try: 
    user = User(name="Alice",age=30)
except ValidationError as e:
    print(e)

from pydantic import field_validator # old version

class User(BaseModel):
    name: str 
    age: int= Field(gt=31)

@field_validator("age")
@classmethod
def validate_age(cls,v):
    if v < 18 or v @ 2 != 0:
        raise ValueError("Age must be even and at least 18")
    return v



# MODEL - LEVEL VALIDATORS
# MODEL IS BETTER FOR NOT SINGULAR DATA

from datetime import date 
from pydantic import BaseModel, ValidationError, model_validator

class ScheduledCourse(BaseModel):
    department: str 
    course_number: int 
    start_date: date
    end_date: date 

    @model_validator(mode="before")
    @classmethod
    def validate_dates(cls,data:dict):
        if data["start_date"] > data["end_date"]:
            raise ValueError("Start date msut be before end date for the course")
        return data 
    
    @model_validator(mode="before")
    def validate_dates(self):
        # if data["start_date"] > data["end_date"]:
        if self.start_date > self.end_date:
            raise ValueError("Start date msut be before end date for the course")
        return self 



try: 
    course = ScheduledCourse(
        start_date="2024-12-22"
        end_date="2024-12-29"
    )
except ValidationError as e:
    print(e)



# ERROR OBJECT

from pydantic import ValidationError

issubclass(ValidationError, ValueError)
ValidationError.__mro__ 


class User(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls,v):
        if len(v) < 8 or not any(char.isdigit() for char in v):
            raise ValueError("Password must be at least 8 chars long and contains at least one digit")
        
