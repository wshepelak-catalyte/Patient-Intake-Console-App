def collect_raw_patient_input() -> dict:
    """
    Collects raw patient input from the user.

    Returns:
        dict: A dictionary containing the raw patient input.
    """
    return {
        "first_name": input("Enter first name: ").strip(),
        "last_name": input("Enter last name: ").strip(),
        "ssn": input("Enter social security number (SSN): ").strip(),
        "email": input("Enter email address: ").strip(),
        "address": {
            "street": input("Enter street address: ").strip(),
            "city": input("Enter city: ").strip(),
            "state": input("Enter state: ").strip(),
            "zip_code": input("Enter zip code: ").strip(),
        },
        "age": input("Enter age: ").strip(),
        "height": input("Enter height in centimeters: ").strip(),
        "weight": input("Enter weight in kilograms: ").strip(),
        "gender": input("Enter gender (Male/Female/Other): ").strip(),
        "insurance": input("Enter insurance provider: ").strip(),
    }