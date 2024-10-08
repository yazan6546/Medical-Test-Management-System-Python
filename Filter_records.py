from datetime import timedelta

from ConsolePrinter import ConsolePrinter
from InputValidator import InputValidator
from Patient import Patient
from Test import Test


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
        name = input("Enter Test Name: \n").upper()

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

            tests = list(filter(lambda test: test.status.lower() == status, tests))
            filtered_dict[id] = tests

    if 6 in conditions:
        invalid = True
        while invalid:

            try:
                min = input("Enter minimum turnaround time in this format : DD-HH-MM\n")
                InputValidator.is_period_valid(min)
                days, hours, minutes = min.split('-')
                time1 = timedelta(days=int(days),hours=int(hours), minutes=int(minutes))

                max = input("Enter maximum turnaround time : DD-HH-MM\n")
                InputValidator.is_period_valid(max)
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

    count = Patient.get_record_num(patients)

    if count == 0:
        return
    summation = Patient.get_sum_result(patients, "result")
    average_1 = summation/count
    min_1 = Patient.get_min_patients(patients, "result")
    max_1 = Patient.get_max_patients(patients, "result")

    for patient in patients:
        tests = list(filter(lambda test: test.status.lower() == "completed", patient.get_tests_list()))
        patient.tests = tests

    # Remove all patient objects with an empty list
    patients = list(filter(lambda patient: len(patient.get_tests_list()) != 0, patients))
    summation = Patient.get_sum_turnaround(patients)
    count = Patient.get_record_num(patients)



    if count != 0:
        average_2 = summation / count
        min_2 = Patient.get_min_patients(patients, "turnaround")
        max_2 = Patient.get_max_patients(patients, "turnaround")

    else:
        average_2 = "No completed tests"
        min_2 = "No completed tests"
        max_2 = "No completed tests"

    print("**************** Summary Report ****************\n")

    print(f"Average result: {average_1} ")
    print(f"Min result: {min_1} ")
    print(f"Max result: {max_1} \n")

    print(f"Average turnaround time: {average_2} ")
    print(f"Min turnaround time: {min_2} ")
    print(f"Max turnaround time: {max_2} \n")
