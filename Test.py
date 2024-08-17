from pkgutil import resolve_name


class Test:

    Test = {}
    def __init__(self, name, status, unit, date_start, date_end=None, result=None):
        self.name = name
        self.status = status
        self.date_start = date_start
        self.unit = unit
        self.result = result

        if status.lower() == 'completed':
            self.date_end = date_end

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
        result = float(array[2].strip())
        unit = str(array[3].strip())
        status = str(array[4]).strip()

        if len(array) > 5:
            end = str(array[5].strip())
            test = Test(name=name, status=status, unit=unit, date_start=start, date_end=end, result=result)
        else:
            test = Test(name=name, status=status, unit=unit, date_start=start, result=result)

        return test




    # def is_abonormal(self):
    #     if self.result is not None and self.result:
    #         return True
    #     if self.result is not None and self.result
    #         return True
    #     else:
    #         return False

