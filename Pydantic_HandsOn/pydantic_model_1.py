from pydantic import BaseModel, ValidationError, Field, field_validator, model_validator, computed_field


class StudentMarks(BaseModel):
    name: str
    marks: int = Field(..., ge=0, le=100)

    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('Name must not be empty')
        return value

    @model_validator(mode='after')
    def check_marks(cls, values):
        marks = values.get('marks')
        if marks is not None and (marks < 0 or marks > 100):
            raise ValueError('Marks must be between 0 and 100')
        return values

    @computed_field
    def grade(self) -> str:
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'