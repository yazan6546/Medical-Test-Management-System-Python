import Filter_records
import Patient
from ConsolePrinter import ConsolePrinter
from InsertionHandler import InsertionHandler
from Patient import *
from Test_type import *
from UpdateHandler import UpdateHandler


def main():

    Test_type.import_tests()
    Patient.import_records()


    while True:

        ConsolePrinter.show_menu()
        option = int(input("\nChoose your option.\n\n"))

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
            continue

        elif option == 10:
            continue

        else:
            print("Invalid option. Please try again.\n")




if __name__ == '__main__':
    main()
