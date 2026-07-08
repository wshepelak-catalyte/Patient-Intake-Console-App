"""Prompt helpers to gather and validate patient input from the user."""

# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=too-many-locals
from models.gender import Gender
from models.patient import Patient
from storage.database import Database
from validation.validators import (
    is_valid_name, is_valid_last_name, is_valid_ssn, is_valid_email,
    is_valid_street, is_valid_city, is_valid_state, zip_code_is_valid,
    is_valid_age, is_valid_height, is_valid_weight, is_valid_gender,
    is_valid_insurance
)


def collect_raw_patient_input(database: Database) -> dict | None:
    """Collects raw patient input and validates it once."""
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    ssn = input(
        "Enter social security number (SSN) in format XXX-XX-XXXX: "
    ).strip()
    email = input("Enter email address: ").strip()
    street = input("Enter street address: ").strip()
    city = input("Enter city: ").strip()
    state = input("Enter state (two-letter code, e.g., CA): ").strip().upper()
    zip_code = input("Enter zip code (XXXXX or XXXXX-XXXX): ").strip()
    age_raw = input("Enter age: ").strip()
    height_raw = input(
        "Enter height in inches (optional, press Enter to skip): "
    ).strip()
    weight_raw = input(
        "Enter weight in pounds (optional, press Enter to skip): "
    ).strip()
    gender = input("Enter gender (Male/Female/Other): ").strip()
    insurance = input("Enter insurance provider: ").strip()

    raw_input = {
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
        "age": age_raw,
        "height": height_raw,
        "weight": weight_raw,
        "gender": gender,
        "insurance": insurance,
    }

    validated_input, errors = validate_patient_input(database, raw_input)
    if errors:
        print("\n=== Patient creation failed ===")
        for error in errors:
            print(f"- {error}")
        print("Patient was not created. Returning to the main menu.")
        return None

    return validated_input


def validate_patient_input(database: Database, raw_input: dict) -> tuple[dict, list[str]]:
    """Validate raw patient input and return cleaned data plus errors."""
    errors = []
    cleaned_input = {
        "first_name": raw_input["first_name"],
        "last_name": raw_input["last_name"],
        "ssn": raw_input["ssn"],
        "email": raw_input["email"],
        "address": raw_input["address"],
        "age": None,
        "height": None,
        "weight": None,
        "gender": raw_input["gender"],
        "insurance": raw_input["insurance"],
    }

    if not is_valid_name(cleaned_input["first_name"]):
        errors.append(
            "Invalid first name. Use letters only (max 30 characters)."
        )
    if not is_valid_last_name(cleaned_input["last_name"]):
        errors.append(
            "Invalid last name. Use letters only (max 30 characters)."
        )
    if not is_valid_ssn(database, cleaned_input["ssn"]):
        errors.append("Invalid SSN. Use format XXX-XX-XXXX or a unique SSN.")
    if not is_valid_email(database, cleaned_input["email"]):
        errors.append("Invalid email. Use format name@domain.com or a unique email.")
    if not is_valid_street(cleaned_input["address"]["street"]):
        errors.append(
            "Invalid street address. Use letters, numbers, and symbols only"
            " (max 30 characters)."
        )
    if not is_valid_city(cleaned_input["address"]["city"]):
        errors.append("Invalid city. Use letters only (max 30 characters).")
    if not is_valid_state(cleaned_input["address"]["state"]):
        errors.append(
            "Invalid state. Use a valid two-letter state code (e.g., CA, NY, TX)."
        )
    if not zip_code_is_valid(cleaned_input["address"]["zip_code"]):
        errors.append(
            "Invalid zip code. Use format XXXXX or XXXXX-XXXX"
            " (e.g., 90210 or 90210-1234)."
        )

    age_value = is_valid_age(raw_input["age"])
    if age_value == -1:
        errors.append("Invalid age. Enter a number between 0 and 120.")
    else:
        cleaned_input["age"] = age_value

    height_value = is_valid_height(raw_input["height"])
    if height_value == -1:
        errors.append(
            "Invalid height. Enter a number between 0 and 108 or leave blank."
        )
    else:
        cleaned_input["height"] = height_value

    weight_value = is_valid_weight(raw_input["weight"])
    if weight_value == -1:
        errors.append(
            "Invalid weight. Enter a number between 0 and 1400 or leave blank."
        )
    else:
        cleaned_input["weight"] = weight_value

    if not is_valid_gender(cleaned_input["gender"]):
        errors.append("Invalid gender. Choose from: Male, Female, or Other.")
    if not is_valid_insurance(cleaned_input["insurance"]):
        errors.append(
            "Invalid insurance. Use letters, numbers, and symbols only"
            " (max 50 characters)."
        )

    return cleaned_input, errors

def collect_patient_edits(database: Database, patient_id: int) -> Patient:
    """
    Collects and validates patient edits from the user.

    Args:
        patient_id (int): The ID of the patient to edit.
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
    # retrieve patient object from database using patient id
    patient = database.view_patient_details(patient_id)

    for field in fields_to_edit:
        field = field.strip()
        if field == "1":
            while True:
                first_name = input("Enter new first name: ").strip()
                if is_valid_name(first_name):
                    patient.first_name = first_name
                    break
        elif field == "2":
            while True:
                last_name = input("Enter new last name: ").strip()
                if is_valid_last_name(last_name):
                    patient.last_name = last_name
                    break
        elif field == "3":
            while True:
                ssn = input(
                    "Enter new social security number (SSN) in format XXX-XX-XXXX: ").strip()
                if is_valid_ssn(database, ssn):
                    patient.ssn = ssn
                    break
        elif field == "4":
            while True:
                email = input("Enter new email address: ").strip()
                if is_valid_email(database, email):
                    patient.email = email
                    break
        elif field == "5":
            while True:
                street = input("Enter new street address: ").strip()
                if is_valid_street(street):
                    patient.address.street = street
                    break
            while True:
                city = input("Enter new city: ").strip()
                if is_valid_city(city):
                    patient.address.city = city
                    break
            while True:
                state = input("Enter new state (two-Letter code, e.g., CA): ").strip().upper()
                if is_valid_state(state):
                    patient.address.state = state
                    break
            while True:
                zip_code = input("Enter new zip code (XXXXX or XXXXX-XXXX): ").strip()
                if zip_code_is_valid(zip_code):
                    patient.address.zip_code = zip_code
                    break
        elif field == "6":
            while True:
                age_raw = input("Enter new age: ").strip()
                age_val = is_valid_age(age_raw)
                if age_val != -1:
                    patient.age = age_val
                    break
        elif field == "7":
            while True:
                height_raw = input(
                    "Enter new height in inches (optional, press Enter to skip): ").strip()
                height_val = is_valid_height(height_raw)
                if height_val is None or height_val != -1:
                    patient.height = height_val
                    break
        elif field == "8":
            while True:
                weight_raw = input(
                "Enter new weight in pounds (optional, press Enter to skip): ").strip()
                weight_val = is_valid_weight(weight_raw)
                if weight_val is None or weight_val != -1:
                    patient.weight = weight_val
                    break
        elif field == "9":
            while True:
                gender = input("Enter new gender (Male/Female/Other): ").strip()
                if is_valid_gender(gender):
                    patient.gender = Gender(gender)
                    break
        elif field == "10":
            while True:
                insurance = input("Enter new insurance provider: ").strip()
                if is_valid_insurance(insurance):
                    patient.insurance = insurance
                    break
    return patient
