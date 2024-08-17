from Patient import Patient
from Test import *

patients = {}

def show_menu():
    print("""--------Medical Test Management System-------

1• Add new medical test.
2• Add a new medical test record.
3• Update patient records including all fields.
4• Update medical tests in the medicalTest file.
5• Filter medical tests.
6• Generate textual summary reports.
7• Export medical records to a comma separated file.
8• Import medical records from a comma separated file.""")


def main():
    show_menu()


if __name__ == '__main__':

    main()