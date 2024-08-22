from ConsolePrinter import ConsolePrinter
from InputValidator import InputValidator
from Utilities import Utilities


class InsertionHandler:

    @staticmethod
    def insert_medical_test():
        access = False
        while not access:
            test_name = input("Enter test name: \n")
            test_lower_bound = input("Enter test lower bound, if no lower bound exists, enter -1: \n")
            test_upper_bound = input("Enter test upper bound: if no upper bound exists, enter -1: \n")
            test_unit = input("Enter test unit: \n")
            test_period = input("Enter test period in the format days-hours-minutes (dd-hh-mm): \n")
            if (not Utilities.isfloat(test_lower_bound)) or (not Utilities.isfloat(test_upper_bound)):
                print("your test should include one range at least\n")
                continue

            if (test_lower_bound == '-1') and (test_upper_bound == '-1'):
                print("you should input at least one bound\n")
                continue

            if test_name is None:
                print("please enter a test name\n")
                continue

            if test_unit is None:
                print("please enter a test unit\n")
                continue

            if not Utilities.is_period_valid(test_period):
                print("please enter a valid test period\n")
                continue

            file_input_string = ''
            if (test_lower_bound != '-1' and test_upper_bound != '-1' and
                    Utilities.are_bounds_consistent(test_lower_bound, test_upper_bound)):
                file_input_string = \
                    f"{test_name};>{test_lower_bound},<{test_upper_bound};{test_unit};{test_period}\n"
            elif test_lower_bound == '-1':
                file_input_string = f"{test_name};<{test_upper_bound};{test_unit};{test_period}\n"
            else:
                file_input_string = f"{test_name};>{test_lower_bound};{test_unit};{test_period}\n"

            record_file = open('medicalRecord.txt', 'a')
            record_file.write(file_input_string)
            record_file.close()
            access = True


    @staticmethod
    def insert_medical_record():
        access = False

        while not access:
            patient_id = input("Enter patient patient ID: \n")
            tests_list = ConsolePrinter.print_test_names()
            print(tests_list)
            test_name_number = input("Enter the number of the test you want:\n")
            test_date_time = input("Enter test date time in the format YYYY-MM-DD hh:mm : \n")
            test_result = input("Enter test result: \n")
            test_unit = input("Enter test unit: \n")
            test_states_list = ConsolePrinter.print_enter_available_test_states()
            print(test_states_list)
            test_status_number = input("Enter test status number from the list above:\n")

            if not InputValidator.is_patient_id_valid(patient_id):
                print("enter a valid patient ID \n")
                continue
            if not InputValidator.is_test_number_valid(test_name_number):
                print("enter a valid test number \n")
                continue
            if not InputValidator.is_date_time_valid(test_date_time):
                print("enter a valid test date and time \n")
                continue
            if not Utilities.isfloat(test_result):
                print("enter a valid test result \n")
                continue
            if test_unit is None:
                print("enter a valid test unit\n")
                continue
            if not InputValidator.is_test_status_number_valid(test_status_number):
                print("enter a valid test status number \n")
                continue

            test_name = tests_list.split("- ")[int(test_status_number)][1]
            test_status = test_states_list("- ")[int(test_status_number)][1]

            #if test_status == "Completed":
                    #continue from here





