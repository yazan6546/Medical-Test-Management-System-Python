from Test import Test
from ConsolePrinter import ConsolePrinter
from InputValidator import InputValidator
from Test_type import Test_type
from Patient import Patient


class InsertionHandler:

    @staticmethod
    def insert_medical_test():
        access = False
        while not access:


            test_name = input("Enter test name: \n").strip()

            if not test_name.isalpha():
                raise ValueError("Test name must be alphanumeric")

            InputValidator.is_test_name_exist(test_name, Test_type.types)

            test_lower_bound = float(input("Enter test lower bound, if no lower bound exists, enter -1: \n")).strip()
            test_upper_bound = float(input("Enter test upper bound: if no upper bound exists, enter -1: \n")).strip()


            if (test_lower_bound == '-1') and (test_upper_bound == '-1'):
                print("you should input at least one bound\n")
                continue

            if not InputValidator.are_bounds_consistent(test_lower_bound, test_upper_bound):
                print("The lower bound should be less than the upper bound\n")

            test_unit = input("Enter test unit: \n").strip()

            if not test_name.isalpha():
                print("please enter a test unit\n")
                continue

            test_period = input("Enter test period in the format days-hours-minutes (dd-hh-mm): \n").strip()

            if not InputValidator.is_period_valid(test_period):
                print("please enter a valid test period\n")
                continue

            file_input_string = ''
            if test_lower_bound != '-1' and test_upper_bound != '-1':

                new_test = Test_type(name=test_name, range1=test_lower_bound, range2=test_upper_bound, unit=test_unit,
                                     period=test_period)

            elif test_lower_bound == '-1':
                new_test = Test_type(name=test_name, range2=test_upper_bound, unit=test_unit,
                                     period=test_period)
            else:
                new_test = Test_type(name=test_name, range1=test_lower_bound, unit=test_unit,
                                     period=test_period)

            record_file = open('medicalTest.txt', 'a')
            record_file.write(str(new_test))
            record_file.close()

            Test_type.types[test_name] = new_test
            access = True

    @staticmethod
    def insert_medical_record():
        test_status_list = ["Pending", "Completed", "Reviewed"]
        access = False

        while not access:

            try:
                patient_id = input("Enter patient patient ID: \n").strip()
                InputValidator.is_patient_id_valid(patient_id)
                ConsolePrinter.print_test_names()
                print()
                test_name = input("Enter the test you want:\n").strip()
                InputValidator.is_test_name_valid(test_name, Test_type.types)
                test_result = input("Enter test result: \n").strip()
                InputValidator.isfloat(test_result)
                ConsolePrinter.print_available_test_states()
                print()

                test_status_number = input("Enter test status number from the list above:\n").strip()
                InputValidator.is_test_status_number_valid(test_status_number)

                test_date_start = input("Enter test date time in the format YYYY-MM-DD hh:mm : \n").strip()
                test_date_end = None
                InputValidator.is_date_time_valid(test_date_start)

                test_status = test_status_list[int(test_status_number) - 1]

                if test_status == "Completed":
                    test_date_end = input("Enter test date time in the format YYYY-MM-DD hh:mm : \n").strip()
                    InputValidator.is_date_time_valid(test_date_end)

            except ValueError as e:
                print(f"Error : {e}. Try again.")
                continue


            # add the new patient into the dictionary
            if patient_id not in Patient.patients:
                patient = Patient(id=patient_id)
                Patient.patients[patient_id] = patient

            test_unit = Test_type.types[test_name].unit
            test = Test(name=test_name, unit=test_unit, status=test_status, result=test_result,
                        date_start=test_date_start, date_end=test_date_end)
            Patient.patients[patient_id].add_test(test)

            record_file = open('medicalRecord.txt', 'a')
            record_file.write(f"{patient_id}: {str(test)}")
            record_file.close()

            access = True
            # test_name = tests_list.split("- ")[int(test_status_number)][1]
            # test_status = test_states_list("- ")[int(test_status_number)][1]

            #if test_status == "Completed":
            #continue from here
