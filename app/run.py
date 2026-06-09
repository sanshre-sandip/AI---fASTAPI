from pydantic import BaseModel, EmailStr, AnyUrl, Field , field_validator                            

#pydantic provides the custom datatype like EmailStr AnyUrl Field
# we can add metadat using Field in any field using ----->  Annotated
from typing import List,TypedDict, Optional, Dict, Annotated
class Student(BaseModel):
    name: str
    age: int = Field(gt=0)
    relation: Optional[Dict[str, str]] = None
    email: Optional[EmailStr] = None
    url: Optional[AnyUrl] = None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_email = ['aasiii.com', 'tech.com']
        domain = value.split('@')[-1]

        if domain not in valid_email:
            raise ValueError('Not vallid')
        
        return value

    


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
    "email": "sandpipe989@tech.com"
    
}

patient1 = Student(**student_info)
update_data(patient1)

#insert_data(patient1)


#pydantic provides the custom datatype like EmailStr AnyUrl




