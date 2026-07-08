from storage.database import Database

def is_unique_ssn(patient_base : Database, ssn : str) -> bool:
    unique = True
    
    for patient in patient_base.patients:
        if patient.get("ssn") == ssn:
            unique = False
    
    return unique

def is_unique_email(patient_base : Database, email : str) -> bool:
    unique = True

    for patient in patient_base.patients:
        if patient.get("email") == email:
            unique = False
    
    return unique
