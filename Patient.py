from InputValidator import InputValidator
from Test import *

class Patient:

    patients = {}

    def __init__(self, id, tests=None):
        self.__id = None

        # If the default argument were [] it would cause
        # all patient objects to have the same list
        # as it is mutable. This is a workaround

        self.__tests = tests if tests is not None else []
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        InputValidator.is_patient_id_valid(id)
        self.__id = id

    def add_test(self, test):
        self.__tests.append(test)
    def delete_test(self, test):
        self.__tests.remove(test)

    def print_tests(self):
        for i in self.__tests:
            print(i)

    def get_test(self, index):
        return self.__tests[index]

    def get_test_numbers(self):
        return len(self.__tests)

    def get_tests_list(self):
        return self.__tests

    def __str__(self):
        return '\n'.join(map(lambda x : f"{x[0] + 1}) {self.id}: {str(x[1])}", enumerate(self.__tests)))

    def print_patients_with_numbering(self, start_number=1):
        # Use map to create the lines with numbering
        numbered_lines = map(
            lambda i_record: f"{start_number + i_record[0]}) {self.id}: {i_record[1]}",
            enumerate(self.__tests)
        )

        # Join the lines and print
        print("\n".join(numbered_lines))

        # Return the next starting number
        return start_number + len(self.__tests)

    @staticmethod
    def import_records():

        Patient.patients.clear()
        # Read the entire file into a string
        with open('medicalRecord.txt', 'r') as file:
            content = file.read()

        # Split content based on the first delimiter ':'
        records = content.split('\n')
        records = list(filter(lambda x : x != '', records))

        for record in records:
            id = record.split(':', 1)[0].strip()
            data = record.split(':', 1)[1].strip()
            if id not in Patient.patients:
                Patient.add_patient(id)
            test = Test.create_test(data)
            Patient.patients[id].add_test(test)

        # for patient in Patient.patients.values():
        #     print(patient.id)


    @staticmethod
    def add_patient(id):
        patient = Patient(id)
        Patient.patients[id] = patient

    @staticmethod
    def get_patient(id):
        return Patient.patients[id]

    @staticmethod
    def remove_patient(patient):
        Patient.patients.pop(patient.id)

    @staticmethod
    def convert_to_array():
        array = [(i.id, i.__tests) for i in Patient.patients.values()]
        return array

    @staticmethod
    def get_sum():

        summation = 0
        for patient in Patient.patients.values():
            tests = patient.get_tests_list()

            summation += sum(list(map(lambda x: x.result, tests)))

        return summation

    @staticmethod
    def get_record_num():
        length = 0
        for patient in Patient.patients.values():
            length += len(patient.get_tests_list())

        return length

    def get_max_tests(self):
        test =  max(self.get_tests_list(), key=lambda test : test.result)
        return test.result

    @staticmethod
    def get_max_patients():
        max_list = list(map(lambda patient : patient.get_max_tests(), Patient.patients.values()))
        print(max_list)
        return max(max_list)


