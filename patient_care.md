patient_care is a Python Package that allows a user to manage the patients and procedures in a hospital setting.
The package consists of two modules, patient.py and procedure.py. 


PATIENT.PY

The patient.py file creates different instances of patients. 
Counts the number of patients and creates a list of all of the patients. 

Args:
    name: string
    age: int
    service: string Default: None
    listPreExistCond: list of strings Default: None
    risk_factor: int Default: None


List of functions:

.display_Patient()
- Displays a patient with their name, age, service, pre-existing conditions and risk factor.

.patient_Count()
- Displays current patient count

.display_PatientsLists()
- Displays a list of patients with their name, age, service, pre-existing conditions and risk factor.

.triage_Patient()
- returns a patients risk factor and adds a patient to the waiting list along with their expected wait time.
- Determines risk factor of patient.
- Asks patient a series of predefined yes or no questions.
- Patient sorted into the wait list based on risk factor.
- Estimated/re-estimates wait time for each patient on wait list.

.display_Wait_Times_List()
- Display the list of patients on the waiting list
- Displays the patient's name, risk factor and estimated wait time

.patient_Totalcost(list_of_procedures)
Displays a table with the base, staffing and total cost for each procedure of a patient is being recommended.

Arg:
    list of procedure: List containers procedures created using the procedure.py file

- 






PROCEDURE.PY

The procedure.py file creates procedure that is to be conducted at a hospital.
Creates a list of all of the procedures at the hospital.

Args:
    name: string
    base_procedureRF: int Default: None
    baseProcedureCost: int Default: 0
    avglengthOfCare: int Default: 1


.displayProcedure()
- Display a procedure name, base risk factor, average procedure cost and average length of care 



.displayProcedureList()
- Display a procedure name, base risk factor, average procedure cost and average length of care for each procedure



.indProcedureRisk(Patient)
- Determines the risk of a procedure for a specific patient based on the age and pre-existing conditions of the patient and the base risk of the procedure

Args:
    Patient: name (string), age (int), preExistingCond (list of strings)



.expectedTotalProcedureCost(Patient)
- Determines the total cost of a procedure for a given patient
- Changes based off of procedure length and risk factor

Arg:
    Patient: name (string), age (int), preExistingCond (list of strings)
