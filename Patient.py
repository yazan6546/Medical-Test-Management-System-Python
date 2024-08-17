from Test import *

class Patient:

    patients = {}

    def __init__(self, id):
        self.__tests = []
        self.id = id


    def add_test(self, test):
        self.__tests.append(test)
    def delete_test(self, test):
        self.__tests.remove(test)

    def print_tests(self):
        for i in self.__tests:
            print(i)

    def __str__(self):
        return '\n'.join(map(str,self.__tests))

    @staticmethod
    def import_records():
        # Read the entire file into a string
        with open('medicalRecord.txt', 'r') as file:
            content = file.read()

        # Split content based on the first delimiter ':'
        records = content.split('\n')

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