import re
from token import RARROW


class Utilities:
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





