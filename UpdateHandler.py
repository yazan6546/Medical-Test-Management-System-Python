from Test import Test
from ConsolePrinter import ConsolePrinter
from InputValidator import InputValidator
from Test_type import Test_type
from Utilities import Utilities
from Patient import Patient


class UpdateHandler:

    @staticmethod
    def update_medical_test():

        list_key = list(Test_type.types.keys())

        access = False
        while not access:

            ConsolePrinter.print_test_file()
            print()

            test_number = input("Enter test line number: \n").strip()

            if not InputValidator.is_test_number_valid(test_number):
                print("please enter a valid test number\n")
                continue

            test = Test_type.types[list_key[int(test_number) - 1]]

            for attr, value in test.__dict__.items():
                while True:
                    new_value = input(f"Current {attr}: {value} | Enter new value or press Enter to skip: ").strip()
                    if not new_value:  # If the user presses Enter without input, skip the attribute
                        break
                    try:
                        # Validate the input using the corresponding validation function
                        validated_value = Test_type.validation_map[attr](new_value)
                        setattr(test, attr, validated_value)  # Update the attribute
                        break  # Exit the loop if input is valid
                    except ValueError as e:
                        print(f"Invalid input for {attr}: {e}")
                        retry = input("Would you like to retry? (y/n): ").strip().lower()
                        if retry != 'y':
                            break  # Exit the loop if the user chooses not to retry

            access = True

    @staticmethod
    def update_medical_record():
        test_status_list = ["Pending", "Completed", "Reviewed"]
        access = False

        while not access:
            patient_id = input("Enter patient patient ID: \n").strip()

            if not InputValidator.is_patient_id_valid(patient_id):
                print("enter a valid patient ID \n")
                continue

            ConsolePrinter.print_test_names()
            print()

            test_name = input("Enter the test you want:\n").strip()

            if not InputValidator.is_test_name_valid(test_name):
                print("enter a valid test name \n")
                continue

            test_result = input("Enter test result: \n").strip()

            if not Utilities.isfloat(test_result):
                print("enter a valid floating point test result \n")
                continue

            ConsolePrinter.print_available_test_states()

            test_status_number = input("Enter test status number from the list above:\n").strip()
            if not InputValidator.is_test_status_number_valid(test_status_number):
                print("enter a valid test status number \n")
                continue

            test_date_start = input("Enter test date time in the format YYYY-MM-DD hh:mm : \n").strip()
            test_date_end = None

            if not InputValidator.is_date_time_valid(test_date_start):
                print("enter a valid test date and time \n")
                continue

            test_status = test_status_list[int(test_status_number) - 1]

            if test_status == "Completed":
                test_date_end = input("Enter test date time in the format YYYY-MM-DD hh:mm : \n").strip()
                if not InputValidator.is_date_time_valid(test_date_end):
                    print("enter a valid test date and time \n")
                    continue


            # add the new patient into the dictionary
            if patient_id not in Patient.patients:
                patient = Patient(id=patient_id)
                Patient.patients[patient_id] = patient

            test_unit = Test_type.types[test_name].unit
            test = Test(name=test_name, unit=test_unit, status=test_status, result=test_result, date_start=test_date_start, date_end=test_date_end)
            Patient.patients[patient_id].add_test(test)

            record_file = open('medicalRecord.txt', 'a')
            record_file.write(f"{patient_id}: {str(test)}")
            record_file.close()

            access = True
            # test_name = tests_list.split("- ")[int(test_status_number)][1]
            # test_status = test_states_list("- ")[int(test_status_number)][1]

            #if test_status == "Completed":
            #continue from here
