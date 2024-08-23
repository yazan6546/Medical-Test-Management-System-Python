from datetime import timedelta

import Patient
from ConsolePrinter import ConsolePrinter
from InsertionHandler import InsertionHandler
from Patient import *
from Test_type import *
from UpdateHandler import UpdateHandler


#
# Function that returns a list of filtered patient objects given the
# condition vector
#
def filter_tests(conditions):

    conditions = list(map(int, conditions.split(','))) # Convert the list of numeric strings to integers
    conditions = {i : True for i in conditions} # Convert into a dictionary for fast lookups

    # Convert the dictionary of key id and value patient to a dictionary
    # with key id and value list of tests

    filtered_dict = dict(map(lambda x : (x[0], x[1].get_tests_list()), Patient.patients.items()))

    if len(conditions) > 6:
        raise Exception("Too many conditions")

    if 1 in conditions:

        invalid = True
        while invalid:

            id = input("Enter Patient ID: \n")
            try:
                InputValidator.is_patient_id_valid(id)
                InputValidator.is_patient_id_exist(id, Patient.patients)
                invalid = False
            except ValueError as e:
                print(f"Error : {e}")
                continue

            filtered_dict.clear()
            filtered_dict = {id : Patient.patients[id].get_tests_list()}

    if 2 in conditions:
        name = input("Enter Test Name: \n")

        # Iterate over each test and filter
        for id, tests in filtered_dict.items():

            tests = list(filter(lambda x: x.name == name, tests))
            filtered_dict[id] = tests




    # Get all abnormal tests

    if 3 in conditions:
        for id, tests in filtered_dict.items():
            tests = list(filter(lambda test: test.is_abnormal(), tests))
            filtered_dict[id] = tests


    if 4 in conditions:

        invalid = True
        while invalid:

            try:
                start = input("Enter Start Date in this format : %Y-%m-%d %H:%M\n")
                start = Test.create_date(start)
                end = input("Enter End Date in this format: %Y-%m-%d %H:%M\n")
                end = Test.create_date(end)
                invalid = False

            except ValueError as e:
                print(f"Error : {e}")
                continue

            for id, tests in filtered_dict.items():
                tests = list(filter(lambda test: start < test.date_start < end, tests))
                filtered_dict[id] = tests


    if 5 in conditions:
        status = input("Enter test Status: \n")
        for id, tests in filtered_dict.items():

            tests = list(filter(lambda test: test.status == status, tests))
            filtered_dict[id] = tests

    if 6 in conditions:
        invalid = True
        while invalid:

            try:
                min = input("Enter minimum turnaround time in this format : DD-HH-MM\n")
                Utilities.is_period_valid(min)
                days, hours, minutes = min.split('-')
                time1 = timedelta(days=int(days),hours=int(hours), minutes=int(minutes))

                max = input("Enter maximum turnaround time : DD-HH-MM\n")
                Utilities.is_period_valid(max)
                days, hours, minutes = max.split('-')
                time2 = timedelta(days=int(days), hours=int(hours), minutes=int(minutes))
                invalid = False

            except ValueError as e:
                print(f"Error : {e}")
                continue

            for id, tests in filtered_dict.items():

                tests = list(filter(lambda test: test.status.lower() == 'completed'
                                                 and time1 < test.date_end - test.date_start < time2, tests))
                filtered_dict[id] = tests


    patients = list(map(lambda items : Patient(items[0], items[1]), filtered_dict.items()))

    # Remove all patient objects with an empty list
    patients = list(filter(lambda patient : len(patient.get_tests_list()) != 0, patients))
    return patients


def print_filtered_tests(patients):

    print("\n************ Tests that match the criteria ******************\n")
    ConsolePrinter.print_record_file(patients)
    print()

def generate_report(conditions):
    patients = filter_tests(conditions)
    print_filtered_tests(patients)

    summation = Patient.get_sum(patients)
    count = Patient.get_record_num(patients)
    average = summation/count
    min = Patient.get_min_patients(patients)
    max = Patient.get_max_patients(patients)

    print("**************** Summary Report ****************\n")

    print(f"Average : {average} ")
    print(f"Min : {min} ")
    print(f"Max : {max} ")

    print()



def main():

    Test_type.import_tests()
    Patient.import_records()


    while True:

        ConsolePrinter.show_menu()
        option = int(input("\nChoose your option.\n\n"))

        if option == 1:
            ConsolePrinter.print_test_file()
            print()

        if option == 2:
            ConsolePrinter.print_record_file()
            print()

        if option == 3:
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
            patients = filter_tests(conditions)
            print_filtered_tests(patients)

        elif option == 8:
            ConsolePrinter.print_filter_menu()
            conditions = input("Enter conditions in this format : 1, 2, ...\n")
            generate_report(conditions)




if __name__ == '__main__':
    main()
