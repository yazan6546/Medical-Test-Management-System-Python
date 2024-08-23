from ConsolePrinter import ConsolePrinter
from InputValidator import InputValidator
from Patient import Patient
from Test_type import Test_type


class UpdateHandler:

    @staticmethod
    def update_medical_test():

        list_key = list(Test_type.types.keys())

        access = False
        while not access:

            ConsolePrinter.print_test_file()
            print()

            test_number = input("Enter test line number: \n").strip()

            try:
                InputValidator.is_test_number_valid(test_number, Test_type.types)
            except ValueError as e:
                print(f"Error: {e}")

            test = Test_type.types[list_key[int(test_number) - 1]]
            for attr, value in test.__dict__.items():
                while True:
                    attr = str(attr).replace("_Test_type__", "")
                    new_value = input(f"Current {attr}: {value} | Enter new value or press Enter to skip: ").strip()
                    if not new_value:  # If the user presses Enter without input, skip the attribute
                        break
                    try:
                        # Validate the input using the corresponding validation function
                        setattr(test, attr, new_value)  # Update the attribute
                        break  # Exit the loop if input is valid
                    except ValueError as e:
                        print(f"Invalid input for {attr}: {e}")
                        retry = input("Would you like to retry? (y/n): ").strip().lower()
                        if retry != 'y':
                            break  # Exit the loop if the user chooses not to retry

            print()
            access = True

    @staticmethod
    def update_medical_record():

        access = False
        while not access:

            ConsolePrinter.print_record_file()
            test_id = input("\nEnter the ID that you want a test of:\n").strip()
            try:
                InputValidator.is_patient_id_exist(test_id, Patient.patients)
                patient = Patient.patients[test_id]

                # Print the numbered patient tests
                print(patient)
                record_num = input("Enter the line number of the record:\n").strip()
                InputValidator.is_test_record_number_valid(record_num, patient.get_test_numbers())
                test = patient.get_test(int(record_num) - 1)

            except ValueError as e:
                print(f"Error: {e}")
                continue

            for attr, value in test.__dict__.items():

                # The unit is brought from Test types object
                if attr == 'unit':
                    continue

                # Do not ask for date_end input if status is not completed
                if test.status.lower != 'completed' and attr == '_Test__date_end':
                    continue

                while True:
                    attr = str(attr).replace("_Test__", "")
                    new_value = input(f"Current {attr}: {value} | Enter new value or press Enter to skip: ").strip()

                    if not new_value:  # If the user presses Enter without input, skip the attribute
                        break
                    try:
                        # Validate the input using the corresponding validation function
                        setattr(test, attr, new_value)  # Update the attribute
                        break  # Exit the loop if input is valid
                    except ValueError as e:
                        print(f"Invalid input for {attr}: {e}")
                        retry = input("Would you like to retry? (y/n): ").strip().lower()
                        if retry != 'y':
                            break  # Exit the loop if the user chooses not to retry

            print()
            access = True
