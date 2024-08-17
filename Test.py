import datetime
from copy import copy, deepcopy

from Test_type import Test_type


class Test:

    Test = {}
    def __init__(self, name, status, unit, date_start, date_end=None, result=None):
        self.name = name
        self.status = status
        self.date_start = deepcopy(date_start)
        self.unit = unit
        self.result = float(result)

        if status.lower() == 'completed':
            self.date_end = deepcopy(date_end)

        elif status.lower() != 'reviewed' and status.lower() != 'pending':
            raise Exception('Invalid status : ' + status)

    def __str__(self):
        test =  f"%s, %s, %f, %s, %s" % (self.name, self.date_start, self.result, self.unit, self.status)
        if self.status == 'completed':
            test += f", %s" % self.date_end
        return test


    @staticmethod
    def create_test(record):

        array = record.split(',')
        name = str(array[0].strip())

        start = array[1].strip()
        start = Test.create_date(start)

        result = float(array[2].strip())
        unit = str(array[3].strip())
        status = str(array[4]).strip()

        if len(array) > 5:

            end = str(array[5].strip())
            end = Test.create_date(end)

            test = Test(name=name, status=status, unit=unit, date_start=start, date_end=end, result=result)
        else:
            test = Test(name=name, status=status, unit=unit, date_start=start, result=result)

        return test

    @staticmethod
    def create_date(date_string):
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')
        return date



    def is_abonormal(self):
        range1 = Test_type.types[self.name].range1 # get the normal range of this test
        range2 = Test_type.types[self.name].range2

        if range1 is not None and range2 is not None:
            return self.result < range1 or self.result > range2
        elif range1 is not None and range2 is None:
            return self.result < range1
        elif range1 is None and range2 is not None:
            return self.result > range2


