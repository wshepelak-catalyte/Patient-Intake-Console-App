import re

def is_valid_name(name: str) -> bool:
    """Validates that the name contains only letters and is not empty."""
    return bool(re.match(r"^[A-Za-z.,'-]{1,30}$", name))

def is_valid_last_name(last_name: str) -> bool:
    """Validates that the last name contains only letters and is not empty."""
    return bool(re.match(r"^[A-Za-z.,'-]{1,30}$", last_name))

def is_valid_ssn(ssn: str) -> bool:
    """Validates that the SSN is in the format XXX-XX-XXXX."""
    return bool(re.match(r"^\d{3}-\d{2}-\d{4}$", ssn))

def is_valid_email(email: str) -> bool:
    """Validates that the email is in a standard email format."""
    return bool(re.match(r"^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$", email)) and bool(re.match(r"^.{5,50}$", email))

def is_valid_street(street: str) -> bool:
    """Validates that the street address is not empty and contains valid characters."""
    return bool(re.match(r"^[A-Za-z0-9.,'-]{1,30}$", street))

def is_valid_city(city: str) -> bool:
    """Validates that the city name contains only letters and is not empty."""
    return bool(re.match(r"^[A-Za-z.,'-]{1,30}$", city))

def is_valid_state(state: str) -> bool:
    """Validates that the state is a valid two-letter state code."""
    from validation.state_codes import STATE_CODE_TO_NAME
    return state in STATE_CODE_TO_NAME and bool(re.match(r"^[A-Z]{2}$", state))

def zip_code_is_valid(zip_code: str) -> bool:
    """Validates that the zip code is in the format XXXXX or XXXXX-XXXX."""
    return bool(re.match(r"^\d{5}(-\d{4})?$", zip_code))

def is_valid_age(age: str) -> bool:
    """Validates that the age is a positive integer."""
    return age.isdigit() and -1*(int(age)-0)*(int(age)-120) >= 0

def is_valid_height(height: str) -> bool:
    """Validates that the height is a positive integer between 0 and 108 inches."""
    if str(height).strip() == "":
        return True  # Allow empty height
    return height.isdigit() and -1*(int(height)-0)*(int(height)-108) >= 0

def is_valid_weight(weight: str) -> bool:
    """Validates that the weight is a positive integer."""
    if str(weight).strip() == "":
        return True  # Allow empty weight
    return weight.isdigit() and -1*(int(weight)-0)*(int(weight)-1400) >= 0

def is_valid_gender(gender: str) -> bool:
    """Validates that the gender is a valid input"""
    return gender in ["Male", "Female", "Other"]   

def is_valid_insurance(insurance: str) -> bool:
    """Validates that the insurance is in a valid format"""
    return bool(re.match(r"^[A-Za-z.,'-]{1,50}", insurance))