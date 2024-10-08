import datetime

from InputValidator import InputValidator
from Test_type import Test_type


class Test:

    def __init__(self, name, status, unit, date_start, date_end=None, result=None):

        self.name = name
        self.status = status
        self.unit = unit
        self.result = result
        self.__date_end = None
        self.date_start = date_start
        if status.lower() == 'completed':
            self.date_end = date_end


    def __str__(self):
        test = f"%s, %s, %.1f, %s, %s" % (
        self.name, self.date_start.strftime("%Y-%m-%d %H:%M"), self.result, self.unit, self.status)
        if self.status.lower() == 'completed':
            test += f", %s" % self.date_end.strftime("%Y-%m-%d %H:%M")
        return test

    @property
    def name(self):
        return self.__name.upper()

    @name.setter
    def name(self, name):
        InputValidator.is_test_name_valid_2(name, Test_type.types)
        self.unit = Test_type.types[name.upper()].unit
        self.__name = name.upper()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        InputValidator.is_test_status_valid(status)
        self.__status = status
        if status.lower() != 'completed':
            self.__date_end = None

    @property
    def date_start(self):
        return self.__date_start

    @date_start.setter
    def date_start(self, date_start):
        date = datetime.datetime.strptime(date_start, '%Y-%m-%d %H:%M')

        if self.status.lower() == 'completed':
            self.__date_end = None

        if date > datetime.datetime.now():
            raise ValueError("Date cannot be in the future")

        if self.__date_end is not None and self.status.lower() == "completed" and date > self.__date_end:
            raise ValueError("start date cannot be higher than end date")
        elif self.__date_end is not None and self.status.lower() == "completed" and date == self.__date_end:
            raise ValueError("start date cannot be equal to end date")

        self.__date_start = date

    @property
    def date_end(self):

        return self.__date_end

    @date_end.setter
    def date_end(self, date_end):
        date = datetime.datetime.strptime(date_end, '%Y-%m-%d %H:%M')

        if date > datetime.datetime.now():
            raise ValueError("Date cannot be in the future")

        if date < self.date_start:
            raise ValueError("start date cannot be higher than end date")
        elif date == self.date_start:
            raise ValueError("start date cannot be equal to end date")

        self.__date_end = date

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        self.__result = float(result)

    @property
    def turnaround(self):

        if self.status.lower() == 'completed':
            return self.date_end - self.date_start
        else:
            return None

    @staticmethod
    def create_date(date):
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
        return date

    @staticmethod
    def create_test(record):

        array = record.split(',')
        name = str(array[0].strip())

        start = str(array[1].strip())

        result = float(array[2].strip())
        unit = str(array[3].strip())
        status = str(array[4]).strip()

        if len(array) > 5:

            end = str(array[5].strip())

            test = Test(name=name, status=status, unit=unit, date_start=start, date_end=end, result=result)
        else:
            test = Test(name=name, status=status, unit=unit, date_start=start, result=result)

        return test

    def get_test_NA_for_DNE(self):
        test = f"%s, %s, %.1f, %s, %s" % (
        self.name, self.date_start.strftime("%Y-%m-%d %H:%M"), self.result, self.unit, self.status)
        if self.status.lower() == 'completed':
            test += f", %s" % self.date_end.strftime("%Y-%m-%d %H:%M")
        else:
            test += ", N/A"
        return test

    def is_abnormal(self):
        range1 = Test_type.types[self.name].range1  # get the normal range of this test
        range2 = Test_type.types[self.name].range2

        if range1 is not None and range2 is not None:
            return self.result < range1 or self.result > range2
        elif range1 is not None and range2 is None:
            return self.result < range1
        elif range1 is None and range2 is not None:
            return self.result > range2
