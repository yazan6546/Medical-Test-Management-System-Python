from Patient import Patient
from Test import Test

class csv_read:

    @staticmethod
    def export_to_csv(name):
        headers = "ID, Test Name, Start Date, Result, Unit, Status, End Date\n"
        string = Patient.get_patients_without_numbering_CSV()

        # Read the entire file into a string
        with open(f'{name}.csv', 'w') as file:
            file.write(headers)
            file.writelines(string)

    @staticmethod
    def import_from_csv(name):
        Patient.patients.clear()
        # Read the entire file into a string

        try:
            with open(f"{name}.csv", 'r') as file:
                content = file.read()

        except FileNotFoundError:
            print(f"File {name}.csv does not exist\n")

        # Split content based on the first delimiter ':'
        records = content.split('\n')
        records = list(filter(lambda x: x != '', records))

        for record in records[1:]:
            data = record.split(',')
            print(data)
            id = data[0].strip()
            data = ",".join(data[1:]).strip()
            if id not in Patient.patients:
                Patient.add_patient(id)
            test = Test.create_test(data)
            Patient.patients[id].add_test(test)

        # for patient in Patient.patients.values():
        #     print(patient.id)


