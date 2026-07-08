"""User interface menu routines for the Patient Intake System."""

from storage.database import Database
from ui.prompts import collect_patient_edits, collect_raw_patient_input

database = Database()

def main_menu() -> None:
    """Displays the patient intake menu and handles user interaction."""

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
    """Displays the list of patients stored in the database."""

    print("\n=== List of Patients ===")
    patients = database.get_all_patients()

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
<<<<<<< Updated upstream
        print(
            f"ID: {patient.id}\n"
            f"Name: {patient.first_name} {patient.last_name}\n"
            f"Age: {patient.age}\n"
            f"Gender: {patient.gender.value}\n"
 )
=======
        print(f"ID: {patient.id}\nName: {patient.first_name} {patient.last_name}\nSSN: {patient.ssn}\nEmail: {patient.email}\nAddress: {patient.address.street}, {patient.address.city}, {patient.address.state} {patient.address.zip_code}\nAge: {patient.age}\nHeight: {patient.height}\nWeight: {patient.weight}\nGender: {patient.gender.value}\nInsurance: {patient.insurance}\n")
>>>>>>> Stashed changes

def create_patient() -> None:
    """Prompts the user for patient details and saves the new patient."""

    print("\n=== Create a New Patient ===")
    patient_input = collect_raw_patient_input(database)
    database.create_patient(patient_input)
    print("Patient created successfully.")


def view_patient_details() -> None:
    """Displays details for a specified patient ID."""

    print("\n=== View Patient Details ===")
    patient_id = int(input("Enter the ID of the patient: ").strip())
    patient = database.view_patient_details(patient_id)
    if patient is not None:
        print(f"ID: {patient.id}")
        print(f"Name: {patient.first_name} {patient.last_name}")
        print(f"SSN: {patient.ssn}")
        print(f"Email: {patient.email}")
        print(
            f"Address: {patient.address.street}, {patient.address.city}, "
            f"{patient.address.state} {patient.address.zip_code}"
        )
        print(f"Age: {patient.age}")
        print(f"Height: {patient.height}")
        print(f"Weight: {patient.weight}")
        print(f"Gender: {patient.gender.value}")
        print(f"Insurance: {patient.insurance}")
    else:
        print("!!!===your request is invalid===!!!")
        print("    Check the ID and try again")
        print("!!!=============================!!!")


def edit_patient() -> None:
    """Prompts the user to edit an existing patient's record."""

    print("\n=== Edit a Patient ===")
    patient_id = int(input("Enter the ID of the patient to edit: ").strip())
    patient = database.view_patient_details(patient_id)
    if not patient:
        print("Patient not found.")
        return

    print(f"Editing patient: {patient.first_name} {patient.last_name}")
<<<<<<< Updated upstream
    raw_input = collect_patient_edits(database, patient_id)  # Collect new patient data
    database.edit_patient(patient_id, raw_input)

=======
    raw_input = collect_patient_edits(patient_id)  # Collect new patient data
    patient = database.edit_patient(patient_id, raw_input)  # Update the patient in the database
>>>>>>> Stashed changes

def delete_patient() -> None:
    """Deletes a specified patient from the database after confirmation."""

    print("\n=== Delete a Patient ===")
    patient_id = int(input("Enter the ID of the patient to delete: ").strip())
    patient = database.view_patient_details(patient_id)
    if not patient:
        print("Patient not found.")
        return

    confirm_prompt = (
        f"Are you sure you want to delete {patient.first_name}"
        f" {patient.last_name}? (y/n): "
    )
    confirm = input(confirm_prompt).strip().lower()

    if confirm == 'y':
        database.delete_patient(patient_id)
        print("Patient deleted successfully.")
    else:
        print("Deletion cancelled.")
