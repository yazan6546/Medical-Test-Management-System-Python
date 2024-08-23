from datetime import *

import Test
from ConsolePrinter import ConsolePrinter
from Patient import Patient
from Test_type import Test_type

Patient.import_records()
print(ConsolePrinter.print_record_file())