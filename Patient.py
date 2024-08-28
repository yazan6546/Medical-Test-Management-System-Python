from datetime import timedelta

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

    @property
    def tests(self):
        return self.__tests

    @tests.setter
    def tests(self, tests):
        self.__tests = tests if tests is not None else []

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
    def get_patients_without_numbering():
        string = ""
        for patient in Patient.patients.values():
            string +=  '\n'.join(map(lambda x : f"{patient.id}: {str(x)}", patient.get_tests_list())) + "\n"

        return string

    @staticmethod
    def get_patients_without_numbering_CSV():
        string = ""
        for patient in Patient.patients.values():
            string +=  '\n'.join(map(lambda x : f"{patient.id}, {x.get_test_NA_for_DNE()}", patient.get_tests_list())) + "\n"

        return string

    @staticmethod
    def import_records():

        Patient.patients.clear()
        # Read the entire file into a string

        try:
            with open('medicalRecord.txt', 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"File medicalRecord.txt not found.")
            exit(1)

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
    def get_sum_result(patients, attr):

        summation = 0
        for patient in patients:
            tests = patient.get_tests_list()

            summation += sum(list(map(lambda x: getattr(x, attr), tests)))

        return summation

    @staticmethod
    def get_sum_turnaround(patients):

        summation = timedelta(seconds=0)
        for patient in patients:
            tests = patient.get_tests_list()

            for test in tests:
                summation += test.turnaround
        return summation


    @staticmethod
    def get_record_num(patients):
        length = 0
        for patient in patients:
            length += len(patient.get_tests_list())

        return length

    def get_max_tests(self, attr):
        test =  max(self.get_tests_list(), key=lambda test : getattr(test, attr))
        return getattr(test, attr)

    @staticmethod
    def get_max_patients(patients, attr):
        max_list = list(map(lambda patient : patient.get_max_tests(attr), patients))
        return max(max_list)


    def get_min_tests(self, attr):
        test = min(self.get_tests_list(), key=lambda test: getattr(test, attr))
        return getattr(test, attr)

    @staticmethod
    def get_min_patients(patients, attr):
        min_list = list(map(lambda patient: patient.get_min_tests(attr), patients))
        return min(min_list)







