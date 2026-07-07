from models.address import Address
from models.gender import Gender
from models.patient import Patient
from ui.prompts import collect_raw_patient_input

class Database:
    def __init__(self):
        """Initialize the in-memory database with an empty patient list."""
        self.patients = []

    def get_next_patient_id(self) -> int:
        """Gets the next patient ID by counting existing patients."""
        return len(self.patients) + 1

    def create_patient(self) -> None:
        """Creates a new patient and saves it to the database."""
        raw_input = collect_raw_patient_input()
        patient = Patient(
            id=self.get_next_patient_id(),
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
        # Save the patient to the database
        self.save_patient(patient)

    def save_patient(self, patient: Patient) -> None:
        """Saves a patient to the in-memory database."""
        self.patients.append(patient)

    def view_patient_details(self, patient_id: int) -> Patient:
        """Views the details of a specific patient by ID."""
        patients = self.get_all_patients()
        for patient in patients:
            if patient.id == patient_id:
                return patient
        return None

    def get_all_patients(self) -> list:
        """Retrieves all patients from the in-memory database.
        Returns:
            list: A list of Patient objects.
        """
        return self.patients
    
    def save_all_patients(self, patients: list) -> None:
        """Updates the in-memory patient list.
        Args:
            patients (list): A list of Patient objects to store in memory.
        """
        self.patients = patients

    def edit_patient(self, patient_id: int, updated_patient: Patient) -> bool:
        """Edits an existing patient's details in the database.
        Args:
            patient_id (int): The ID of the patient to edit.
            updated_patient (Patient): The updated Patient object.
        Returns:
            bool: True if the patient was found and updated, False otherwise.
        """
        patients = self.get_all_patients()
        for i, patient in enumerate(patients):
            if patient.id == patient_id:
                patients[i] = updated_patient
                self.save_all_patients(patients)
                return True
        return False
    
    def delete_patient(self, patient_id: int) -> bool:
        """Deletes a patient from the database by ID.
        Args:
            patient_id (int): The ID of the patient to delete.
        Returns:
            bool: True if the patient was found and deleted, False otherwise.
        """
        patients = self.get_all_patients()
        for i, patient in enumerate(patients):
            if patient.id == patient_id:
                del patients[i]
                self.save_all_patients(patients)
                return True
        return False