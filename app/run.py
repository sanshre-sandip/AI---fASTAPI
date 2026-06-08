from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int



def insert_data(student: Student):

    print(student.name)
    print(student.age)
    print('done')    

student_info = {'name': 'Sandip', 'age': 30}

patient1 = Student(**student_info)

insert_data(patient1)


