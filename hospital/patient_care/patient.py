class Patient:
    count = 0
    patientsList = []
    wait_times_list = []

    def __init__(self, name, age, service = None, listPreExistCond = None, risk_factor = None):
        
        '''
        __init__(self, name, age, service = None, listPreExistCond = None, risk_factor = None)
        Returns an instance of class Patient 
        
        Args:
            name: string
            age: int greater than 0
            service: string Default: None
            listPreExistCond: list of strings Default: None
            risk_factor: int in range 0 to 10 (inclusive) Default = None 
        
        Return:
            An instance of the class Patient
        '''       
        
        self.name = name
        self.age = age
        self.service = service
        self.listPreExistCond = listPreExistCond
        self.risk_factor = risk_factor

        Patient.count +=1
        patient_variables = (self.name, self.age, self.service, self.listPreExistCond, self.risk_factor)
        Patient.patientsList.append(patient_variables)

    # Display patient 
    def display_Patient(self):
        print('Patient name:', self.name,'\nAge:',self.age,'\nService:',self.service,'\nPre-existing conditions:',self.listPreExistCond,'\nRisk factor:',self.risk_factor,'\n')

        '''
        display_Patient(self):
        Return patient

        Return:
            Name, age, service, pre-existing conditions and risk factor

        Help on function display_Patient in module __main__:

        Displays the following for each patient:
            Name
            Age
            Service
            Pre-exisitng conditions
            Risk factor
        '''

    # Print the number of patients  
    def patient_Count(self):

        '''
        patient_Count(self):
        Return the number of patients

        Return:
            Integer 

        Help on function patient_Count in module __main__:

        Return patient.count
        '''

        print("Current patient count:",Patient.count)

    #Display the list of all the patients
    def display_PatientsList(self):

        '''
        display_PatientsList(self):
        Return a all patients

        Return:
            Name, age, service, pre-existing conditions and risk factor of each patient

        Help on function display_PatientsList in module __main__:

        Displays the following for each patient:
            Name
            Age
            Service
            Pre-exisitng conditions
            Risk factor
        '''

        print("List of patients:")
        print("--------------------")
        for row in Patient.patientsList:
            print('Name:',row[0])
            print('Age:',row[1])
            print('Service:',row[2])
            print('Pre-existing Conditions:',row[3])
            print("Risk factor:", row[4])
            print("--------------------") 

    # Prompt the issues with questions about the patients condition. 
    # Returns a risk factor and an estimated wait time for the patient.
    def triage_Patient(self, wait_times_list=wait_times_list):
        '''
        triage_Patient(self, wait_times_list=wait_times_list):
        Assigns risk_factor for the specified patient and adds patient to the wait_times_list

        Returns:
            Nothing is returned
 
        Help on funtion triage_Patient in module __main__:

        Define dictionary of 3 sepate dictionaries. Each dictionary represents a binary tree of root 0. Each end node, specified by 'A' has a risk factor, otherwise they have a question ('Q')
        Ask patient to select one of the dictionaries based on what type of symptoms they have
        Create tree using triageNode class using the specified dictionary
        Search the tree. Ask question for node 0, if yes get the question in the left node, otherwise choice the right node. If node is an end node, select the risk factor
        Define the risk factor for the patient as the returned value from the tree: integer from 0 to 10
        Add patient to the wait list based on their risk factor
        Define the wait times for each patient in the wait list as defined by their risk factor and position in the wait list
        '''

        # Dictionary of triage libraries
        triageDict = {
            'A':{
                0 : ("Did the pain start during physical activity?",'Q'),
                    -2 : ("Does the chest pain radiate into your arms, jaw or back?","Q"),
                        -1 : (4,"A"),
                        -4 : ('Is your chest pain constant?',"Q"),
                            -3 : (5,"A"),
                            -6 : ('Have you ever had chest pain like this before?',"Q"),
                                -5 : (6,"A"),
                                -14 : ('Do you have a history of any cardiac conditions?',"Q"),
                                    -8 : ('Are you pale, diaphoretic, short of breath, or dizzy/lightheaded?',"Q"),
                                        -7 : (6,"A"),
                                        -10 : ('Is your chest pain worse when you move or take a deep breath?',"Q"),
                                            -9 : (7,"A"),
                                            -12 : ('Did the chest pain start less than 24 hours ago?',"Q"),
                                                -11 : (7,"A"),
                                                -13 : (9,"A"),
                                    -16 : ('Are you pale, diaphoretic, short of breath, or dizzy/lightheaded?',"Q"),
                                        -15 : (8,"A"),
                                        -18 : ('Is your chest pain worse when you move or take a deep breath?',"Q"),
                                            -17 : (8,"A"),
                                            -20 : ('Did the chest pain start less than 24 hours ago?',"Q"),
                                                -19 : (9,"A"),
                                                -21 : (10,"A"),
                    20 : ("Does the chest pain radiate into your arms, jaw or back?","Q"),
                        21 : (2,"A"),
                        18 : ('Is your chest pain constant?',"Q"),
                            19 : (5,"A"),
                            16 : ('Have you ever had chest pain like this before?',"Q"),
                                17 : (5,"A"),
                                8 : ('Do you have a history of any cardiac conditions?',"Q"),
                                    14 : ('Are you pale, diaphoretic, short of breath, or dizzy/lightheaded?',"Q"),
                                        15 : (5,"A"),
                                        12 : ('Is your chest pain worse when you move or take a deep breath?',"Q"),
                                            13 : (7,"A"),
                                            10 : ('Did the chest pain start less than 24 hours ago?',"Q"),
                                                11 : (8,"A"),
                                                9 : (10,"A"),
                                    6 : ('Are you pale, diaphoretic, short of breath, or dizzy/lightheaded?',"Q"),
                                        7 : (7,"A"),
                                        4 : ('Is your chest pain worse when you move or take a deep breath?',"Q"),
                                            5 : (9,"A"),
                                            2 : ('Did the chest pain start less than 24 hours ago?',"Q"),
                                                3 : (9,"A"),
                                                1 : (10,"A")
            },'B':{
                0 : ("Do you have a cough?",'Q'),
                    -14 : ("Are you bringing anything up?","Q"),
                        -15 : (1,"A"),
                        -12 : ("Do you have previous lung conditions?","Q"),
                            -13 : (6,"A"),
                            -10 : ('Do you smoke?',"Q"),
                                -11 : (4,'A'),
                                -8 : ('Do you have chest pains?','Q'),
                                    -9 : (9,'A'),
                                    -6 : ('Do you have a history of any cardiac conditions', 'Q'),
                                        -7 : (8,'A'),
                                        -2 : ('Are you able to do your normal physical activity?','Q'),
                                            -1 : (7,'A'),
                                            -4 : ('Are you able to speak full sentences?','Q'),
                                                -5 : (2,'A'),
                                                -3 : (5,'A'),
                    2 : ("Do you have previous lung conditions?","Q"),
                        1 : (6,"A"),
                        4 : ('Do you smoke?',"Q"),
                            3 : (4,'A'),
                            6 : ('Do you have chest pains?','Q'),
                                5 : (9,'A'),
                                8 : ('Do you have a history of any cardiac conditions', 'Q'),
                                    7 : (8,'A'),
                                    12 : ('Are you able to do your normal physical activity?','Q'),
                                        13 : (7,'A'),
                                        10 : ('Are you able to speak full sentences?','Q'),
                                            9 : (2,'A'),
                                            11 : (5,'A')
                
            },'C':{
                0 : ("Do you feel sick?",'Q'),
                    -14 : ("Are you vomiting?","Q"),
                        -6 : ('Is the pain in the upper or lower part of the abdomen?',"Q"),
                            -2 : ("Do you have a history of any abdominal conditions?","Q"),
                                -1 : (6,"A"),
                                -4 : ('Have you had any recent abdominal surgeries',"Q"),
                                    -3 : (9,"A"),
                                    -5 : (7,"A"),
                            -12 : ('Have your bowel movements been normal?','Q'),
                                -13 : (5,'A'),
                                -8 : ("Do you have a history of any abdominal conditions?","Q"),
                                    -7 : (6,"A"),
                                    -10 : ('Have you had any recent abdominal surgeries',"Q"),
                                        -11 : (7,"A"),
                                        -9 : (8,"A"),
                            -22 : ('Is your vomit green or yellow','Q'),
                                -16 : ('Have your menstrual periods been normal (If male enter: yes)',"Q"),
                                    -15 : (6,'A'),
                                        -18 : ("Do you have a history of any abdominal conditions?","Q"),
                                            -17 : (5,"A"),
                                            -20 : ('Have you had any recent abdominal surgeries',"Q"),
                                                -19 : (6,"A"),
                                                -21 : (7,"A"),
                                -28 : ('Is the pain in the upper or lower part of the abdomen?',"Q"),
                                    -24 : ("Do you have a history of any abdominal conditions?","Q"),
                                        -23 : (4,"A"),
                                        -26 : ('Have you had any recent abdominal surgeries',"Q"),
                                            -25 : (5,"A"),
                                            -27 : (6,"A"),
                                    -34 : ('Have your bowel movements been normal?','Q'),
                                        -35 : (4,'A'),
                                        -30 : ("Do you have a history of any abdominal conditions?","Q"),
                                            -29 : (5,"A"),
                                            -32 : ('Have you had any recent abdominal surgeries',"Q"),
                                                -31 : (6,"A"),
                                                -33 : (7,"A"),
                    4 : ("Do you have a history of any abdominal conditions?","Q"),
                        5 : (5,"A"),
                        2 : ('Have you had any recent abdominal surgeries',"Q"),
                            1 : (8,"A"),
                            3 : (7,"A")
        }}


        # Select specific triage library 
        initQuestion = None
        while initQuestion != 'A' and initQuestion != 'B' and initQuestion != 'C':
            initQuestion = str(input("Select from the following:\nA) Chest pains\nB) Shortness of breath\nC) Abdominal pain\nEnter A, B or C.")).upper()
        if initQuestion == 'A' or initQuestion == 'B' or initQuestion == 'C':
            
            # Create new tree using specified library
            selectedTree = triageDict[initQuestion]
            triage_tree = triageNode(0)
            for row in selectedTree:
                triage_tree.insert_node(row)

            # Search library till an end node is reached
            end_node_triage_tree = (triage_tree.search_triage_tree(selected_triage_tree = selectedTree))

            # Convert the range of possible risk factors into a series of number ranging from 0 to n (n = number of end nodes)
            # 0 = lowest risk, n = highest risk
            
            
            self.risk_factor = selectedTree[end_node_triage_tree][0]
            
            # Add patients into a wait list based on their calculated risk factor
            # If risk factors are equal, new patients are treated last
            tmp_patient = [self.name, self.risk_factor, None]

            # Rank each individual in the wait list based off of their risk factor
            for row in range(len(wait_times_list)):
                if tmp_patient not in wait_times_list:
                    if tmp_patient[1]  > wait_times_list[row][1]:
                        wait_times_list.insert(row, tmp_patient)
            if tmp_patient not in wait_times_list:
                wait_times_list.append(tmp_patient)

            # Recalculate wait times when a new patient is added 
            expected_wait_time = [0]
        #    expected_wait_time.append(0)
            for row in range(len(wait_times_list)):
                new_wait_time = 0
                new_wait_time = (wait_times_list[row][1]**1.05)+15
                for i in range(row):
                    new_wait_time += (wait_times_list[i][1]**1.05)+15
                expected_wait_time.append(new_wait_time)
                wait_times_list[row][2] = int(expected_wait_time[row])
        else: 
            print("Invalid input.\nProgram terminated.")

    def display_Wait_Times_List(self, wait_times_list = wait_times_list):

        '''
        display_Wait_Times_List(self, wait_times_list = wait_times_list):
        Prints a list of patients on the wait list

        Args: 
            wait_times_list: List of lists each representing a patient Default: wait_times_list

        Help on function display_Wait_Times_List in module __main__:

        Displays the following for each patient:
            Name
            Risk factor
            Estimated wait time
        '''        

        print("Emergency room waiting list:")         
        for row in range(len(wait_times_list)):
            print("\nName:", wait_times_list[row][0],"\nRisk factor:", wait_times_list[row][1],"\nEstimated wait time:", wait_times_list[row][2], 'minutes')

    # Determines the total cost of the of the procedures a patients will undergo
    # Returns a printed table of all of the procedures, a lyout of the various cost and total costs
    def patient_TotalCost(self, listProcedures, sumCost=0, sumProcedureCost=0, sumBaseCost=0, sumTotalCost=0):
        
        '''
        patient_TotalCost(self, listProcedures, sumCost=0, sumProcedureCost=0, sumBaseCost=0, sumTotalCost=0):

        Args:
            listProcedures: list of strings
            sumCost: int greater than zero Default: 0
            sumProcedureCost: int greater than zero Default: 0
            sumBaseCost: int greater than zero Default: 0
            sumTotalCos: int greater than zero Default: 0
        
        Return:
            An integer calculated from the inputs.

        Help on function patient_TotalCost in module __main__:

        for each procedure:
            If risk factor for procedure is less than 8
                Calculate the staffing cost
                Create list of all costs
                Add list to a dictionary 
                Add base cost to sum base cost
                Add staffing cost to sum staff cost
                Add total cost to sum total cost

            else: Add NA to all lists
        Create a list of the sum of all costs
        Print list to summarize the costs of each procedure and total cost for a patient
        '''
        
        summaryList = {}
        totalSummaryList = {}
        for row in listProcedures:
            # Output if a procedure is not denied
            if row.indProcedureRisk(self) < 8:
                staffCost = row.expectedTotalProcedureCost(self) - row.baseProcedureCost
                list_costs = (row.baseProcedureCost,staffCost,row.expectedTotalProcedureCost(self),row.indProcedureRisk(self),"")
                summaryList[row.procedure_name] = list_costs
                sumProcedureCost+=row.baseProcedureCost
                sumBaseCost += staffCost
                sumTotalCost+=row.expectedTotalProcedureCost(self)
            else: 
                # Output if a procedure is denied
                tmpListNA = ("NA","NA","NA",row.indProcedureRisk(self),"Denied, too high risk")
                summaryList[row.procedure_name] = tmpListNA

        totalSummaryList['Total cost:'] = (sumProcedureCost, sumBaseCost, sumTotalCost)

        # Print table of all the patient costs   
        print("\nPatient:",self.name)  
        print("Procedure:\tBase procedure cost:\tStaffing cost:\tExpected total cost:\tRisk factor\tComments")
        print("----------\t--------------------\t--------------\t--------------------\t-----------\t-----------")
        for key in summaryList:
            print(key,"\t",summaryList[key][0],"\t\t\t",summaryList[key][1],"\t\t",summaryList[key][2],'\t\t\t',summaryList[key][3],"\t\t",summaryList[key][4],sep='')
        print("----------\t--------------------\t--------------\t--------------------\t-----------\t-----------")
        for key in totalSummaryList:
            print(key,"\t",totalSummaryList[key][0],"\t\t\t",totalSummaryList[key][1],"\t\t",totalSummaryList[key][2],sep='')
