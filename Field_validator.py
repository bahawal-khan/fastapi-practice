from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: Dict[str, str]

    # Email validator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hbl.com', 'js.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Email is not valid')

        return value

    # Transform name
    @field_validator('name')
    @classmethod
    def transform(cls, value):
        return value.upper()

    # Age validator (before mode)
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Not a correct age')


def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


patient_info = {
    'name': 'Khan',
    'age': '21',
    'email': 'khan@hbl.com',
    'weight': 75,
    'contact_details': {
        'contact': '12345678910'
    },
    'linkedin_url': 'http://linkedin.com/1322',
    'allergies': ['Dust'],
    'married': False
}

patient1 = Patient(**patient_info)

insert_patient_info(patient1)