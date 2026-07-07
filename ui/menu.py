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