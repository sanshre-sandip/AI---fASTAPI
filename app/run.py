from pydantic import BaseModel
from typing import List,TypedDict, Optional, Dict
class Student(BaseModel):
    name: str
    age: int
    relation: Optional[Dict[str, str]] = None




def insert_data(student: Student):

    print(student.name)
    print(student.age)
    print('done')    

def update_data(student: Student):

    print(student.name)
    print(student.age)
    print(student.relation)
    print('done') 

student_info = {
    "name": "Sandip",
    "age": 30,
    
}

patient1 = Student(**student_info)
update_data(patient1)

insert_data(patient1)


