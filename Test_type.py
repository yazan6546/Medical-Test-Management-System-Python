from InputValidator import InputValidator

class Test_type:

    types = {}
    def __init__(self, unit, period, name, range1=None, range2=None):

        self.__range1 = None
        self.__range2 = None

        if range1 is not None:
            self.range1 = range1
        if range2 is not None:
            self.range2 = range2
        if range1 is None and range2 is None:
            raise Exception("You must specify either range1 or range2")

        self.__period = period
        self.__unit = unit
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        InputValidator.is_test_name_valid(value, Test_type.types)
        self.__name = value

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value):
        InputValidator.is_period_valid(value)
        self.__period = value

    @property
    def range1(self):
        return self.__range1

    @range1.setter
    def range1(self, value):
        self.__range1 = float(value)


    @property
    def range2(self):
        return self.__range2

    @range2.setter
    def range2(self, value):
        self.__range2 = float(value)

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        if not str(value).isalpha():
            raise ValueError("You must specify a valid unit")
        self.__unit = value


    def __str__(self):

        test = f"%s;" % self.name
        if self.__range1 is not None and self.__range2 is not None:
            test += f">%.1f,<%.1f;" % (float(self.range1), float(self.range2))
        elif self.__range1 is None:
            test += f"<%.1f; " % self.range2
        elif self.__range2 is None:
            test += f">%.1f;" % self.range1

        test += f"%s;%s" % (self.unit, self.period)

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


            ranges = range.split(',')
            if len(ranges) == 2:
                range1 = ranges[0][1::]
                range2 = ranges[1][1::]
                Test_type.types[name] = Test_type(range1=range1, unit=unit, range2=range2, period=period, name=name)
            elif len(ranges) == 1 and ranges[0][0] == '>':
                range1 = ranges[0][1::]
                Test_type.types[name] = Test_type(range1=range1, unit=unit, period=period, name=name)
            elif len(ranges) == 1 and ranges[0][0] == '<':
                range2 = ranges[0][1::]
                Test_type.types[name] = Test_type(range2=range2, unit=unit, period=period, name=name)

            else:
                raise Exception('Wrong number of ranges')