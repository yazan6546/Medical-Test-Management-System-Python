from Patient import *
from Test import *

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

    while True:

        show_menu()
        print("Choose your option.")
        option = int(input("enter your choice: "))

        if option == 1:
            continue





if __name__ == '__main__':

    main()