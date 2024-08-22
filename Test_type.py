from urllib.request import URLopener

from InputValidator import InputValidator
from Utilities import Utilities


class Test_type:

    types = {}

    # Validation map for error handling
    validation_map = {
        'name': InputValidator.is_test_name_valid,
        'period': Utilities.is_period_valid,
        'range1': Utilities.isfloat,
        'range2': Utilities.isfloat,
    }

    def __init__(self, unit, period, name, range1=None, range2=None):
        if range1 is not None:
            self.range1 = float(range1)
        if range2 is not None:
            self.range2 = float(range2)
        if range1 is None and range2 is None:
            raise Exception("You must specify either range1 or range2")

        self.period = period
        self.unit = unit
        self.name = name


    def __str__(self):

        test = f"%s;" % self.name
        if hasattr(self, 'range1') and hasattr(self, 'range2'):
            test += f">%.1f,<%.1f;" % (self.range1, self.range2)
        elif not hasattr(self, 'range1'):
            test += f"<%.1f; " % self.range2
        elif not hasattr(self, 'range2'):
            test += f">%.1f;" % self.range1

        test += f"%s;%s-%s-%s" % (self.unit, (self.period[0]), (self.period[1]), (self.period[2]))

        return test




    @staticmethod
    def import_tests():

        # clear the dictionary to avoid duplicates and outdated data
        Test_type.types.clear()

        # Read the entire file into a string
        with open('medicalTest.txt', 'r') as file:
            content = file.read()

        # Split content based on the first delimiter ':'
        tests = content.split('\n')

        # remove blank lines
        tests = list(filter(lambda x : x != '', tests))
        for test in tests:
            columns = test.split(';')
            name = columns[0].strip()
            range = columns[1].strip()
            unit = columns[2].strip()
            period = columns[3].strip()

            days = period.split('-')[0].strip()
            hours = period.split('-')[1].strip()
            minutes = period.split('-')[2].strip()

            ranges = range.split(',')
            if len(ranges) == 2:
                range1 = ranges[0][1::]
                range2 = ranges[1][1::]
                Test_type.types[name] = Test_type(range1=range1, unit=unit, range2=range2, period=(days, minutes, hours), name=name)
            elif len(ranges) == 1 and ranges[0][0] == '>':
                range1 = ranges[0][1::]
                Test_type.types[name] = Test_type(range1=range1, unit=unit, period=(days, minutes, hours), name=name)
            elif len(ranges) == 1 and ranges[0][0] == '<':
                range2 = ranges[0][1::]
                Test_type.types[name] = Test_type(range2=range2, unit=unit, period=(days, minutes, hours), name=name)

            else:
                raise Exception('Wrong number of ranges')