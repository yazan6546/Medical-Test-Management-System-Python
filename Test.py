class Test:

    Test = {}
    def __init__(self, name, status, unit, date_start, date_end=None, result=None):
        self.name = name
        self.status = status
        self.date_start = date_start
        self.unit = unit
        self.result = result

        if status == 'completed':
            self.date_end = date_end

        elif status != 'reviewed' and status != 'pending':
            raise Exception('Invalid status : ' + status)


    @staticmethod
    def create_test(record):

        array = record.split(',')
        name = str(array[0].strip())
        start = array[1].strip()
        result = float(array[2].strip())
        unit = array[3].strip().strip
        status = str(array[4]).strip()

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

