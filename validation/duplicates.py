"""Duplicate detection helpers for patient records."""

from storage.database import Database


def is_unique_ssn(patient_base: Database, ssn: str) -> bool:
    """Return True when the provided SSN is not already present in the database."""
    unique = True

    for patient in patient_base.patients:
        if patient.ssn == ssn:
            unique = False

    return unique


def is_unique_email(patient_base: Database, email: str) -> bool:
    """Return True when the provided email is not already present in the database."""
    unique = True

    for patient in patient_base.patients:
        if patient.email == email:
            unique = False

    return unique
