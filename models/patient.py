from dataclasses import dataclass
from typing import Optional

from models.address import Address
from models.gender import Gender

@dataclass
class Patient:
    '''Attributes:
    first_name (str): The first name of the patient.
    last_name (str): The last name of the patient.
    ssn (str): The social security number of the patient.
    email (str): The email address of the patient.
    address (Address): The physical address of the patient.
    age (int): The age of the patient.
    height (float): The height of the patient in centimeters.
    weight (float): The weight of the patient in kilograms.
    gender (enum): The gender of the patient, represented as an enumeration (e.g., Male, Female, Other).
    insurance (str): The insurance provider of the patient.
    '''
    first_name: str
    last_name: str
    ssn: str
    email: str
    address: 'Address'
    age: int
    height: Optional[float] = None
    weight: Optional[float] = None
    gender: 'Gender'
    insurance: str