#__author__ = 'davegall'


#Payroll class for my employee hours tracker.

class EmployeeCheck(object):#This begins my functions class that will handle all calculations and can be used for any instance.
    def __init__(self):
        pass

    def deductions(self, d):# this decides which tax rate to use.
        if int(d) < 4:#if you have less than 4 dependants then your total tax rate will be .23 which equates to 23%
            rate = .23
            return rate#This returns the decimal to be multiplied by the employees gross pay.
        else:           #if your dependants are over 4 you will be charged at .28 which equates to 28%
            rate = .28
            return rate#This returns the decimal to be multiplied by the gross of the employees pay.

    def check_gross(self, hours, pay):# This function will give us the result of the users gross pay.
        self.gross = float(hours) * float(pay)#This multiples the two arguments and puts them into a variable called self.gross
        gross = self.gross#This takes self.gross and puts it into an easier to return variable.
        return gross#This returns the results of the equation.

    def employee_taxes(self, g, r):#This function gives us how much the employee paid in total taxes.
        self.taxes = float(g) * float(r)#This will multiply the two arguments which equates to the users gross pay and the tax rate.
        taxes = self.taxes
        return taxes#This returns the result of the equation above to be used in the code.

    def check_net(self, gross, taxes):#This code will give the user their net pay.
        self.net = float(gross) - float(taxes)#This subtracts the users gross pay by how much they paid in taxes to get their gross pay.
        net = self.net
        return net#This returns the users net pay to be displayed on the page.








class Payroll(object):#Sets up and stores the data from the user
    def __init__(self):
        self.employee_name = "" #stores the employee name
        self.employee_hours = 0 #stores the employee hours
        self.employee_dependants = 0#stores the users dependants
        self.__hourly_pay = 0#Restricted value


    @property#decorator that is needed to set up the setter for __hourly_pay
    def hourly_pay(self):
        return self.__hourly_pay #Returns __hourly_pay

    @hourly_pay.setter#setter for __hourly_pay
    def hourly_pay(self, hp):#This will validate whether the user puts in a number greater than 0
        if hp < 0:
            print "Please put a valid wage in."#This will display in the console if the user puts in a value less than 0
        else:
            self.hourly_pay = hp#It will allow the input if the value is 0 or above.














