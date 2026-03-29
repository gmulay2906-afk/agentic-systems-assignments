from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing import Dict

class Student(BaseModel):
    name: str = Field(max_length=50, description="Provide the name of the student")
    email: EmailStr = Field(description="Provide a valid email of the student", examples=['abc@gmail.com'])
    age: int = Field(gt=0, le=100)
    college: str = None
    marks: float = Field(default = 10.0)
    emergency_contact_number: Dict[str, int]

    # This field validator is used to validate if email belongs to masai.com or not. 
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        # abc@masai.com
        domain_name = value.split('@')[-1]  # ['abc', 'masai.com'] 

        if domain_name != 'masai.com':
            raise ValueError('Not a valid domain for email.')

        return value

    @field_validator('college')
    @classmethod
    def transform_college_name_to_upper_case(cls, value):
        return value.lower()
    
    # default value of mode is `after`.
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if value < 0 and value > 100:
            raise ValueError("Invalid age provided.")
        
        return value
    
    @model_validator(mode='after')
    @classmethod
    def validate_contact_number(cls, model):
        if model.age < 18 and 'fathers' not in model.emergency_contact_number:
            raise ValueError('If age of student is less than 18 then fathers contact number is mandatory')
        
        return model

    @computed_field
    @property
    def percentage(self) -> float:
        return self.marks;

    @model_validator(mode='after')
    @classmethod
    def validate_percentage(cls, model):
        if model.percentage < 0 or model.percentage > 100:
            raise ValueError('Percentage should be between 0 to 100')

        return model

    
student_info = {'name' : 'Chirag', 'college' : 'MASAI', 'email' : 'abc@masai.com', 'age' : '20', 'emergency_contact_number' : {'friends' : 7656373}, 'marks' : 89,
                'name' : 'Chirag', 'college' : 'MASAI', 'email' : 'efg@masai.com', 'age' : '22', 'emergency_contact_number' : {'friends' : 7656333}, 'marks' : 56}

#using this student_info dict, create the Student object. 
# ** -> unpacking. 
student = Student(**student_info)

print(student.email)