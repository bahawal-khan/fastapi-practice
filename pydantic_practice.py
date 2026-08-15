##first create a pydantic model
##Type validation pydantic
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

##We do a custom validation using field function and metadata

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of patient in 50 char',examples=['Ali','Ahmad'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0,lt=110)
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient is married or not')]
    allergies: Optional[List[str]]= Field(max_length = 5)
    contact_details: Dict[str,str]

def insert_patient_info(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


patient_info = {'name': 'Khan','age': 21,'email':'khan@gmail.com','weight': 75,
                'contact_details':{'contact': '12345678910'},'linkedin_url': 'http://linkedin.com/1322','allergies':['Dust']}

patient1 =  Patient(**patient_info)



insert_patient_info(patient1)