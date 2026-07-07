from dataclasses import dataclass
from typing import Optional

from models.address import Address
from models.gender import Gender

''' Patient class to represent a patient with personal and medical information.'''

@dataclass
class Patient:
    '''Attributes:
    id (int): The unique identifier for the patient, auto-assigned starting from 1.
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
    id: int = 0
    first_name: str = ""
    last_name: str = ""
    ssn: str = ""
    email: str = ""
    address: 'Address' = None
    age: int = 0
    height: Optional[float] = None
    weight: Optional[float] = None
    gender: 'Gender' = None
    insurance: str = ""