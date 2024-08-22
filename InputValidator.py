from datetime import datetime


class InputValidator:

    @staticmethod
    def is_patient_id_valid(patient_id):
        if not patient_id.isnumeric() or not len(patient_id) == 7:
            raise ValueError("Patient ID is invalid")

    @staticmethod
    def is_test_name_valid(test_name, types):
        if  test_name not in types:
            raise ValueError("Test name is invalid")

    @staticmethod
    def is_test_number_valid(test_number, types):
        if not test_number.isnumeric() or not 1 <= int(test_number) <= len(types):
            raise ValueError("Test number is invalid")


    @staticmethod
    def is_date_time_valid(date_time):
        date_time_format = '%Y-%m-%d %H:%M'
        datetime.strptime(date_time, date_time_format)

    @staticmethod
    def is_test_status_number_valid(test_status):
        if not test_status.isnumeric() or not 3 >= int(test_status) > 0:
            raise ValueError("Test status is invalid")
