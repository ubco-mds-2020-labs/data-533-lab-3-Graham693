patient_care is a Python Package that allows a user to manage the patients and procedures in a hospital setting.
The package consists of two modules, patient.py and procedure.py. 


PATIENT.PY

The patient.py file creates different instances of patients with their name, age, service and pre-existing conditions (optinal), counts the number of patients and creates a list of all of the patients. The patients risk factor is only displayed after the patient has been triaged.

List of functions:

.display_Patient()
- Displays a patient with their name, age, service, pre-existing conditions and risk factor.

.patient_Count()
- Displays current patient count

.display_PatientsLists()
- Displays a list of patients with their name, age, service, pre-existing conditions and risk factor.

.triage_Patient()
- returns a patients risk factor and adds a patient to the waiting list along with their expected wait time.
- The risk factor is determined by asking the patient a series of predefined yes or no questions based in one of 3 binary trees. The returned risk factor is based on the value of the end node when the search function is returned. 
- The patient is then sorted into the wait list based on his risk factor and will be placed below anyone with the same risk factor.
- A wait time is estimated/re-estimated for each patient on the wait list based on a preset function and their risk factor.

.display_Wait_Times_List()
- Display the list of patients on the waiting list
- Displays the patient's name, risk factor and estimated wait time

.patient_Totalcost(list_of_procedures)
- displays a table with the base, staffing and total cost for each procedure that a patient is being recommended. The total cost of all of the procedures is also calculated
- If the risk factor of the procedure is 8 or higher the procedure is deemed to risking will not be performed. Its costs are not added to the total costs of the patient
- Requires a list of procedures that were created using the procedure.py file as input

.displayProcedureList()
- Displays a list of all of the procedures
- Displays the name and base risk factor of the procedure

.displayProcedure()
- Display a procedure
- Display the procedures name, base procedure risk, base procedure cost and the average length of care


PROCEDURE.PY

The procedure.py file creates procedure with its name, base risk factor, base procedure cost (optional), and average length of the procedure (optional). Creates a list of all of the procedures at the hospital.

.indProcedureRisk(Patient)
- Determines the risk of a procedure for a specific patient based on the age and pre-existing conditions of the patient and the base risk of the procedure
- Requires the input of a patient created using the patient.py file

.expectedTotalProcedureCost(Patient)
- Determines the total cost of a procedure for a given patient based the risk factor of the procedure for a given patient
- Requires the input of a patient created using the patient.py file