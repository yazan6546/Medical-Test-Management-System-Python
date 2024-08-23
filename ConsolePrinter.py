from Patient import Patient
from Test_type import Test_type


class ConsolePrinter:
    @staticmethod
    def print_available_test_states():
        print ("""Test states:
        1- Pending\n
        2- Completed\n
        3- Reviewed""")

    @staticmethod
    def print_filter_menu():
        print("""Enter one or a combination of these conditions:

1• Patient ID, 
2• Test Name, 
3• Abnormal tests, 
4• Test added to the system within a specific period (start and end dates), 
5• Test status, 
6• Test turnaround time within a period (minimum and maximum turnaround time)\n""")


    @staticmethod
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

    @staticmethod
    def print_test_names():

        for count, test_name in enumerate(Test_type.types.keys()):
            print(f"{count+1}) {test_name}")

    @staticmethod
    def print_test_file():
        for count, test in enumerate(Test_type.types.values()):
            print(f"{count+1}) {test}")

    @staticmethod
    def print_record_file(list_patients=Patient.patients.values()):
        number = 1

        if len(list_patients) == 0:
            print("No records that match these criteria")
            return

        for patient in list_patients:
            number = patient.print_patients_with_numbering(number)

        return number

