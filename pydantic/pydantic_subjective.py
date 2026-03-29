from pydantic import BaseModel, Field, field_validator, model_validator, computed_field, EmailStr
from typing import Dict

class Address(BaseModel):
    city : str = Field(min_length=3)
    pincode : int = Field(length=6)

class User(BaseModel):
    user_id : int
    name : str
    email : str
    age : int = Field(ge=18)
    address : Address
    is_premium : bool = False

user_data = {
    'user_id' : 1,
    'name' : 'Chirag',
    'email' : 'abc@gmaul.com',
    'age' : 20,
    'address' : {
        'city' : 'New York',
        'pincode' : 10001
    }
}

user = User(**user_data)
print(user)

print(user.model_dump)