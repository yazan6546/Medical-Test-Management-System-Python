import re
from datetime import datetime

class InputValidator:

    @staticmethod
    def is_patient_id_valid(patient_id):
        if not patient_id.isnumeric() or not len(patient_id) == 7:
            raise ValueError("Patient ID is invalid")

    @staticmethod
    def is_patient_id_exist(patient_id, dict):
        if patient_id not in dict:
            raise ValueError("Patient ID is non-existent")

    @staticmethod
    def is_test_name_valid(test_name, types):
        if  test_name.upper() in types:
            raise ValueError(f"Test name {test_name} already exists.")
        elif not test_name.isalpha():
            raise ValueError(f"Test name {test_name} is invalid.")

    @staticmethod
    def is_test_name_valid_2(test_name, types):
        if test_name.upper() not in types:
            raise ValueError(f"Test name {test_name} does not exist.")
        elif not test_name.isalpha():
            raise ValueError(f"Test name {test_name} is invalid.")

    @staticmethod
    def is_test_number_valid(test_number, types):
        if not test_number.isnumeric() or not 1 <= int(test_number) <= len(types):
            raise ValueError("Test number is invalid")

    @staticmethod
    def is_test_record_number_valid(test_number, record_numbers):
        if not test_number.isnumeric() or not 1 <= int(test_number) <= record_numbers:
            raise ValueError("Test number is invalid")


    @staticmethod
    def is_date_time_valid(date_time):
        date_time_format = '%Y-%m-%d %H:%M'
        date_time = datetime.strptime(date_time, date_time_format)

        if date_time > datetime.now():
            raise ValueError("Date cannot be in the future")

    @staticmethod
    def is_test_status_number_valid(test_status):
        if not test_status.isnumeric() or not 3 >= int(test_status) > 0:
            raise ValueError("Test status is invalid")

    @staticmethod
    def is_test_status_valid(test_status):
        if (str(test_status).lower() != 'completed'
            and str(test_status).lower() != 'reviewed'
            and str(test_status).lower() != 'pending'):

            raise ValueError("Test status is invalid")

    @staticmethod
    def is_range_valid(range):
        try:
            float(range)
        except ValueError:
            raise ValueError("Range is invalid")
        if float(range) < 0:
            raise ValueError("Range should be greater than or equal to zero")



    @staticmethod
    def isfloat(num):
        try:
            float(num)
        except ValueError:
            raise ValueError("Invalid floating point number.")

    @staticmethod
    def is_period_valid(period):
        if not re.match(r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9]", period):
            raise ValueError("Invalid period. It does not match the pattern DD-HH-MM.")

        time = period.split("-")
        hours = int(time[1])
        minutes = int(time[2])

        if hours > 23 or minutes > 59:
            raise ValueError("Invalid period. Hours should be less than 24 and minutes should be less than 60.")

        return True

    @staticmethod
    def are_bounds_consistent(lower_bound, upper_bound):

        if lower_bound == -1 or upper_bound == -1:
            return True

        lower_bound = float(lower_bound)
        upper_bound = float(upper_bound)
        if lower_bound > upper_bound:
            raise ValueError("Lower bound should be less than upper bound.")
        return True

    @staticmethod
    def is_match_pattern(string):
        if not re.match(r'^(?:[1-6](?:,[1-6])*)?$', string):
            raise ValueError("Invalid pattern. It does not match the pattern 1, 2, 3...")





