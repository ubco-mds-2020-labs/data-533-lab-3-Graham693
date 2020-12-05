# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import random  
from hospital.hospital_management.member import *
class Physician(Member):
  
    physicianList = list()
    Member.count=0
    
    def __init__(self, name, hourly_wage, years_emplyed, department):
        Member.__init__(self, name, hourly_wage, years_emplyed)
        self.department = department
        
        Member.count = Member.count+1
        doctor = (self.name, self.hourly_wage, self. years_emplyed,self.department)
        Physician.physicianList.append(doctor)
        
        
    def display(self):
        Member.display(self)
        print('Physican Department: {}'.format(self.department))
        
        
    def christmasBonus(self):
        Member.christmasBonus(self)
        
    def physicianCount(self):
        
        print("There are {} physicans currently working at this hospital".format(Member.count))
    
    
    
    def displayPhysicians(self):
        print("Current Physicians:")
        print("--------------------")
        for row in Physician.physicianList:
            print('Name: Dr.',row[0])
            print('Hourly salary:',row[1])
            print('Department:',row[3])
            print("--------------------")
            
            
            
            
    def yearlySalary(self, hours_per_week):
        
        ##before taxes
        yearly_sal=hours_per_week*52*self.hourly_wage
        
        ##after taxes
        
        if yearly_sal<=700000:
                tax_rate=0.05
                
        elif yearly_sal>700000 and yearly_sal<1000000:
            tax_rate=0.10
            
        else:
             tax_rate=0.20
        
        take_home_pay=yearly_sal-(yearly_sal*tax_rate)
        
        print('Yearly take home pay for Dr. {} is {} after taxes'.format(self.name,take_home_pay))
        
    
    def vactionTimePriority(self):
        ##done by a lottery system
        priority_nums = list(range(len(Physician.physicianList)))
        random.shuffle(priority_nums)   
        
        
        priority_list=[]
        for i in Physician.physicianList:
            priority_list.append(i[0])       
        
        
        
        priority_dict = {} 
        
        for name in priority_list: 
            for num in priority_nums: 
                priority_dict[name] = num 
                priority_nums.remove(num) 
                break  
        
        requested_weeks=[]
        print('Physician vacation time will be granted in this order:')
        for v in sorted( priority_dict.values() ):
            for key in priority_dict:
                if priority_dict[ key ] == v:
                    print(key,v)
                    break
                    
                    
    def oncallschedule(self):
        remaining_days=[]
        ##done by a lottery system
        days_open=['Sunday','Monday',"Tuesday","Wednesday","Thursday","Friday","Saturday"]
        
        random.shuffle(days_open)   
        doctor_list=[]
        for i in Physician.physicianList:
            doctor_list.append(i[0:5])       
        
        priority_dict = {} 
       
        if len(doctor_list) ==7:
            random.shuffle(doctor_list)
            priority_dict=dict(zip(days_open,doctor_list))
           
                           
        elif len(doctor_list) < len(days_open):
            random.shuffle(doctor_list)
            assigned_days=days_open[:len(doctor_list)+1]
            
            priority_dict=dict(zip(assigned_days,doctor_list))
           
            remaining_days=[]
            for x in days_open:
                if x not in priority_dict:
                                
                    remaining_days.append(x)
                    
                    for day in remaining_days:
                        
                        priority_dict[day]=random.choice(doctor_list)
                    
        else:
            random.shuffle(doctor_list)
            assigned_people=doctor_list[:len(days_open)+1]
            not_on_call=doctor_list[len(days_open):]
            priority_dict=dict(zip(days_open,assigned_people))
            
            for person in not_on_call:
                print("Doctor", person,"is not on call this week")
        
        
        for i in priority_dict:
            print(i,"on call doctor:",priority_dict[i])
            
                        
