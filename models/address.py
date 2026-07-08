"""
Defines an address class used to group location data together into one object.
"""
from dataclasses import dataclass


@dataclass
class Address:
    """
    Address class to represent a physical address of where patient is located.    

    Attributes:
        street (str): The street address of the patient.
        city (str): The city where the patient resides.
        state (str): The state where the patient resides.
        zip_code (str): The ZIP code of the patient's address.
    """

    street: str
    city: str
    state: str
    zip_code: str
