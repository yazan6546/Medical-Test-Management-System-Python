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
    def print_test_names():

        for count, test_name in enumerate(Test_type.types.keys()):
            print(f"{count+1}) {test_name}")

    @staticmethod
    def print_test_file():
        for count, test in enumerate(Test_type.types.values()):
            print(f"{count+1}) {test}")

    @staticmethod
    def print_record_file():
        number = 1
        for patient in Patient.patients.values():
            number = patient.print_patients_with_numbering(number)

        return number

