class ConsolePrinter:
    @staticmethod
    def print_enter_available_test_states():
        return ("""Test states:
        1- Pending\n
        2- Completed\n
        3- Reviewed""")

    @staticmethod
    def print_test_names():
        with open('medicalTest.txt', 'r') as file:
            content = file.read()

        content_list = content.split('\n')
        test_name_list = "Available tests: \n"
        i = 1
        for test in content_list:
            content_list += f"{i}- {test.split(';')[0]}\n"
            i = i+1

        file.close()
        return test_name_list

