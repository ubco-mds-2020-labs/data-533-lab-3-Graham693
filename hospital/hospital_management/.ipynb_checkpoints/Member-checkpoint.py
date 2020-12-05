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

class Member:
    
    def __init__(self, name, hourly_wage, years_emplyed):
    
    
        self.name=name
        self.hourly_wage = hourly_wage
        self.years_emplyed=years_emplyed
        print('(Hospital Member: {})'.format(self.name))

    
    def display(self):
        
        print('Name: {}, Hourly wage: {}'.format(self.name,self.hourly_wage))
        
        
        
    def christmasBonus(self):
        if self.years_emplyed<5:
            c_bonus=500
            print('{}s Christmas bonus is {} $'.format(self.name, c_bonus ))
        
        elif (self.years_emplyed>5 and self.years_emplyed<10):
            c_bonus=1000
            print('{}s Christmas bonus is {} $'.format(self.name, c_bonus ))
                
        else: 
        
            c_bonus=2000
            print('{}s Christmas bonus is {} $'.format(self.name, c_bonus ))
