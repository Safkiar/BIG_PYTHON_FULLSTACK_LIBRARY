from pydantic import BaseModel

# Schemas blueprints for data structures 

class ScheduledCourse(BaseModel):
    department: str = "?"
    course_number: int 
    start_date: date = date.today()
    end_date: date 

    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date > self.end_date:
            raise ValueError('Start date must be before end date')
        return self 
    
    ScheduledCourse.model_json_schema()

import json 

print(json.dumps(ScheduledCourse.model_json_schema(), indent=2))

