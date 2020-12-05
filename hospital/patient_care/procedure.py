class Procedure:
    proceduresList = list()
    #ProcedureFrequency= {'hourly':1,'daily':24,'weekly':7*24,'Monthly':30*24,'Annual':365.25*24}

    def __init__(self, procedure_name, base_procedureRF = None, baseProcedureCost = 0, avglengthOfCare = 1):
        
        '''
        __init__(self, procedure_name, base_procedureRF = None, baseProcedureCost = 0, avglengthOfCare = 1):
        Returns an instance of class Procedure with a specified name, base procedure risk, base procedure cost, and average length of the procedure
        
        Args:
            precedure_name: string
            base_procedureRF: int in the range of 0 to 10 (inclusive) Default: None
            baseProcedureCost: int or float greater than zero Default: 0
            avglengthOfCare: int or float greater than zero Default: 1
        
        Return:
            An instance of the class Procedure
        '''
        
        self.procedure_name = procedure_name
        self.base_procedureRF = base_procedureRF
        self.baseProcedureCost = baseProcedureCost
        self.avglengthOfCare = avglengthOfCare
        tmpP = (self.procedure_name, self.base_procedureRF, self.baseProcedureCost, self.avglengthOfCare)
        Procedure.proceduresList.append(tmpP)
    
 
    def indProcedureRisk(self, PatientX):   
        
        '''
        indProcedureRisk(self, PatientX):
        Returns the an integer from 0 to 10 representing the risk a the procedure for a given patient

        Args:
            PatientX: An instance of the Patient class that is created using the patient.py file. Consist of the name, age and pre-existing conditions of a patient
        
        Return:
            An integer in the range of 0 and 10.

        Help on function indProcedureRisk in module __main__:

        Get patient's age
        Get patient's list of pre-exisitng conditions
        If there is some risk associated with the procedure:
            Determine the risk of the procedure for different age groups
            Add 1 to the risk factor for each pre-existing condition of the patient
            Add the base procedure risk to the risk factor
            Limit the risk factor to a maximum value of 10
        If there is no risk associated with the procedure: return 0
        '''

        tmpRF=0
        age = PatientX.age
        PreExistCond = PatientX.listPreExistCond
        if self.base_procedureRF != None:
            if age > 12 and age < 80: riskFactor = (age-10)//20
            elif age > 80: 
                riskFactor = 4
                if age > 90: riskFactor = 5
            elif age > 3: riskFactor = 5
            else: riskFactor = 3
            if PreExistCond != None: 
                for row in PreExistCond: tmpRF+=1
                if tmpRF > 3: tmpRK=3
            riskFactor+=tmpRF
            riskFactor+=self.base_procedureRF

            if riskFactor > 10: riskFactor=10
            return riskFactor
        else: 
            return 0
           # print("The risk factor for a",self.procedure_name,"is",riskFactor,".")

    def expectedTotalProcedureCost(self, PatientY):

        '''
        expectedTotalProcedureCost(self, PatientY):

        Args:
            PatientY: An instance of the Patient class that is created using the patient.py file. Consist of the name, age and pre-existing conditions of a patient
        
        Return:
            An integer that is greater than 0.

        Help on function indProcedureRisk in module __main__:

        Predefine the values for avgNurseSalary as 40
        Predefine the values for avgNursePatientRatio as 1/5
        Predefine the values for avgPhysicianSalary as 80
        Predefine the values for avgPhysicianPatientRatio as 1/20

        Get the risk factor for a patient giving the specified procedure
        If the risk factor is greater than 7, the procedure is not conducted: Return a string.
        else: determine the length of care based off of the risk factor (avgLengthOfCareFactor)
            Calculate the total cost (base_procedure cost + avg_length_care*staffing_cost*avgLengthOfCareFactor)
        '''

        avgNurseSalary = 40
        avgNursePatientRatio = 1/5
        avgPhysicianSalary = 80
        avgPhysicianPatientRatio = 1/20

        riskFactorProc = int(self.indProcedureRisk(PatientY))

        if riskFactorProc > 7:
            return "Procedure risk is too high risk. Procedure will not proceed."
            #totalProcedureCost = ''
        else:
            if riskFactorProc > 6: avgLengthOfCareFactor = 2
            elif riskFactorProc > 4: avgLengthOfCareFactor = 1
            elif riskFactorProc > 2: avgLengthOfCareFactor = 0.8
            else: avgLengthOfCareFactor = 0.6

            totalProcedureCost = self.baseProcedureCost + self.avglengthOfCare*     (avgNursePatientRatio*avgNurseSalary + avgPhysicianPatientRatio*avgPhysicianSalary)*avgLengthOfCareFactor

            return int(totalProcedureCost)

    def display_ProcedureList(self):

        '''
        display_ProcedureList(self):
        Return a all procedures

        Return:
            Name, base risk factor, base cost of the procedure and average length of care for each procedure

        Help on function display_PatientsList in module __main__:

        Displays the following for each procedure:
            Name
            Base risk factor
            Average procedure cost
            Average length of care
        '''

        print("List of procedures:")
        print("--------------------")
        for row in Procedure.proceduresList:
            print('Procedure name:',row[0])
            print('Base risk factor:',row[1])
            print('Average procedure cost:',row[2])
            print('Average length of care:',row[3])
            print("--------------------")
    
    def display_Procedure(self):

        '''
        display_Patient(self):
        Return patient

        Return:
            Name, age, service, pre-existing conditions and risk factor

        Help on function display_PatientsList in module __main__:

        Displays the following for each patient:
            Name
            Age
            Service
            Pre-exisitng conditions
            Risk factor
        '''

        print('Procedure name:', self.procedure_name,'\nBase procedure risk:',self.base_procedureRF,'\nBase procedure cost:',self.baseProcedureCost,'\nAverage length of care:',self.avglengthOfCare,'\n')