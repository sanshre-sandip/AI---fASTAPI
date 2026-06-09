from pydantic import BaseModel, EmailStr, AnyUrl, Field                             

#pydantic provides the custom datatype like EmailStr AnyUrl
from typing import List,TypedDict, Optional, Dict
class Student(BaseModel):
    name: str
    age: int = Field(gt=0)
    relation: Optional[Dict[str, str]] = None
    email: Optional[EmailStr] = None
    url: Optional[AnyUrl] = None




def insert_data(student: Student):

    print(student.name)
    print(student.age)
    print('done')    

def update_data(student: Student):

    print(student.name)
    print(student.age)
    print(student.relation)
    print(student.email)
    print(student.url)
    print('done') 

student_info = {
    "name": "Sandip",
    "age": 1,
    
}

patient1 = Student(**student_info)
update_data(patient1)

#insert_data(patient1)


#pydantic provides the custom datatype like EmailStr AnyUrl




