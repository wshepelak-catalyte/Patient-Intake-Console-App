# Patient Intake Console App

## Overview

A console-based patient intake system that manages patient records entirely in memory. This project is a proof-of-concept application for Super Health Inc. and demonstrates Python dataclasses, enums, structured validation, nested models, and a simple menu-driven user interface.

## Features

- In-memory storage for all patient records
- Patient data modeled with `@dataclass` and a nested `Address` type
- Gender represented by a `Gender` enum with `MALE`, `FEMALE`, and `OTHER`
- Simple interactive menu for listing, creating, viewing, editing, and deleting patients
- Field-level validation helpers in `validation/validators.py`
- Console prompts in `ui/prompts.py` and menu handling in `ui/menu.py`

## Prerequisites

- Python 3.10 or newer
- Optional: a virtual environment for dependency isolation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wshepelak-catalyte/Patient-Intake-Console-App.git
   cd Patient-Intake-Console-App
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install development tooling if desired:

   ```bash
   pip install pylint pytest
   ```

> Note: The current repository does not require any external runtime dependencies beyond the Python standard library.

## Running the Application

From the project root, run:

```bash
python app.py
```

This starts the patient intake console menu. Available actions include:

1. List Patients
2. Create Patient
3. View Patient Details
4. Edit a Patient
5. Delete a Patient
6. Exit

## Project Structure

- `app.py` — application entry point that launches the main menu
- `models/` — dataclass models for `Patient`, `Address`, and `Gender`
- `storage/database.py` — in-memory storage layer for patient records
- `ui/menu.py` — main console menu and application workflows
- `ui/prompts.py` — raw user input prompts and validation helpers
- `validation/validators.py` — field validators for names, SSN, email, address, age, height, weight, gender, and insurance
- `validation/state_codes.py` — valid two-letter U.S. state codes
- `tests/` — placeholder directory for unit tests

## Validation Rules

Validation helper functions are isolated in `validation/validators.py` and cover the following fields:

- `first_name`, `last_name`: letters plus spaces, periods, commas, apostrophes, hyphens
- `ssn`: `XXX-XX-XXXX`
- `email`: `name@domain.com` format and length limits
- `street`: alphanumeric plus common symbols
- `city`: letters plus common symbols
- `state`: two-letter U.S. state abbreviation
- `zip_code`: `12345` or `12345-6789`
- `age`: integer between `0` and `120`
- `height`: optional integer between `0` and `108`
- `weight`: optional integer between `0` and `1400`
- `gender`: one of `Male`, `Female`, `Other`
- `insurance`: letters plus common characters, maximum 50 characters

## Linting

This repository includes a `.pylintrc` configuration file. Run linting with:

```bash
pylint .
```

## Testing

The repository currently does not include dedicated unit tests. The validation layer is intentionally separated from the console UI so that tests can be added for `validation/validators.py` without mocking user input.

A recommended test command once tests are added:

```bash
python -m pytest
```

## Known Limitations

- All data is stored in memory only and is lost when the program exits
- No authentication or external database integration is included
- The current edit workflow requires re-entering all patient fields
- Patient creation validation is currently performed during prompt collection rather than as a single raw-input batch

## Contributors
<a href="https://github.com/wshepelak-catalyte/Patient-Intake-Console-App/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wshepelak-catalyte/Patient-Intake-Console-App"/>
</a>
