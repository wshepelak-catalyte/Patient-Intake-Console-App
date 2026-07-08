"""Duplicate detection helpers for patient records."""

from storage.database import Database


def is_unique_ssn(patient_base: Database, ssn: str) -> bool:
    """Return True when the provided SSN is not already present in the database."""
    return not any(patient.ssn == ssn for patient in patient_base.patients)


def is_unique_email(patient_base: Database, email: str) -> bool:
    """Return True when the provided email is not already present in the database."""
    return not any(patient.email == email for patient in patient_base.patients)
