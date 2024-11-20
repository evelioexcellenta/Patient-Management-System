# Evelio Excellenta - Manajemen Data Pasien Rumah Sakit
import os
from tabulate import tabulate

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def no_empty_input(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        else:
            print("This field cannot be empty. Please enter a valid value.")

def yes_no_input(message):
    while True:
        user_input = input(message).strip().lower()
        if user_input in ("yes", "no"):
            return user_input
        print("Invalid input. Please enter 'yes' or 'no'.")

def create_patient(data):
    patient_id = no_empty_input("Enter Patient ID: ")
    if patient_id in data:
        input("Patient ID already exists! Press Enter to return to the menu...")
        return

    name = no_empty_input("Enter Name: ")
    age = int(no_empty_input("Enter Age: "))
    diagnosis = no_empty_input("Enter Diagnosis: ")
    room_number = no_empty_input("Enter Room Number: ")
    admission_date = no_empty_input("Enter Admission Date (DD-MM-YYYY): ")
    status = no_empty_input("Enter Patient Status: ")

    confirm = yes_no_input("\nDo you want to save this record? (yes/no): ").lower()
    if confirm == "yes":
        data[patient_id] = {
            "Name": name,
            "Age": age,
            "Diagnosis": diagnosis,
            "Room Number": room_number,
            "Admission Date": admission_date,
            "Status": status,  
        }
        print("Patient record added successfully.")
    else:
        print("Record not saved.")
    input("\nPress Enter to return to the menu...")

def read_patient(data):
    pid = input("Enter Patient ID (or leave blank to view all): ")
    if pid:
        if pid in data:
            patient_info = [
                [
                    pid,
                    data[pid].get("Name", "N/A"),
                    data[pid].get("Age", "N/A"),
                    data[pid].get("Diagnosis", "N/A"),
                    data[pid].get("Room Number", "N/A"),
                    data[pid].get("Admission Date", "N/A"),
                    data[pid].get("Status", "N/A"),
                ]
            ]
            print("\nPatient Record:")
            print(
                tabulate(
                    patient_info,
                    headers=[
                        "Patient ID",
                        "Name",
                        "Age",
                        "Diagnosis",
                        "Room Number",
                        "Admission Date",
                        "Status",
                    ],
                    tablefmt="grid",
                )
            )
        else:
            print("Patient not found.")
    else:
        if data:
            print("\nAll Patients:")
            table_data = []
            for pid, details in data.items():
                row = [pid] + [
                    details.get("Name", "N/A"),
                    details.get("Age", "N/A"),
                    details.get("Diagnosis", "N/A"),
                    details.get("Room Number", "N/A"),
                    details.get("Admission Date", "N/A"),
                    details.get("Status", "N/A"),
                ]
                table_data.append(row)
            print(
                tabulate(
                    table_data,
                    headers=[
                        "Patient ID",
                        "Name",
                        "Age",
                        "Diagnosis",
                        "Room Number",
                        "Admission Date",
                        "Status",
                    ],
                    tablefmt="grid",
                )
            )
        else:
            print("No patient records available.")
    input("\nPress Enter to return to the menu...")

def update_patient(data):
    pid = input("Enter Patient ID: ")
    if pid in data:
        print(f"\nCurrent details for Patient ID: {pid}")
        patient_info = [
            [
                pid,
                data[pid].get("Name", "N/A"),
                data[pid].get("Age", "N/A"),
                data[pid].get("Diagnosis", "N/A"),
                data[pid].get("Room Number", "N/A"),
                data[pid].get("Admission Date", "N/A"),
                data[pid].get("Status", "N/A"),
            ]
        ]
        print(
            tabulate(
                patient_info,
                headers=[
                    "Patient ID",
                    "Name",
                    "Age",
                    "Diagnosis",
                    "Room Number",
                    "Admission Date",
                    "Status",
                ],
                tablefmt="grid",
            )
        )

        field = input(
            "\nEnter Field to Update (Name, Age, Diagnosis, Room Number, Admission Date, Status): "
        ).capitalize()
        if field in data[pid]:
            new_value = no_empty_input(f"Enter New Value for {field}: ")
            print("\nNew details for confirmation:")
            patient_info_update = [[field, data[pid][field]], [field, new_value]]
            print(
                tabulate(
                    patient_info_update,
                    headers=["Field", "Old Value", "New Value"],
                    tablefmt="grid",
                )
            )

            confirm = yes_no_input("\nDo you want to save this update? (yes/no): ").lower()
            if confirm == "yes":
                data[pid][field] = new_value
                print(f"Patient {field} updated successfully.")
            else:
                print("Update canceled.")
        else:
            print("Field not found.")
    else:
        print("Patient not found.")
    input("\nPress Enter to return to the menu...")


def delete_patient(data):
    pid = input("Enter Patient ID to Delete: ")
    if pid in data:
        print(f"\nPatient details for deletion (ID: {pid}):")
        patient_info = [
            [
                pid,
                data[pid].get("Name", "N/A"),
                data[pid].get("Age", "N/A"),
                data[pid].get("Diagnosis", "N/A"),
                data[pid].get("Room Number", "N/A"),
                data[pid].get("Admission Date", "N/A"),
                data[pid].get("Status", "N/A"),
            ]
        ]
        print(
            tabulate(
                patient_info,
                headers=[
                    "Patient ID",
                    "Name",
                    "Age",
                    "Diagnosis",
                    "Room Number",
                    "Admission Date",
                    "Status",
                ],
                tablefmt="grid",
            )
        )
        confirm = yes_no_input("\nAre you sure you want to delete this record? (yes/no): ").lower()
        if confirm == "yes":
            del data[pid]
            print(f"Patient record {pid} deleted successfully.")
        else:
            print("Delete operation canceled.")
    else:
        print("Patient not found.")
    input("\nPress Enter to return to the menu...")

def discharge_patient(data):
    pid = input("Enter Patient ID to Discharge: ")
    if pid in data:
        if data[pid]["Status"].lower() == "discharged":
            print("Patient is already discharged.")
            input("\nPress Enter to return to the menu...")
            return

        print(f"\nCurrent Patient Details (ID: {pid}):")
        patient_info = [
            ["Name", data[pid]["Name"]],
            ["Age", data[pid]["Age"]],
            ["Diagnosis", data[pid]["Diagnosis"]],
            ["Room Number", data[pid]["Room Number"]],
            ["Admission Date", data[pid]["Admission Date"]],
            ["Status", data[pid]["Status"]]
        ]
        print(tabulate(patient_info, headers=["Field", "Value"], tablefmt="grid"))

        confirm = yes_no_input("\nAre you sure you want to discharge this patient? (yes/no): ").lower()
        if confirm == "yes":
            data[pid]["Status"] = "Discharged" 
            print(f"Patient {pid} has been successfully discharged.")
        else:
            print("Discharge operation canceled.")
    else:
        print("Patient not found.")
    input("\nPress Enter to return to the menu...")

def main():
    patient_data = {}
    while True:
        clear_screen()
        print("\nHospital Patient Data Management")
        print("1. Add Patient Record")
        print("2. View Patient Record")
        print("3. Update Patient Record")
        print("4. Delete Patient Record")
        print("5. Discharge Patient")
        print("6. Exit")
        choice = input("Enter your choice: ")
        clear_screen()
        if choice == "1":
            create_patient(patient_data)
        elif choice == "2":
            read_patient(patient_data)
        elif choice == "3":
            update_patient(patient_data)
        elif choice == "4":
            delete_patient(patient_data)
        elif choice == "5":
            discharge_patient(patient_data)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            input("Invalid choice. Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
