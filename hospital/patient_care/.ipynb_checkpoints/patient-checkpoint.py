cclass Patient:
    count = 0
    patientsList = []
    wait_times_list = []

    def __init__(self, name, age, service = None, listPreExistCond = None, risk_factor = None):
        self.name = name
        self.age = age
        self.service = service
        self.listPreExistCond = listPreExistCond
        self.risk_factor = risk_factor

        Patient.count +=1
        patient_variables = (self.name, self.age, self.service, self.listPreExistCond)
        Patient.patientsList.append(patient_variables)

    # Display patient 
    def display_Patient(self):
            print('Patient name:', self.name,'\nAge:',self.age,'\nService:',self.service,'\nPre-existing conditions:',self.listPreExistCond,'\nRisk factor:',self.risk_factor,'\n')

    # Print the number of patients  
    def patient_Count(self):
        print("Current patient count:",Patient.count)

    #Display the list of all the patients
    def diplay_PatientsList(self):
        print("List of patients:")
        print("--------------------")
        for row in Patient.patientsList:
            print('Name:',row[0])
            print('Age:',row[1])
            print('Service:',row[2])
            print('Pre-existing Conditions:',row[3])
            print("Risk factor:", wait_times_list[row][1])
            print("--------------------") 

    # Prompt the issues with questions about the patients condition. 
    # Returns a risk factor and an estimated wait time for the patient.
    def triage_Patient(self, wait_times_list=wait_times_list):
        #tmpListTriage = (self.name)

        # Dictionary of triage libraries
        triageDict = {
            'A':{
                0 : ("Has your bruse grown over the past day?",'Q'),
                -2 : ("Do you feel faint or get tired easily since you got that bruse?","Q"),
                -1 : (7,"A"),
                -3 : (10,"A"),
                2 : ("Does your bruise hurt a lot?","Q"),
                1 : (3,"A"),
                3 : (0,"A")
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
                -3 : (5,'A')
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
                0 : ("Do you feel sink?",'Q'),
                -2 : ("Do you feel faint or get tired easily since you got that bruse?","Q"),
                -1 : (7,"A"),
                -3 : (10,"A"),
                2 : ("Does your bruise hurt a lot?","Q"),
                1 : (3,"A"),
                3 : (0,"A")
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
                triage_tree.insert(row)

            # Search library till an end node is reached
            end_node_triage_tree = (triage_tree.search_triage_tree(selected_triage_tree = selectedTree))

            # Convert the range of possible risk factors into a series of number ranging from 0 to n (n = number of end nodes)
            # 0 = lowest risk, n = highest risk
            
            
            self.risk_factor = selectedTree[end_node_triage_tree][0]
            
            # Add patients into a wait list based on their calculated risk factor
            # If risk factors are equal, new patients are treated last
            tmp_patient = [self.name, self.risk_factor, None]
           # if len(wait_times_list) == 0:
         #       wait_times_list.append(tmp_patient)
            #else:
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
                    new_wait_time += expected_wait_time[i+1]
                expected_wait_time.append(new_wait_time)
                wait_times_list[row][2] = int(expected_wait_time[row])
        else: 
            print("Invalid input.\nProgram terminated.")

    def display_Wait_Times_List(self, wait_times_list = wait_times_list):  
            print("Emergency room waiting list:")         
            for row in range(len(wait_times_list)):
                print("\nName:", wait_times_list[row][0],"\nRisk factor:", wait_times_list[row][1],"\nPredicted wait time:", wait_times_list[row][2], 'minutes')

    # Determines the total cost of the of the procedures a patients will undergo
    # Returns a printed table of all of the procedures, a lyout of the various cost and total costs
    def patient_TotalCost(self, listProcedures, sumCost=0, sumProcedureCost=0, sumBaseCost=0, sumTotalCost=0):
        summaryList = {}
        totalSummaryList = {}
        for row in listProcedures:
            # Output if a procedure is not denied
            if row.indProcedureRisk(self) < 7:
                staffCost = row.expectedTotalProcedureCost(self) - row.baseProcedureCost
                list_costs = (row.baseProcedureCost,staffCost,row.expectedTotalProcedureCost(self),row.indProcedureRisk(self),"")
                summaryList[row.procedure_name] = list_costs
                sumProcedureCost+=row.baseProcedureCost
                sumBaseCost += tmpStaffCost
                sumTotalCost+=row.expectedTotalProcedureCost(self)
            else: 
                # Output if a procedure is denied
                tmpListNA = ("NA","NA","NA",row.indProcedureRisk(self),"Denied, too high risk")
                summaryList[row.procedure_name] = tmpListNA

        totalSummaryList['Total cost:'] = (sumProcedureCost, sumBaseCost, sumTotalCost)

        # Print table of all the patient costs   
        print("Procedure:\tBase procedure cost:\tStaffing cost:\tExpected total cost:\tRisk factor\tComments")
        print("----------\t--------------------\t--------------\t--------------------\t-----------\t-----------")
        for key in summaryList:
            print(key,"\t",summaryList[key][0],"\t\t\t",summaryList[key][1],"\t\t",summaryList[key][2],'\t\t\t',summaryList[key][3],"\t\t",summaryList[key][4],sep='')
        print("----------\t--------------------\t--------------\t--------------------\t-----------\t-----------")
        for key in totalSummaryList:
            print(key,"\t",totalSummaryList[key][0],"\t\t\t",totalSummaryList[key][1],"\t\t",totalSummaryList[key][2],sep='')

class triageNode:

    def __init__(self, current_node):
        self.left = None
        self.right = None
        self.current_node = current_node
        
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right
      

# Insert method to create nodes
    def insert(self, current_node):

        if self.current_node is not None:
            if current_node < self.current_node:
                if self.left is None:
                    self.left = triageNode(current_node)
                else:
                    self.left.insert(current_node)
            elif current_node > self.current_node:
                if self.right is None:
                    self.right = triageNode(current_node)
                else:
                    self.right.insert(current_node)
        else:
            self.current_node = current_node


    # primary method for search across the triage tree 
    # Return the risk factor for the patient
    def search_triage_tree(self, selected_triage_tree, current_node=0):

        if selected_triage_tree[current_node][1] == 'Q':

          # Ask question to the patient
            patients_answer = self.printQuestion(selected_triage_tree = selected_triage_tree, current_Question = current_node)
 
          # Look up next question
            child_node = self.search(current_node = current_node, patients_answer2 = patients_answer)

           # Reiterate until a risk factor is determined 
            return self.search_triage_tree(selected_triage_tree, current_node = child_node)
        else: 
            return current_node

    # Prompts user with a question. Returns 'yes' or 'no'   
    def printQuestion(self, selected_triage_tree, current_Question=0):
        patient_Answer = str(input(selected_triage_tree[current_Question][0])).lower()
        if patient_Answer != 'yes' and patient_Answer != 'no':
            print("Invalid input.\nInput must be: \"yes\" or \"no\".")

            #Reiterate until a correct answer is inputed
            self.printQuestion(self, selected_triage_tree, current_Question)
        else:   
            return patient_Answer

    def search(self, current_node=0, patients_answer2 = "no"):
        if current_node < self.current_node:
            left_child_node = self.getLeftChild()
            return left_child_node.search(current_node,patients_answer2)
        elif current_node > self.current_node:
            right_child_node = self.getRightChild()
            return right_child_node.search(current_node,patients_answer2)
        else:
            if patients_answer2 == 'yes':
                child_node = self.getLeftChild()
            else:
                child_node = self.getRightChild()
            return child_node.current_node
