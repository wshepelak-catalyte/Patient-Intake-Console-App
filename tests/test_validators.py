"""Tests for patient input validation helpers."""

import pytest

from validation.validators import (
    is_valid_age,
    is_valid_city,
    is_valid_email,
    is_valid_gender,
    is_valid_height,
    is_valid_insurance,
    is_valid_last_name,
    is_valid_name,
    is_valid_ssn,
    is_valid_state,
    is_valid_street,
    is_valid_weight,
    zip_code_is_valid,
)


def test_valid_name_values() -> None:
    assert is_valid_name("Victor")
    assert is_valid_name("Mary-Jane")
    assert is_valid_name("O'Connor")
    assert is_valid_name("Anne Marie")


def test_invalid_name_values() -> None:
    assert not is_valid_name("")
    assert not is_valid_name("123")
    assert not is_valid_name("John@Doe")
    assert not is_valid_name("A" * 31)


def test_valid_last_name_values() -> None:
    assert is_valid_last_name("Smith")
    assert is_valid_last_name("Van Helsing")


def test_invalid_last_name_values() -> None:
    assert not is_valid_last_name("")
    assert not is_valid_last_name("Smith#")


def test_valid_ssn_values() -> None:
    assert is_valid_ssn("123-45-6789")


def test_invalid_ssn_values() -> None:
    assert not is_valid_ssn("123456789")
    assert not is_valid_ssn("12-345-6789")
    assert not is_valid_ssn("abc-de-ghij")


def test_valid_email_values() -> None:
    assert is_valid_email("user@example.com")
    assert is_valid_email("alice123@domain.org")


def test_invalid_email_values() -> None:
    assert not is_valid_email("user@@example.com")
    assert not is_valid_email("user@domain")
    assert not is_valid_email("toolong" + "a" * 45 + "@x.com")


def test_valid_street_values() -> None:
    assert is_valid_street("8430 W Sunset Blvd")
    assert is_valid_street("123 Main St.")


def test_invalid_street_values() -> None:
    assert not is_valid_street("")
    assert not is_valid_street("Street!@#")
    assert not is_valid_street("A" * 31)


def test_valid_city_values() -> None:
    assert is_valid_city("Los Angeles")
    assert is_valid_city("St. Louis")


def test_invalid_city_values() -> None:
    assert not is_valid_city("")
    assert not is_valid_city("City123")
    assert not is_valid_city("A" * 31)


def test_valid_state_values() -> None:
    assert is_valid_state("CA")
    assert is_valid_state("NY")


def test_invalid_state_values() -> None:
    assert not is_valid_state("C")
    assert not is_valid_state("XX")
    assert not is_valid_state("ca")


def test_valid_zip_code_values() -> None:
    assert zip_code_is_valid("90210")
    assert zip_code_is_valid("90210-1234")


def test_invalid_zip_code_values() -> None:
    assert not zip_code_is_valid("9021")
    assert not zip_code_is_valid("902101234")
    assert not zip_code_is_valid("90210-123")


def test_valid_age_values() -> None:
    assert is_valid_age("0") == 0
    assert is_valid_age("120") == 120
    assert is_valid_age("35") == 35


def test_invalid_age_values() -> None:
    assert is_valid_age("") == -1
    assert is_valid_age("-1") == -1
    assert is_valid_age("121") == -1
    assert is_valid_age("thirty") == -1


def test_valid_height_values() -> None:
    assert is_valid_height("") is None
    assert is_valid_height("0") == 0
    assert is_valid_height("108") == 108


def test_invalid_height_values() -> None:
    assert is_valid_height("109") == -1
    assert is_valid_height("-1") == -1
    assert is_valid_height("abc") == -1


def test_valid_weight_values() -> None:
    assert is_valid_weight("") is None
    assert is_valid_weight("0") == 0
    assert is_valid_weight("1400") == 1400


def test_invalid_weight_values() -> None:
    assert is_valid_weight("1401") == -1
    assert is_valid_weight("-5") == -1
    assert is_valid_weight("abc") == -1


def test_valid_gender_values() -> None:
    assert is_valid_gender("Male")
    assert is_valid_gender("Female")
    assert is_valid_gender("Other")


def test_invalid_gender_values() -> None:
    assert not is_valid_gender("")
    assert not is_valid_gender("male")
    assert not is_valid_gender("Unknown")


def test_valid_insurance_values() -> None:
    assert is_valid_insurance("Self-Insured")
    assert is_valid_insurance("Health Plan")


def test_invalid_insurance_values() -> None:
    assert not is_valid_insurance("")
    assert not is_valid_insurance("Insurance@123")


if __name__ == "__main__":
    pytest.main(["-q", __file__])
