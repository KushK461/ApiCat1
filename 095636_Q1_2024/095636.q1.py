class Hospital:
    def __init__(self):
        self.name = ""
        self.age = ""
        self.illness = ""

#defining function for adding a patient
def add_patient(name, age, illness):

        patient = {
            'name' : name,
            'age' : age,
            'illness' : illness
        }
def patient_list (patient_list):
    patient_list.append(patient)
    print(f"Patient added!")

def display_patients(patient_list):
    for patient in patient_list:
        print(f"name: {patient['name']}, Age; {patient['Age']}, illness:{patient['illness']}")

    else:
        print("Patient does not exist")

def search_patient_by_name(name, patient_list):
    for patient in patient_list:
        if patient['name'] == name:
            print(f"Name: {patient[name]}, Age; {patient['Age']}, illness:{patient['illness']}")
            return
        print(f"Patient '{name}' unavailable")

def remove_patient_by_name(name, patient_list):
    for patient in patient_list:
        if patient['name'] == name:
            patient_list.remove(patient)
            print(f" '{name}' has been removed")
            return
        print("Patient '{name}' not in list,try another name")


