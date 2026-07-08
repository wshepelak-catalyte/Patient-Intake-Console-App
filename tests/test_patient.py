"""Tests for the Patient class in models/patient.py."""

from unittest import mock
from models.patient import Patient
from models.address import Address

def test_patient_str_representation():
    """Test the string representation of the Patient class."""
    mock_name = "John"
    mock_last_name = "Doe"
    mock_ssn = "123-45-6789"
    mock_email = "john.doe@example.com"
    mock_address = Address(
        street = "123 Main St",
        city = "Anytown",
        state = "CA",
        zip_code = "12345"
    )
    mock_age = 30
    mock_height = 70
    mock_weight = 180
    mock_gender = mock.Mock()
    mock_gender.value = "Male"
    mock_insurance = "Blue Cross"

    patient = Patient(
        id=1, first_name=mock_name, last_name=mock_last_name, ssn=mock_ssn,
        address=mock_address, email=mock_email, age=mock_age, height=mock_height,
        weight=mock_weight, gender=mock_gender, insurance=mock_insurance
    )

    expected_str = (
        "Patient ID: 1\n"
        f"Name: {mock_name} {mock_last_name}\n"
        f"SSN: {mock_ssn}\n"
        f"Email: {mock_email}\n"
        f"Address: {str(mock_address)}\n"
        f"Age: {mock_age}\n"
        f"Height: {mock_height}\n"
        f"Weight: {mock_weight}\n"
        f"Gender: {mock_gender.value}\n"
        f"Insurance: {mock_insurance}\n"
    )

    assert str(patient) == expected_str
