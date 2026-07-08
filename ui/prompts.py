"""Prompt helpers to gather and validate patient input from the user."""

from storage.database import Database
from validation.validators import (
    is_valid_name, is_valid_last_name, is_valid_ssn, is_valid_email,
    is_valid_street, is_valid_city, is_valid_state, zip_code_is_valid,
    is_valid_age, is_valid_height, is_valid_weight, is_valid_gender,
    is_valid_insurance
)

def collect_raw_patient_input(database : Database) -> dict:
    """
    Collects and validates patient input from the user.

    Returns:
        dict: A dictionary containing the validated patient input.
    """
    # First name with validation
    while True:
        first_name = input("Enter first name: ").strip()
        if is_valid_name(first_name):
            break
        print("Invalid first name. Use letters only (max 30 characters).")
    
    # Last name with validation
    while True:
        last_name = input("Enter last name: ").strip()
        if is_valid_last_name(last_name):
            break
        print("Invalid last name. Use letters only (max 30 characters).")
    
    # SSN with validation
    while True:
        ssn = input("Enter social security number (SSN) in format XXX-XX-XXXX: ").strip()
        if is_valid_ssn(database, ssn):
            break
        print("Invalid SSN. Use format XXX-XX-XXXX (e.g., 123-45-6789).")
    
    # Email with validation
    while True:
        email = input("Enter email address: ").strip()
        if is_valid_email(database, email):
            break
        print("Invalid email. Use format name@domain.com.")
    
    # Street with validation
    while True:
        street = input("Enter street address: ").strip()
        if is_valid_street(street):
            break
        print("Invalid street address. Use letters, numbers, and symbols only (max 30 characters).")
    
    # City with validation
    while True:
        city = input("Enter city: ").strip()
        if is_valid_city(city):
            break
        print("Invalid city. Use letters only (max 30 characters).")
    
    # State with validation
    while True:
        state = input("Enter state (two-letter code, e.g., CA): ").strip().upper()
        if is_valid_state(state):
            break
        print("Invalid state. Use a valid two-letter state code (e.g., CA, NY, TX).")
    
    # Zip code with validation
    while True:
        zip_code = input("Enter zip code (XXXXX or XXXXX-XXXX): ").strip()
        if zip_code_is_valid(zip_code):
            break
        print("Invalid zip code. Use format XXXXX or XXXXX-XXXX (e.g., 90210 or 90210-1234).")
    
    # Age with validation
    while True:
        age = input("Enter age: ").strip()
        if is_valid_age(age):
            break
        print("Invalid age. Enter a number between 0 and 120.")
    
    # Height with validation (optional)
    while True:
        height_raw = input("Enter height in centimeters (optional, press Enter to skip): ").strip()
        height_val = is_valid_height(height_raw)

        if height_val is None or height_val != -1:
            break
        print("Invalid height. Enter a number between 0 and 108 or leave blank.")
    
    # Weight with validation (optional)
    while True:
        weight_raw = input("Enter weight in kilograms (optional, press Enter to skip): ").strip()
        weight_val = is_valid_weight(weight_raw)

        if weight_val is None or weight_val != -1:
            break
        print("Invalid weight. Enter a number between 0 and 1400 or leave blank.")
    
    # Gender with validation
    while True:
        gender = input("Enter gender (Male/Female/Other): ").strip()
        if is_valid_gender(gender):
            break
        print("Invalid gender. Choose from: Male, Female, or Other.")
    
    # Insurance with validation
    while True:
        insurance = input("Enter insurance provider: ").strip()
        if is_valid_insurance(insurance):
            break
        print("Invalid insurance. Use letters, numbers, and symbols only (max 50 characters).")
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "ssn": ssn,
        "email": email,
        "address": {
            "street": street,
            "city": city,
            "state": state,
            "zip_code": zip_code,
        },
        "age": age,
        "height": height_val,
        "weight": weight_val,
        "gender": gender,
        "insurance": insurance,
    }

