from pydantic import BaseModel, AnyUrl, EmailStr, Field, model_validator, computed_field
from typing import Dict, Optional
import os


class Variables(BaseModel):
    name: str
    weight: float
    age: int
    height: float
    relation: Optional[Dict[str, str]] = None
    email: Optional[EmailStr] = None
    url: Optional[AnyUrl] = None
    

    @computed_field
    @property
    def compute(self) -> float:
        bmi = round(self.weight/(self.height**2),3)
        return bmi



def insert_data(variable: Variables):
    
    print(variable.compute)
    print("done")


data = {
    "name": "Sandip",
    "age": 30,
    "height": 5.6,
    "weight": 100.1,
    "email": "sandpipe989@tech.com",
    
}

ready = Variables(**data)

insert_data(ready)