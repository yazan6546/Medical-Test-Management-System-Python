import re


class Utilities:
    @staticmethod
    def isfloat(num):
        try:
            float(num)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_period_valid(period):
        if not re.match(r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9]", period):
            return False

        time = period.split("-")
        hours = int(time[1])
        minutes = int(time[2])

        if hours > 23 or minutes > 59:
            return False

        return True

    @staticmethod
    def are_bounds_consistent(lower_bound, upper_bound):
        lower_bound = float(lower_bound)
        upper_bound = float(upper_bound)
        if lower_bound > upper_bound:
            return False
        return True





