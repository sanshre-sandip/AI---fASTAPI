from pydantic import BaseModel


class Address(BaseModel):
    name: str


class Detail(BaseModel):
    user: str
    grade: int
    address: Address


def check(detail: Detail):
    print(detail.user)
    print(detail.grade)
    print(detail.address)
    print(detail.address.name)
aaa = {
        "name": "Kathmandu"
    }
address1 = Address(**aaa)
data = {
    "user": "Sandip",
    "grade": 12,
    "address": address1
}

student = Detail(**data)

check(student)