class triageNode:

    def __init__(self, current_node):

        '''
        __init__(self, current_node):

        Args:
            current_node: int
            self.left: Returns left node Default: None
            self.right: Returns right node Default: None
        '''

        self.left = None
        self.right = None
        self.current_node = current_node
        
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right
      

    # Add method to create nodes
    def insert_node(self, current_node):

        '''
        insert_node(self, current_node):

        Args:
            current_node: int

        Help on function avglist in module __main__:

        if no node is present add current_node
            if current_node is less than current index & left is None: Create node
                Otherwise re-run insert_node()
            if current_node is greater than current index & right is None: Create node
                Otherwise re-run insert_node()    
        '''

        if self.current_node is not None:
            if current_node < self.current_node:
                if self.left is None:
                    self.left = triageNode(current_node)
                else:
                    self.left.insert_node(current_node)
            elif current_node > self.current_node:
                if self.right is None:
                    self.right = triageNode(current_node)
                else:
                    self.right.insert_node(current_node)
        else:
            self.current_node = current_node


    # primary method for search across the triage tree 
    # Return the risk factor for the patient
    def search_triage_tree(self, selected_triage_tree, current_node=0):

        '''
        search_triage_tree(self, selected_triage_tree, current_node=0):
        Returns the index of the current_node (int)

        Args: 
            selected_triage_tree: Binary tree of dictionaries. Each dictionary consists of an index and a list of either a question & an identifier 'Q' or a risk factor & an identifier 'A'
            current_node: int representing the root of a binary tree Default: 0

        Return:
            int  

        Help on function search_triage_tree in module __main__:

        if the identifier in the selected node of the selected_triage_tree == 'Q'
            Calls 'printQuestion' returning the patient's answer
            Calls the search function returning the child node based on the patient's answer
            Re-iterates if the identifier in the selected_triage_tree based on the index of the child note is not 'A'
        Returns current_node if the identifier in the selected_triage_tree based on the index of the child note is 'A'
        '''

        if selected_triage_tree[current_node][1] == 'Q':

          # Ask question to the patient
           # patients_answer = self.printQuestion(selected_triage_tree = selected_triage_tree, current_Question = current_node)
 
          # Look up next question
            child_node = self.search(current_node = current_node, patients_answer = self.printQuestion(selected_triage_tree = selected_triage_tree, current_Question = current_node))

           # Reiterate until a risk factor is determined 
            return self.search_triage_tree(selected_triage_tree, current_node = child_node)
        else: 
            return current_node

    # Prompts user with a question. Returns 'yes' or 'no'   
    def printQuestion(self, selected_triage_tree, current_Question=0):

        '''
        printQuestion(self, selected_triage_tree, current_Question=0):
        Returns patients answer ('yes' or 'no')

        Args: 
            selected_triage_tree: Binary tree of dictionaries. Each dictionary consists of an index and a list of either a question & an identifier 'Q' or a risk factor & an identifier 'A'
            current_Question: int representing the current question Default: 0

        Return:
            Boolean string ('yes' or 'no')

        Help on function printQuestion in module __main__:

        Asks a question to the patient
        If response is not 'yes' or 'no', it will re-ask the question
        Returns patients answer
        '''

        patient_Answer = str(input(selected_triage_tree[current_Question][0])).lower()
        if patient_Answer != 'yes' and patient_Answer != 'no':
            print("Invalid input.\nInput must be: \"yes\" or \"no\".")

            #Reiterate until a correct answer is inputed
            self.printQuestion(selected_triage_tree, current_Question)
        else:   
            return patient_Answer

    def search(self, current_node=0, patients_answer = "no"):

        '''
        search(self, current_node=0, patients_answer = "no"):
        Returns index of the child_node base on patients answer

        Args:
            current_node: int Default: 0
            patients_answer: boolean string ('yes' or 'no') Default: 'no'

        Return:
            int of index for the child node

        Help on function search in module __main__:

        Search left child node if current_node is less than current position in tree
        Search right child node if current_node is greater than current position in tree
        If patients answer is 'yes' get left child node
        If patients answer is 'no' get left child node
        '''

        if current_node < self.current_node:
            left_child_node = self.getLeftChild()
            return left_child_node.search(current_node,patients_answer)
        elif current_node > self.current_node:
            right_child_node = self.getRightChild()
            return right_child_node.search(current_node,patients_answer)
        else:
            if patients_answer == 'yes':
                child_node = self.getLeftChild()
            else:
                child_node = self.getRightChild()
            return child_node.current_node