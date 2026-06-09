from pydantic import BaseModel, AnyUrl, EmailStr, Field, model_validator
from typing import Dict, Optional


class Variables(BaseModel):
    name: str
    age: int
    relation: Optional[Dict[str, str]] = None
    email: Optional[EmailStr] = None
    url: Optional[AnyUrl] = None
    contact: Dict[str, str]

    @model_validator(mode="after")
    def validate(self):
        if self.age > 30 and "emer" not in self.contact:
            raise ValueError("contact detail needed you are too old")
        return self


def insert_data(variable: Variables):
    print(variable.contact)
    print("done")


data = {
    "name": "Sandip",
    "age": 30,
    "email": "sandpipe989@tech.com",
    
}

ready = Variables(**data)

insert_data(ready)