from pydantic import BaseModel  ,field_validator,Field
from typing import List,Dict

class StudentCreate(BaseModel):

    name: str = Field(..., max_length=50,min_length=1)
    experienceyears: int
    skills: List[str]
    has_degree: bool


    @field_validator('experienceyears')
    @classmethod
    def validate_experienceyears(cls,value):
        if value<=0:
            raise ValueError("The candidate should have some experience")
        return value

    @field_validator('skills')
    @classmethod
    def validate_skills(cls,value):
        if not value:
            raise ValueError("The candidate should have some experience")
        return value


def validate_and_score_resumes(data: List):
    valid_items=[]
    results=[]
    print (data)
    print ("--------------------------------")
    for item in data:
        try:
            print (item)
            print ("+++++++++++++++++++++++++++++++")
            validated= StudentCreate(**item)
            print (validated)
            valid_items.append(validated)
            print (valid_items)
        except ValueError:
            print (item, "not a valid candidate")
        
    for item in valid_items:
        base_score=10*item.experienceyears
        skill_points= len(item.skills)*5
        if item.has_degree:
            score=base_score + skill_points+20
        score=base_score+skill_points
        results.append((item.name,score))

    results.sort(key=lambda x:x[1],reverse=True)
    return results

data=[
    {'name': 'Alice', 'experienceyears': 5, 'skills': ['Python', 'SQL'], 'has_degree': True},
    {'name': 'Bob', 'experienceyears': -1, 'skills': ['Java'], 'has_degree': False},
    {'name': 'Carol', 'experienceyears': 3, 'skills': [], 'has_degree': False},
    {'name': 'Dave', 'experienceyears': 7, 'skills': ['Python', 'ML', 'SQL'], 'has_degree': False},
]
res=validate_and_score_resumes(data)
print(res)