Subpackage 1: 

Module 1: ‘Member’ (Parent)

__init__(self, name, hourly_wage, years_emplyed):
Initializes each member of the hospital. Provides each member the attributes: name, hourly_wage, years_emplyed. Prints out the name of the new member when initialized.
Args:
	self
	name: string
	hourly_wage: int or float
	years_emplyed: int or float

display(self):
Args: self
Prints out the name and hourly_wage of a member.
Returns: A printed string with member.name and member.hourly_wage

christmasBonus(self):
Args: self
Calculates and returns the Christmas bonus for a member.
Returns: A printed string with member.name and the amount of the bonus.


Module 2: Physician (Child)

__init__
Initializes the physician object. Inherits the attributes of the Member’s class.
Increases the Member’s count and appends the attributes of the physician to the Physician list
Args:
	self
	name: string
	hourly_wage: int or float
	years_emplyed: int or float
	department: string

Display(self)
Displays the attributes of a physician using the display method of the Member class. The department of the physician is also displayed.
Args: self
Returns: a string with the physician’s name, hourly_wage and department

christmasBonus(self)
Displays the Christmas bonus of the 
Args: self
Returns: Prints string with the employee’s name and Christmas bonus

physicianCount(self)
Display’s the number of physicians in the hospital directory
Args: self
Returns: String with number of physicians (int)

displayPhysicians(self)
Prints physicians name, hourly_wage and department
Args: self
Returns: printed list with the physicians attributes

yearlySalary(self)
Calculates the yearly salary of a physicians after taxes
Args: 
Self
Hours_per_week (int/float)
Returns: Physician name and salary (int/float)

vacationTimePriority(self)
Calculates the order of priority for physicians to take vacation time (Based on a lottery-based system)
Args: self
Returns: prints names of the physicians and their priority number

Oncallschedule(self)
Formulates an ‘on call’ schedules for the week by randomly assigning the physicians working at the hospital to specific days. If there are day still open (# physicians < 7), physicians will be randomly assigned multiple shifts. If there are physicians that haven’t assigned a shift (# physicians > 7) it will print out the physicians with a shift and the physicians that do not have a shift.
Args: self
Returns: printed list of the day of the week and the on-call physicians for each day.

Module 3: Nurse (Child)
__init__
Initializes the nurse object. Inherits the attributes of the Member’s class.
Increases the Member’s count and appends the attributes of the nurse to the nurses list
Args:
	self
	name: string
	hourly_wage: int or float
	years_emplyed: int or float
monthly_Hours: int or float

Display(self)
Displays the attributes of a nurse using the display method of the Member class. The monthly_Hours of the nurse are also displayed.
Args: self
Returns: a string with the nurse’s name, hourly_wage and monthly_Hours worked.

christmasBonus(self)
Displays the Christmas bonus of the 
Args: self
Returns: Prints string with the employee’s name and Christmas bonus

AverageDailyHours(self)
Calculates the average daily hours worked per month by a nurse, depending upon the length of the month
Args: 
self
month: string

Returns:  prints the nurse’s name and the average daily hours worked for the month


over_time_pay_monthly(self)
Determines if a nurse is eligible for monthly overtime pay. Calculates take home monthly pay including overtime.
Args: 
	self
	overtime_hours: int/float
Returns:
If nurse is eligible for overtime pay. Pprints the nurses name and calculated take home monthly pay
If they are not eligible for overtime. Prints the nurses name and the statement ‘does not qualify for overtime pay.’

nurseSheduling(self)
Evenly & randomly distributes the nurses to a floor
Args:
	self
	num_open_floors: int
Returns: prints the nurse number and their assigned floor for each nurse and a list of all the nurses and their nurse number.
