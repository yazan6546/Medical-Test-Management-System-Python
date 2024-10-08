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

            try:
                test_name = input("Enter test name: \n").strip()

                InputValidator.is_test_name_valid(test_name, Test_type.types)

                test_lower_bound = input("Enter test lower bound, if no lower bound exists, enter -1: \n").strip()
                InputValidator.is_range_valid(test_lower_bound)
                test_upper_bound = input("Enter test upper bound: if no upper bound exists, enter -1: \n").strip()
                InputValidator.is_range_valid(test_upper_bound)

                if (test_lower_bound == '-1') and (test_upper_bound == '-1'):
                    raise ValueError("you should input at least one bound\n")

                InputValidator.are_bounds_consistent(test_lower_bound, test_upper_bound)
                test_unit = input("Enter test unit: \n").strip()

                if test_unit.isnumeric():
                    raise ValueError("Enter a valid test unit\n")

                test_period = input("Enter test period in the format days-hours-minutes (dd-hh-mm): \n").strip()

                InputValidator.is_period_valid(test_period)

            except ValueError as e:
                print(f"Error : {e} \n")
                continue

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

            Test_type.types[test_name.upper()] = new_test
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
                InputValidator.is_test_name_valid_2(test_name, Test_type.types)
                test_result = input("Enter test result: \n").strip()
                InputValidator.is_result_valid(test_result)
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
                    if test_date_start >= test_date_end:
                        raise ValueError("end test date should be greater than start test date")

            except ValueError as e:
                print(f"Error : {e}. Try again.\n")
                continue


            # add the new patient into the dictionary
            if patient_id not in Patient.patients:
                patient = Patient(id=patient_id)
                Patient.patients[patient_id] = patient

            test_unit = Test_type.types[test_name.upper()].unit
            test = Test(name=test_name, unit=test_unit, status=test_status, result=test_result,
                        date_start=test_date_start, date_end=test_date_end)
            Patient.patients[patient_id].add_test(test)

            record_file = open('medicalRecord.txt', 'a')
            record_file.write(f"\n{patient_id}: {str(test)}")
            record_file.close()

            access = True
            # test_name = tests_list.split("- ")[int(test_status_number)][1]
            # test_status = test_states_list("- ")[int(test_status_number)][1]

            #if test_status == "Completed":
            #continue from here
