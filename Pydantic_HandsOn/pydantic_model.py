from pydantic import BaseModel, Field, field_validator, model_validator, computed_field, EmailStr, conint
from typing import Dict

class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: int = Field(conint(ge=100000, le=999999)

class User(BaseModel):
    user_id : int
    name : str
    email : str
    age : int = Field(ge=18)
    address : Address
    is_premium : bool = False




user_data = {"user_id" : 123, "name": "Guru", "email": "abc@gmail.com", "age": 18, "address": {"city": "Pune", "pincode": 411052}}

user = User(**user_data)

#use model_dump for user_data and store in a single dictionary

print (user)
    