from Test import *

class Patient:
    def __init__(self, id):
        self.__tests = []
        self.id = id


    def add_test(self, test):
        self.__tests.append(test)
    def delete_test(self, test):
        self.__tests.remove(test)
    
