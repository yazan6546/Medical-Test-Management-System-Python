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

            try:
                InputValidator.is_test_number_valid(test_number, Test_type.types)
            except ValueError as e:
                print(f"Error: {e}")

            test = Test_type.types[list_key[int(test_number) - 1]]

            for attr, value in test.__dict__.items():
                while True:
                    new_value = input(f"Current {attr}: {value} | Enter new value or press Enter to skip: ").strip()
                    if not new_value:  # If the user presses Enter without input, skip the attribute
                        break
                    try:
                        # Validate the input using the corresponding validation function

                        if attr == 'name':
                            validated_value = Test_type.validation_map[attr](new_value, Test_type.types)
                        else:
                            validated_value = Test_type.validation_map[attr](new_value)

                        if attr == 'range2':
                            Utilities.are_bounds_consistent(test.range, validated_value)

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
                    new_value = input(f"Current {attr}: {value} | Enter new value or press Enter to skip: ").strip()
                    if not new_value:  # If the user presses Enter without input, skip the attribute
                        break
                    try:
                        # Validate the input using the corresponding validation function

                        if attr == 'name':
                            validated_value = Test_type.validation_map[attr](new_value, Test_type.types)
                        else:
                            validated_value = Test_type.validation_map[attr](new_value)

                        if attr == 'range2':
                            Utilities.are_bounds_consistent(test.range, validated_value)

                        setattr(test, attr, validated_value)  # Update the attribute
                        break  # Exit the loop if input is valid
                    except ValueError as e:
                        print(f"Invalid input for {attr}: {e}")
                        retry = input("Would you like to retry? (y/n): ").strip().lower()
                        if retry != 'y':
                            break  # Exit the loop if the user chooses not to retry

            access = True
