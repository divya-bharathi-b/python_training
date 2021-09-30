class employee:
  def __init__(self, empid, ename, edept, esal):
      self.empid = empid
      self.ename = ename
      self.edept = edept
      self.esal = esal

  def display(self):
      print("The employee details are : ")
      print("Emp ID : %d"%self.empid)
      print("Emp name : %s" % self.ename)
      print("Emp department : %s" % self.edept)
      print("Emp salary : %d" % self.esal)

class timesheet(employee):
    def __init__(self, date_of_entry, activity, description, hours_spent, status):
        self.date_of_entry = date_of_entry
        self.activity = activity
        self.description = description
        self.hours_spent = hours_spent
        self.status = status

    def createTimesheet(self):
        date_of_entry = input("Enter the date in DD/MM/YYYY format")
        activity = input("Enter the activity")
        description = input("Enter the description")
        hours_spent = int(input("Enter the number of hours spent to complete"))
        status = int(input("Enter the status"))

    def display(self):
        #employee.display()
        print("Date of entry : %s" % self.date_of_entry)
        print("Acticity : %s"%self.activity)
        print("DEscription given : %s"%self.description)
        print("Hours spent to perform the task : %d"%self.hours_spent)
        print("Status of the task : %s"%self.status)

e1=employee(2345, 'divya', 'DO', 26000)
e1.display()
try:
    date_of_entry = input("Enter the date in DD/MM/YYYY format")
    activity = input("Enter the activity")
    description = input("Enter the description")
    hours_spent = int(input("Enter the number of hours spent to complete"))
    if(hours_spent > 8):
        raise (Exception)
    else:
        status='Accepted'

except Exception:
    status = 'On hold'
    print('Status : %s'%status)
    print("Working hours should not be exceed than 8 hours")
else:
    print("Do you want to view your timesheet Type Y/N ")
    input1=input()
    if(input1 == 'Y' or input1 == 'y'):
        e1 = timesheet(date_of_entry,activity, description,hours_spent, status)
        e1.display()
    else:
        exit()



