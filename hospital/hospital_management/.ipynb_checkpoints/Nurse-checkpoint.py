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
class Nurse(Member):
    nurseList = []
    def __init__(self, name, hourly_wage, years_emplyed, monthly_Hours):
        Member.__init__(self, name, hourly_wage, years_emplyed)
        
        self.monthly_Hours=monthly_Hours
       
         
        nurse = (self.name, self.hourly_wage, self.monthly_Hours)
        Nurse.nurseList.append(nurse)
       
              
              
    def display(self):
        Member.display(self)
        print('Hours Worked in a month:{} '.format(self.monthly_Hours))
        
    def christmasBonus(self):
        Member.christmasBonus(self)
    
    def AverageDailyHours(self, month):
        
        month1=month.lower()
        
        if (month1=='january' or 'march' or 'may' or 'july' or 'august' or 'october' or 'december'):
            av_d_hours31 = self.monthly_Hours/31
            
            print('{} averages {} daily hours of work'.format(self.name,av_d_hours31))
        elif (month=='april'or 'june' or 'september' or 'november'):
            
            av_d_hours30=self.monthly_Hours/30
            print('{} averages {} daily hours of work'.format(self.name,av_d_hours30))
        else:
            av_d_hours28=self.monthly_Hours/28
            print('{} averages {} daily hours of work'.format(self.name,av_d_hours28))
        
        
    def over_time_pay_monthly(self, overtime_hours):
        
        if self.monthly_Hours>100:
        
            monthly_pay=self.monthly_Hours*self.hourly_wage+overtime_hours*(self.hourly_wage*1.5)
        
        
            print('{} worked {} overtime hours and take home monthly pay with overtime pay is {}'.format(self.name,overtime_hours, monthly_pay ))
        
        else:
            print('{} does not qualify for overtime pay'.format(self.name))
    
    
    def nurseSheduling(self, num_open_floors):
        floornum = num_open_floors
        
        nursenum = len(Nurse.nurseList)
        
        nurses_available = [i for i in range(nursenum)]

        for i in range(nursenum):
            group = i % floornum
            nurse = random.choice(nurses_available)
            nurses_available.remove(nurse)
            print('Nurse {} assigned to floor {}'.format(nurse, group))
            
        for nurse in range(len(Nurse.nurseList)):
            
            
            print('Nurse {} is {}'.format(nurse,Nurse.nurseList[nurse][0]))
            

            
