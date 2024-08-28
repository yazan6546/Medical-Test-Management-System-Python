import Filter_records
import Patient
from ConsolePrinter import ConsolePrinter
from InsertionHandler import InsertionHandler
from Patient import *
from Test_type import *
from UpdateHandler import UpdateHandler


def export_to_csv():
    headers = "ID, Test Name, Start Date, Result, Unit, Status, End Date\n"
    string = Patient.get_patients_without_numbering_CSV()

    # Read the entire file into a string
    with open('medicalRecord.csv', 'w') as file:
        file.write(headers)
        file.writelines(string)

def import_from_csv(name):
    Patient.patients.clear()
    # Read the entire file into a string

    try:
        with open(f"{name}.csv", 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"File {name}.csv does not exist\n")


    # Split content based on the first delimiter ':'
    records = content.split('\n')
    records = list(filter(lambda x: x != '', records))
    print(records)

    for record in records[1:]:
        data = record.split(',')
        print(data)
        id = data[0].strip()
        data = ",".join(data[1:]).strip()
        if id not in Patient.patients:
            Patient.add_patient(id)
        test = Test.create_test(data)
        Patient.patients[id].add_test(test)

    # for patient in Patient.patients.values():
    #     print(patient.id)



def main():

    Test_type.import_tests()
    Patient.import_records()


    while True:

        ConsolePrinter.show_menu()

        try:
            option = int(input("\nChoose your option.\n\n"))
        except ValueError as e:
            print(f"Error : {e}")
            continue

        if option == 1:
            ConsolePrinter.print_test_file()
            print()

        elif option == 2:
            ConsolePrinter.print_record_file()
            print()

        elif option == 3:
            InsertionHandler.insert_medical_test()
            print("Test successfully added.\n")

        elif option == 4:
            InsertionHandler.insert_medical_record()
            print("Record successfully added.\n")

        elif option == 5:
            UpdateHandler.update_medical_record()
            print("Record successfully updated.\n")

        elif option == 6:
            UpdateHandler.update_medical_test()
            print("Test successfully updated.\n")

        elif option == 7:

            ConsolePrinter.print_filter_menu()

            conditions = input("Enter conditions in this format : 1, 2, ...\n")

            try :
                InputValidator.is_match_pattern(conditions.replace(" ", ""))
                patients = Filter_records.filter_tests(conditions)
                Filter_records.print_filtered_tests(patients)
            except ValueError as e:
                print(f"Error : {e}")

        elif option == 8:
            ConsolePrinter.print_filter_menu()

            try :
                conditions = input("Enter conditions in this format : 1, 2, ...\n")
                InputValidator.is_match_pattern(conditions.replace(" ", ""))
                Filter_records.generate_report(conditions)
            except ValueError as e:
                print(f"Error : {e}")

        elif option == 9:
            export_to_csv()
            print("Successfully exported to medicalRecord.csv\n")

        elif option == 10:

            name = input("Enter the name of the csv file\n")
            import_from_csv(name)
            print("Successfully imported from medicalRecord.csv\n")

        else:
            print("Invalid option. Please try again.\n")




if __name__ == '__main__':
    main()
