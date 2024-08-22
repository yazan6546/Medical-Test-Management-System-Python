from Patient import *
from Test import *
from Utilities import Utilities


def filter_tests(conditions):
    tests = Patient.patients
    if len(conditions) > 6:
        raise Exception("Too many conditions")

    for i in conditions:
        if i > 6 or i < 0:
            raise Exception("Invalid condition")
        if i == 0:
            id = int(input("Enter Patient ID: \n"))
            tests = tests[id].tests
        elif i == 1:
            name = input("Enter Patient Name: \n")
            tests = list(filter(lambda x: x.name == name, tests))
        elif i == 2:
            tests = list(filter(lambda test: test.is_abnormal, tests))
        elif i == 3:
            start = input("Enter Start Date in this format : %Y-%m-%d %H:%M\n")
            start = Test.create_date(start)
            end = input("Enter End Date in this format: %Y-%m-%d %H:%M\n")
            end = Test.create_date(end)
            tests = list(filter(lambda test: start < test.date_start < end, tests))

        elif i == 4:
            status = input("Enter test Status: \n")
            tests = list(filter(lambda test: test.status == status, tests))


def show_menu():
    print("""--------Medical Test Management System-------

1• Add new medical test.
2• Add a new medical test record.
3• Update patient records including all fields.
4• Update medical tests in the medicalTest file.
5• Filter medical tests based on multiple conditions.
6• Generate textual summary reports.
7• Export medical records to a comma separated file.
8• Import medical records from a comma separated file.""")


def main():
    while True:

        show_menu()
        option = int(input("\nChoose your option.\n\n"))

        if option == 1:
            continue

        if option == 5:
            print("""Enter one or a combination of these conditions:
            
1• Patient ID, 
2• Test Name, 
3• Abnormal tests, 
4• Test added to the system within a specific period (start and end dates), 
5• Test status, 
6• Test turnaround time within a period (minimum and maximum turnaround time)\n""")

            print("Enter conditions in this format : 1, 2, ...")
            conditions = input().split()
            filter_tests(conditions)


if __name__ == '__main__':
    main()
