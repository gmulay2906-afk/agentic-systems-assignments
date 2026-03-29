from pydantic import BaseModel, Field, field_validator, model_validator, computed_field, EmailStr
from typing import Dict

class Address(BaseModel):
    city : str = Field(min_length=3)
    pincode : int #= Field(max_length=6)

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(str(value)) != 6:
            raise ValueError("Pincode should be exact 6 digit value")
        return value

class User(BaseModel):
    user_id : int
    name : str
    email : str
    age : int = Field(ge=18)
    address : Address
    is_premium : bool = False




user_data = {"user_id" : 123, "name": "Guru", "email": "abc@gmail.com", "age": 18, "address": {"city": "Pune", "pincode": 411057}}

user = User(**user_data)

#use model_dump for user_data and store in a single dictionary

print (user.address.pincode)
    