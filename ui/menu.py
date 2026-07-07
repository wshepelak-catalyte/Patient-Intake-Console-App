from models.patient import Patient
from models.address import Address
from models.gender import Gender
from storage.database import Database
from ui.prompts import collect_raw_patient_input

database = Database()

def main_menu() -> None:

    while True:
        print("\n=== Patient Intake System ===")
        print("1. List Patients")
        print("2. Create Patient")
        print("3. View Patient Details")
        print("4. Edit a Patient")
        print("5. Delete a Patient")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            list_patients()
        elif choice == "2":
            create_patient()
        elif choice == "3":
            view_patient_details()
        elif choice == "4":
            edit_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            

def list_patients() -> None:
    print("\n=== List of Patients ===")
    try:
        patients = database.get_all_patients()
    except Exception as e:
        print(f"Error occurred while fetching patients: {e}")
        return

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print(f"ID: {patient.id}\nName: {patient.first_name} {patient.last_name}\nSSN: {patient.ssn}\nEmail: {patient.email}\nAddress: {patient.address.street}, {patient.address.city}, {patient.address.state} {patient.address.zip_code}\nAge: {patient.age}\nHeight: {patient.height}\nWeight: {patient.weight}\nGender: {patient.gender.value}\nInsurance: {patient.insurance}\n")       

def create_patient() -> None:
    print("\n=== Create a New Patient ===")
    #database.create_patient()
    patient_input = collect_raw_patient_input()
    database.create_patient(patient_input)
    print("Patient created successfully.")

def view_patient_details() -> None:
    print("\n=== View Patient Details ===")
    patient_id = int(input("Enter the ID of the patient: ").strip())
    patient = database.view_patient_details(patient_id)
    if patient:
        print(f"ID: {patient.id}")
        print(f"Name: {patient.first_name} {patient.last_name}")
        print(f"SSN: {patient.ssn}")
        print(f"Email: {patient.email}")
        print(f"Address: {patient.address.street}, {patient.address.city}, {patient.address.state} {patient.address.zip_code}")
        print(f"Age: {patient.age}")
        print(f"Height: {patient.height}")
        print(f"Weight: {patient.weight}")
        print(f"Gender: {patient.gender.value}")
        print(f"Insurance: {patient.insurance}")

def edit_patient() -> None:
    print("\n=== Edit a Patient ===")
    patient_id = int(input("Enter the ID of the patient to edit: ").strip())
    patient = database.view_patient_details(patient_id)
    if not patient:
        print("Patient not found.")
        return

    print(f"Editing patient: {patient.first_name} {patient.last_name}")
    raw_input = collect_raw_patient_input()  # Collect new patient data
    # Create a Patient object with the new data
    updated_patient = Patient(
        id=patient_id,
        first_name=raw_input["first_name"],
        last_name=raw_input["last_name"],
        ssn=raw_input["ssn"],
        email=raw_input["email"],
        address=Address(
            street=raw_input["address"]["street"],
            city=raw_input["address"]["city"],
            state=raw_input["address"]["state"],
            zip_code=raw_input["address"]["zip_code"]
        ),
        age=int(raw_input["age"]),
        height=float(raw_input["height"]) if raw_input["height"] else None,
        weight=float(raw_input["weight"]) if raw_input["weight"] else None,
        gender=Gender(raw_input["gender"]),
        insurance=raw_input["insurance"]
    )
    # Update the patient details
    if database.edit_patient(patient_id, updated_patient):
        print("Patient updated successfully.")
    else:
        print("Failed to update patient.")

def delete_patient() -> None:
    print("\n=== Delete a Patient ===")
    patient_id = int(input("Enter the ID of the patient to delete: ").strip())
    patient = database.view_patient_details(patient_id)
    if not patient:
        print("Patient not found.")
        return

    confirm = input(f"Are you sure you want to delete {patient.first_name} {patient.last_name}? (y/n): ").strip().lower()
    if confirm == 'y':
        database.delete_patient(patient_id)
        print("Patient deleted successfully.")
    else:
        print("Deletion cancelled.")