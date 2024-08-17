from Patient import Patient
from Test import *

patients = {}
def add_patient(id):
    patient = Patient(id)
    patients[id] = patient



def remove_patient(patient):
    patients.pop(patient.id)

def show_menu():
    print("""--------Medical Test Management System-------

1• Add new medical test.
2• Add a new medical test record.
3• Update patient records including all fields.
4• Update medical tests in the medicalTest file.
5• Filter medical tests.
6• Generate textual summary reports.
7• Export medical records to a comma separated file.
8• Import medical records from a comma separated file.""")


def main():
    show_menu()

    # Read the entire file into a string
    with open('medicalRecord.txt', 'r') as file:
        content = file.read()

    # Split content based on the first delimiter ':'
    records = content.split('\n')

    for record in records:
        id = record.split(':', 1)[0].strip()
        data = record.split(':', 1)[1].strip()
        print(data)
        if id not in patients:
            add_patient(id)
        test = Test.create_test(data)
        patients[id].add_test(test)

    for patient in patients.values():
        print(patient.id)


if __name__ == '__main__':

    main()