def collect_patient_edits(database : Database, patient: dict) -> dict:
    """
    Collects and validates patient edits from the user.

    Args:
        patient (dict): The existing patient data to be edited.
    """
    # ask which fields to edit
    print("Which fields would you like to edit? (Enter numbers separated by commas)")
    print("1. First Name")
    print("2. Last Name")
    print("3. SSN")
    print("4. Email")
    print("5. Address")
    print("6. Age")
    print("7. Height")
    print("8. Weight")
    print("9. Gender")
    print("10. Insurance")

    fields_to_edit = input("Enter your choices (e.g., 1,3,5): ").strip().split(",")

    patient_edits = database.get_patient_by_id(patient["id"]).__dict__.copy()  # Start with existing data
    for field in fields_to_edit:
        field = field.strip()
        if field == "1":
            while True:
                first_name = input("Enter new first name: ").strip()
                if is_valid_name(first_name):
                    patient_edits["first_name"] = first_name
                    break
                print("Invalid first name. Use letters only (max 30 characters).")
        elif field == "2":
            while True:
                last_name = input("Enter new last name: ").strip()
                if is_valid_last_name(last_name):
                    patient_edits["last_name"] = last_name
                    break
                print("Invalid last name. Use letters only (max 30 characters).")
        elif field == "3":
            while True:
                ssn = input("Enter new social security number (SSN) in format XXX-XX-XXXX: ").strip()
                if is_valid_ssn(database, ssn):
                    patient_edits["ssn"] = ssn
                    break
                print("Invalid SSN. Use format XXX-XX-XXXX (e.g., 123-45-6789).")
        elif field == "4":
            while True:
                email = input("Enter new email address: ").strip()
                if is_valid_email(database, email):
                    patient_edits["email"] = email
                    break
                print("Invalid email. Use format user@domain.com.")
        elif field == "5":
            while True:
                street = input("Enter new street address: ").strip()
                if is_valid_street(street):
                    patient_edits["address"]["street"] = street
                    break
                print("Invalid street address. Use letters, numbers, and symbols only (max 30 characters).")
            while True:
                city = input("Enter new city: ").strip()
                if is_valid_city(city):
                    patient_edits["address"]["city"] = city
                    break
                print("Invalid city. Use letters only (max 30 characters).")
            while True:
                state = input("Enter new state (two-letter code, e.g., CA): ").strip().upper()
                if is_valid_state(state):
                    patient_edits["address"]["state"] = state
                    break
                print("Invalid state. Use a valid two-letter state code (e.g., CA, NY, TX).")
            while True:
                zip_code = input("Enter new zip code (XXXXX or XXXXX-XXXX): ").strip()
                if zip_code_is_valid(zip_code):
                    patient_edits["address"]["zip_code"] = zip_code
                    break
                print("Invalid zip code. Use format XXXXX or XXXXX-XXXX (e.g., 90210 or 90210-1234).")
        elif field == "6":
            while True:
                age = input("Enter new age: ").strip()
                if is_valid_age(age):
                    patient_edits["age"] = age
                    break
                print("Invalid age. Enter a number between 0 and 120.")
        elif field == "7":
            while True:
                height_raw = input("Enter new height in centimeters (optional, press Enter to skip): ").strip()
                height_val = is_valid_height(height_raw)
                
                if height_val is None or height_val != -1:
                    patient_edits["height"] = height_val
                    break

                print("Invalid height. Enter a number between 0 and 108 or leave blank.")
        elif field == "8":
            while True:
                weight_raw = input("Enter new weight in kilograms (optional, press Enter to skip): ").strip()
                weight_val = is_valid_weight(weight_raw)

                if weight_val is None or weight_val != -1:
                    patient_edits["weight"] = weight_val
                    break

                print("Invalid weight. Enter a number between 0 and 1400 or leave blank.")
        elif field == "9":
            while True:
                gender = input("Enter new gender (Male/Female/Other): ").strip()
                if is_valid_gender(gender):
                    patient_edits["gender"] = gender
                    break
                print("Invalid gender. Choose from: Male, Female, or Other.")
        elif field == "10":
            while True:
                insurance = input("Enter new insurance provider: ").strip()
                if is_valid_insurance(insurance):
                    patient_edits["insurance"] = insurance
                    break
                print("Invalid insurance. Use letters, numbers, and symbols only (max 50 characters).")

    return patient_edits