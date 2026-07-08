"""
Validation functions for patient input fields including names, SSN, email,
address component, age, height, weight, gender, and insurance provider.
"""
import re
from validation.state_codes import STATE_CODE_TO_NAME
from validation.duplicates import is_unique_ssn, is_unique_email
from storage.database import Database

NAME_PATTERN = re.compile(r"^[A-Za-z .,'-]{1,30}$")
SSN_PATTERN = re.compile(r"^\d{3}-\d{2}-\d{4}$")
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$")
STREET_PATTERN = re.compile(r"^[A-Za-z0-9\s.,'-]{1,30}$")
CITY_PATTERN = re.compile(r"^[A-Za-z\s.,'-]{1,30}$")
STATE_CODE_PATTERN = re.compile(r"^[A-Z]{2}$")
ZIP_CODE_PATTERN = re.compile(r"^\d{5}(-\d{4})?$")
INSURANCE_PATTERN = re.compile(r"^[A-Za-z .,'-]{1,50}$")

def is_valid_name(name: str) -> bool:
    """Validates that the name contains only letters and is not empty."""
    return bool(NAME_PATTERN.fullmatch(name))

def is_valid_last_name(last_name: str) -> bool:
    """Validates that the last name contains only letters and is not empty."""
    return bool(NAME_PATTERN.fullmatch(last_name))

def is_valid_ssn(database : Database, ssn: str) -> bool:
    """Validates that the SSN is in the format XXX-XX-XXXX and unique."""
    return bool(SSN_PATTERN.fullmatch(ssn)) and is_unique_ssn(database, ssn)

def is_valid_email(database : Database, email: str) -> bool:
    """Validates that the email is in a standard email format."""
    return (
        bool(EMAIL_PATTERN.fullmatch(email))
        and bool(re.match(r"^.{5,50}$", email))
        and is_unique_email(database, email)
    )

def is_valid_street(street: str) -> bool:
    """Validates that the street address is not empty and contains valid characters."""
    return bool(STREET_PATTERN.fullmatch(street))

def is_valid_city(city: str) -> bool:
    """Validates that the city name contains only letters and is not empty."""
    return bool(CITY_PATTERN.fullmatch(city))

def is_valid_state(state: str) -> bool:
    """Validates that the state is a valid two-letter state code."""
    return state in STATE_CODE_TO_NAME and bool(STATE_CODE_PATTERN.fullmatch(state))

def zip_code_is_valid(zip_code: str) -> bool:
    """Validates that the zip code is in the format XXXXX or XXXXX-XXXX."""
    return bool(ZIP_CODE_PATTERN.fullmatch(zip_code))

def is_valid_age(age: str) -> int:
    """
    Validates that the age is a positive integer and returns
    age as an int.
    
    Returns
    -------
        int: -1 if age is not a positive integer and the int cast
             of the age string if it is.
    """
    if age.isdigit() and -1*(int(age)-0)*(int(age)-120) >= 0:
        return int(age)
    return -1

def is_valid_height(height: str) -> int | None:
    """
    Validates that the height is a positive integer between 0 and 108 inches.
    
    A blank or whitespace-only string is treated as missing input and returns
    None. A numeric value between 0 and 108 inches is considered valid and is
    returned as an integer. Any other value results in -1 to indicate invalid
    input.
    """
    if str(height).strip() == "":
        return None  # Allow empty height
    if height.isdigit() and -1*(int(height)-0)*(int(height)-108) >= 0:
        return int(height)
    return -1

def is_valid_weight(weight: str) -> int | None:
    """Validates that the weight is a positive integer.
    
    A blank or whitespace-only string is treated as missing input and returns
    None. A numeric value between 0 and 1400 is considered valid and is
    returned as an integer. Any other value results in -1 to indicate invalid
    input.
    """
    if str(weight).strip() == "":
        return None  # Allow empty weight
    if weight.isdigit() and -1*(int(weight)-0)*(int(weight)-1400) >= 0:
        return int(weight)
    return -1


def is_valid_gender(gender: str) -> bool:
    """Validates that the gender is a valid input"""
    return gender in ["Male", "Female", "Other"]

def is_valid_insurance(insurance: str) -> bool:
    """Validates that the insurance is in a valid format"""
    return bool(INSURANCE_PATTERN.fullmatch(insurance))
