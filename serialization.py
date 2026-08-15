from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str = 'male'
    age: int
    address: Address


address_dict = {
    'city': 'DGK',
    'state': 'Punjab',
    'pin': '32000'
}

patient_dict = {
    'name': 'Khan',
    'age': 21,
    'address': address_dict
}

patient1 = Patient(**patient_dict)

##By using serialization we can convert our python in to dict and json format

temp = patient1.model_dump(include=['name','age'])
print(temp)
print(type(temp))


temp1 = patient1.model_dump_json()
print(temp1)
print(type(temp1))


temp2 = patient1.model_dump(exclude={'address':['pin']})
print(temp2)
print(type(temp2))


temp3 = patient1.model_dump(exclude_unset=True)
print(temp3)
print(type(temp3))