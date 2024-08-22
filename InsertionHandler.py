from ConsolePrinter import ConsolePrinter
from InputValidator import InputValidator
from Test_type import Test_type
from Utilities import Utilities


class InsertionHandler:

    @staticmethod
    def insert_medical_test():
        access = False
        while not access:
            test_name = input("Enter test name: \n").strip()

            if not test_name.isalpha():
                print("please enter a valid test name\n")
                continue

            if test_name in Test_type.types:
                print("Test already exists in medicalTest.txt. Enter another name\n")
                continue

            test_lower_bound = input("Enter test lower bound, if no lower bound exists, enter -1: \n").strip()
            test_upper_bound = input("Enter test upper bound: if no upper bound exists, enter -1: \n").strip()

            if (not Utilities.isfloat(test_lower_bound)) or (not Utilities.isfloat(test_upper_bound)):
                print("your test should have valid floating point bounds\n")
                continue

            if (test_lower_bound == '-1') and (test_upper_bound == '-1'):
                print("you should input at least one bound\n")
                continue

            if not Utilities.are_bounds_consistent(test_lower_bound, test_upper_bound):
                print("The lower bound should be less than the upper bound\n")

            test_unit = input("Enter test unit: \n").strip()

            if not test_name.isalpha():
                print("please enter a test unit\n")
                continue

            test_period = input("Enter test period in the format days-hours-minutes (dd-hh-mm): \n").strip()

            if not Utilities.is_period_valid(test_period):
                print("please enter a valid test period\n")
                continue

            days = test_period.split('-')[0].strip()
            hours = test_period.split('-')[1].strip()
            minutes = test_period.split('-')[2].strip()

            file_input_string = ''
            if (test_lower_bound != '-1' and test_upper_bound != '-1'):
                file_input_string = \
                f"\n{test_name};>{test_lower_bound},<{test_upper_bound};{test_unit};{test_period}\n"
                new_test = Test_type(name=test_name, range1=test_lower_bound, range2=test_upper_bound, unit=test_unit, period=(days, hours, minutes))

            elif test_lower_bound == '-1':
                file_input_string = f"\n{test_name};<{test_upper_bound};{test_unit};{test_period}\n"
                new_test = Test_type(name=test_name, range2=test_upper_bound, unit=test_unit, period=(days, hours, minutes))
            else:
                file_input_string = f"\n{test_name};>{test_lower_bound};{test_unit};{test_period}\n"
                new_test = Test_type(name=test_name, range1=test_lower_bound, unit=test_unit, period=(days, hours, minutes))

            record_file = open('medicalTest.txt', 'a')
            record_file.write(file_input_string)
            record_file.close()

            Test_type.types[test_name] = new_test
            access = True


    @staticmethod
    def insert_medical_record():
        access = False

        while not access:
            patient_id = input("Enter patient patient ID: \n").strip()

            if not InputValidator.is_patient_id_valid(patient_id):
                print("enter a valid patient ID \n")
                continue

            ConsolePrinter.print_test_names()
            print()

            test_name_number = input("Enter the number of the test you want:\n").strip()

            if not InputValidator.is_test_number_valid(test_name_number):
                print("enter a valid test number \n")
                continue

            test_date_time = input("Enter test date time in the format YYYY-MM-DD hh:mm : \n").strip()

            if not InputValidator.is_date_time_valid(test_date_time):
                print("enter a valid test date and time \n")
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

            # access = True
            # test_name = tests_list.split("- ")[int(test_status_number)][1]
            # test_status = test_states_list("- ")[int(test_status_number)][1]

            #if test_status == "Completed":
                    #continue from here





