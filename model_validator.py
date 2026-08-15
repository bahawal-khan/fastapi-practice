from pydantic import BaseModel, EmailStr, AnyUrl,model_validator,computed_field
from typing import Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    height: float
    married: bool
    allergies: list[str]
    contact_details: Dict[str, str]


    ##model_validator

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient is too old need an emergency number')
        return model


##computed_field
@computed_field
@property
def bmi(self)-> float:
    return round(self.weight/(self.height**2),2)
    

def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.bmi)


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
    'married': False,
    'height': 1.72
}

patient1 = Patient(**patient_info)

insert_patient_info(patient1)