class Test:

    Test = {}
    def __init__(self, name, status, unit, date_start, date_end=None, result=None):
        self.name = name
        self.status = status
        self.date_start = date_start
        self.date_end = date_end
        self.unit = unit
        self.result = result
        if status == 'completed':
            self.date_end = date_end

        elif status != 'reviewed' or status != 'pending':
            raise Exception('Invalid status')

        Test[name] = True

    @staticmethod
    def create_test(record):

        array = record.split(',')
        name = array[0]
        start = array[1]
        result = array[2]
        unit = array[3]
        status = array[4]

        if len(array) > 5:
            end = array[5]
            test = Test(name, status, unit, start, end, result)
        else:
            test = Test(name, status, unit, start, result)

        return test




    # def is_abonormal(self):
    #     if self.result is not None and self.result:
    #         return True
    #     if self.result is not None and self.result
    #         return True
    #     else:
    #         return False

