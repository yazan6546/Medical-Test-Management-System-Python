class Test:
    def __init__(self, name, status, range1, date_start, duration, date_end=None,  range2=None, result=None):
        self.name = name
        self.status = status
        self.date_start = date_start
        self.duration = duration
        self.date_end = date_end
        if range1 > range2:
            self.range1 = range2
            self.range2 = range1

        self.range1 = range1
        self.range2 = range2

        self.result = result
        if status == 'completed':
            self.date_end = date_end

        elif status != 'reviewed' or status != 'pending':
            raise Exception('Invalid status')

    def is_abonomal(self):
        if self.range2 is None and self.result is not None and self.result < self.range1:
            return True
        if self.range2 is not None and self.result is not None and self.result > self.range2 or self.result < self.range1:
            return True
        else:
            return False
