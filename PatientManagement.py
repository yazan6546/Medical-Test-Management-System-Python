from copy import deepcopy

import Patient
from ConsolePrinter import ConsolePrinter
from InsertionHandler import InsertionHandler
from UpdateHandler import UpdateHandler
from Patient import *
from Test_type import *
from Utilities import Utilities


def filter_tests(conditions):

    conditions = list(map(int, conditions.split(','))) # Convert the list of numeric strings to integers
    conditions = {i : True for i in conditions} # Convert into a dictionary for fast lookups

    # Convert the dictionary of key id and value patient to a dictionary
    # with key id and value list of tests

    filtered_dict = dict(map(lambda x : (x[0], x[1].get_tests_list()), Patient.patients.items()))
    print(filtered_dict)

    if len(conditions) > 6:
        raise Exception("Too many conditions")

    invalid = True
    while invalid:
        if 1 in conditions:
            id = int(input("Enter Patient ID: \n"))
            try:
                InputValidator.is_patient_id_valid(id)
                invalid = False
            except ValueError as e:
                raise Exception(f"Error : {e}")

            filtered_dict.clear()
            filtered_dict = {id, Patient.patients[id].get_tests_list()}

    if 2 in conditions:
        name = input("Enter Test Name: \n")

        # Iterate over each test and filter
        for id, tests in filtered_dict.items():

            tests = list(filter(lambda x: x.name == name, tests))
            filtered_dict[id] = tests


    # Get all abnormal tests

    if 3 in conditions:

        for id, tests in filtered_dict.items():
            tests = list(filter(lambda test: test.is_abnormal, tests))
            filtered_dict[id] = tests

    if 4 in conditions:
        start = input("Enter Start Date in this format : %Y-%m-%d %H:%M\n")
        start = Test.create_date(start)
        end = input("Enter End Date in this format: %Y-%m-%d %H:%M\n")
        end = Test.create_date(end)

        for id, tests in filtered_dict.items():
            tests = list(filter(lambda test: start < test.date_start < end, tests))

    if 5 in conditions:
        status = input("Enter test Status: \n")
        for id, tests in filtered_dict.items():

            tests = list(filter(lambda test: test.status == status, tests))
            filtered_dict[id] = tests




def show_menu():
    print("""--------Medical Test Management System-------

1• Print all Medical Tests.
2• Print all Medical Test Records.
3• Add new medical test.
4• Add a new medical test record.
5• Update patient records including all fields.
6• Update medical tests in the medicalTest file.
7• Filter medical tests based on multiple conditions.
8• Generate textual summary reports.
9• Export medical records to a comma separated file.
10• Import medical records from a comma separated file.""")


def main():

    Test_type.import_tests()
    Patient.import_records()

    while True:

        show_menu()
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
            print("""Enter one or a combination of these conditions:
            
1• Patient ID, 
2• Test Name, 
3• Abnormal tests, 
4• Test added to the system within a specific period (start and end dates), 
5• Test status, 
6• Test turnaround time within a period (minimum and maximum turnaround time)\n""")

            conditions = input("Enter conditions in this format : 1, 2, ...\n")
            filter_tests(conditions)


if __name__ == '__main__':
    main()
