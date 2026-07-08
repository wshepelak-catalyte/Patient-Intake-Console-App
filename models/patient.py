"""
Defines the Patient dataclass, which represents a single patient's record in the
patient intake system. This module stores demographic information, contact 
details, optional physical measurements, gender, insurance provider, and the
nested Address object associated with each patient.
"""
from dataclasses import dataclass
from typing import Optional

from models.address import Address
from models.gender import Gender

# pylint: disable=too-many-instance-attributes
@dataclass
class Patient:
    """
    Patient class to represent a patient with personal and medical information.

    Attributes:
        id (int): The unique identifier for the patient, auto-assigned starting from 1.
        first_name (str): The first name of the patient.
        last_name (str): The last name of the patient.
        ssn (str): The social security number of the patient.
        email (str): The email address of the patient.
        address (Address): The physical address of the patient.
        age (int): The age of the patient.
        height (int): The height of the patient in inches.
        weight (int): The weight of the patient in pounds.
        gender (enum): The gender of the patient, represented as an 
                       enumeration (e.g., Male, Female, Other).
        insurance (str): The insurance provider of the patient.
    """

    id: int = 0
    first_name: str = ""
    last_name: str = ""
    ssn: str = ""
    email: str = ""
    address: 'Address' = None
    age: int = ""
    height: Optional[int] = None
    weight: Optional[int] = None
    gender: 'Gender' = None
    insurance: str = ""
