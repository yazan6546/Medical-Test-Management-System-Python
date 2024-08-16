
patients = {}

def add_patient(patient):
    patients[patient.id] = patient

def remove_patient(patient):
    patients.pop(patient.id)


