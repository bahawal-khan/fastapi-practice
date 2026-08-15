from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {
    'city': 'DGK',
    'state': 'Punjab',
    'pin': '32000'
}

patient_dict = {
    'name': 'Khan',
    'gender': 'male',
    'age': 21,
    'address': address_dict
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)