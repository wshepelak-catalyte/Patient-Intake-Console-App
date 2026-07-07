import os
from cryptography.fernet import Fernet
import json

from models.address import Address
from models.gender import Gender
from models.patient import Patient
from ui.prompts import collect_raw_patient_input

class Database:
    def __init__(self, key_file: str = "secret.key", data_file: str = "private_file.txt"):
        self.key_file = key_file
        self.data_file = data_file
        self.fernet = self.load_or_create_key()

    def load_or_create_key(self) -> Fernet:
        """Loads an existing encryption key or creates a new one if it doesn't exist."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as file:
                key = file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as file:
                file.write(key)
        return Fernet(key)

    def get_next_patient_id(self) -> int:
        """Gets the next patient ID by counting existing patients."""
        try:
            patients = self.get_all_patients()
            return len(patients) + 1
        except:
            return 1

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
        """Saves a patient to the database."""
        # Convert the patient object to a string representation (WITHOUT newline)
        patient_data = f"{patient.id},{patient.first_name},{patient.last_name},{patient.ssn},{patient.email},{patient.address.street},{patient.address.city},{patient.address.state},{patient.address.zip_code},{patient.age},{patient.height if patient.height is not None else ''},{patient.weight if patient.weight is not None else ''},{patient.gender.value},{patient.insurance}"
        # Encrypt the data
        encrypted_data = self.fernet.encrypt(patient_data.encode())
        # Append the encrypted data to the file with newline separator
        with open(self.data_file, "ab") as file:
            file.write(encrypted_data)
            file.write(b'\n')  # Add newline AFTER encryption

    def view_patient_details(self, patient_id: int) -> Patient:
        """Views the details of a specific patient by ID."""
        patients = self.get_all_patients()
        for patient in patients:
            if patient.id == patient_id:
                return patient
        return None

    def get_all_patients(self) -> list:
        """Retrieves all patients from the database.
        Returns:
            list: A list of Patient objects.
        """
        if not os.path.exists(self.data_file):
            return []
        
        # read the encrypted data from the file
        with open(self.data_file, "rb") as file:
            encrypted_data = file.read()
        
        if not encrypted_data:
            return []
        
        # Split the encrypted data by newlines and decrypt each patient individually
        # Each line is a separate encrypted patient record
        encrypted_patients = encrypted_data.split(b'\n')
        patients = []
        
        for encrypted_patient in encrypted_patients:
            if encrypted_patient:
                try:
                    # Decrypt individual patient record
                    decrypted_data = self.fernet.decrypt(encrypted_patient).decode()
                    values = decrypted_data.strip().split(",")
                    
                    if len(values) >= 14:
                        patient = Patient(
                            id=int(values[0]),
                            first_name=values[1],
                            last_name=values[2],
                            ssn=values[3],
                            email=values[4],
                            address=Address(
                                street=values[5],
                                city=values[6],
                                state=values[7],
                                zip_code=values[8]
                            ),
                            age=int(values[9]),
                            height=float(values[10]) if values[10] else None,
                            weight=float(values[11]) if values[11] else None,
                            gender=Gender(values[12]),
                            insurance=values[13]
                        )
                        patients.append(patient)
                except Exception as e:
                    print(f"Error decrypting patient record: {e}")
                    continue
        
        return patients
    
    def save_all_patients(self, patients: list) -> None:
        """Saves all patients to the database.
        Args:
            patients (list): A list of Patient objects to save.
        """
        with open(self.data_file, "wb") as file:
            for patient in patients:
                # Convert each patient to a string (WITHOUT newline)
                patient_data = f"{patient.id},{patient.first_name},{patient.last_name},{patient.ssn},{patient.email},{patient.address.street},{patient.address.city},{patient.address.state},{patient.address.zip_code},{patient.age},{patient.height if patient.height is not None else ''},{patient.weight if patient.weight is not None else ''},{patient.gender.value},{patient.insurance}"
                # Encrypt the data
                encrypted_data = self.fernet.encrypt(patient_data.encode())
                # Write each encrypted patient with newline separator
                file.write(encrypted_data)
                file.write(b'\n')

    def save_patients(self, patients):
        """Saves all patients as JSON to the database."""
        patient_dicts = []
        for patient in patients:
            patient_dicts.append({
                "id": patient.id,
                "first_name": patient.first_name,
                "last_name": patient.last_name,
                "ssn": patient.ssn,
                "email": patient.email,
                "address": {
                    "street": patient.address.street,
                    "city": patient.address.city,
                    "state": patient.address.state,
                    "zip_code": patient.address.zip_code
                },
                "age": patient.age,
                "height": patient.height,
                "weight": patient.weight,
                "gender": patient.gender.value,
                "insurance": patient.insurance
            })
        json_data = json.dumps(patient_dicts)
        encrypted_data = self.fernet.encrypt(json_data.encode())
        with open(self.data_file, 'wb') as f:
            f.write(encrypted_data)

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