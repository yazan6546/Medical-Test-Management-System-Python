from datetime import datetime
from Test_type import Test_type


class InputValidator:

    @staticmethod
    def is_patient_id_valid(patient_id):
        return patient_id.isnumeric() and len(patient_id) == 7

    @staticmethod
    def is_test_name_valid(test_name):
        return test_name in Test_type.types

    @staticmethod
    def is_date_time_valid(date_time):
        date_time_format = '%Y-%m-%d %H:%M'
        try:
            datetime.strptime(date_time, date_time_format)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_test_status_number_valid(test_status):
        return test_status.isnumeric() and 3 >= int(test_status) > 0
