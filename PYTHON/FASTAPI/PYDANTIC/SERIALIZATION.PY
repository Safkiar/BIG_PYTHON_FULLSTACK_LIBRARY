from datetime import date 
from pydantic import BaseModel, model_validator 

class ScheduledCourse(BaseModel):
    department: str
    course_number: int
    start_date: date
    end_date: date 

    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date > self.end_date:
            raise ValueError('Start date must be before end date')
        return self 
    
course = ScheduledCourse(
    department="CS",
    course_number=101,
    start_date="2024-01-23",
    end_date="2024-09-23"
)

course.model_dump()

course.mode_dump_json()

course.model_dump_json(exclude={"department","course_number"})

course.model_dump_json(include={"department","course_number"})

class ScheduledCourse(BaseModel):
    department: str = "?"
    course_number: int
    start_date: date
    end_date: date 

    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date > self.end_date:
            raise ValueError('Start date must be before end date')
        return self 
    
course = ScheduledCourse(
    course_number=101,
    end_date="2024-09-23"
)

course.model_duimp_json(exclude_unset=True)