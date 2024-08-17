class Test_type:

    types = {}

    def __init__(self, unit, range1=None, range2 = None):
        if range1 is not None:
            self.range1 = range1
        if range2 is not None:
            self.range2 = range2
        if range1 is None and range2 is None:
            raise Exception("You must specify either range1 or range2")

        self.unit = unit

    @staticmethod
    def import_tests():
        # Read the entire file into a string
        with open('medicalTest.txt', 'r') as file:
            content = file.read()

        # Split content based on the first delimiter ':'
        tests = content.split('\n')
        tests = list(filter(lambda x : x != '', tests))
        for test in tests:
            print(test)
            columns = test.split(';')
            name = columns[0].strip()
            range = columns[1].strip()
            unit = columns[2].strip()

            ranges = range.split(',')
            if len(ranges) == 2:
                range1 = ranges[0][1::]
                range2 = ranges[1][1::]
                Test_type.types[name] = Test_type(range1=range1, unit=unit, range2=range2)
            elif len(ranges) == 1:
                range1 = ranges[0][1::]
                Test_type.types[name] = Test_type(range1=range1, unit=unit)

            else:
                raise Exception('Wrong number of ranges')