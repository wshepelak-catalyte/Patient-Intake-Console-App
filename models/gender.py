"""
Defines the Gender enumeration used to represent patient gender values.
"""

from enum import Enum

class Gender(Enum):
    """Enumeration representing patient gender options."""

    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
