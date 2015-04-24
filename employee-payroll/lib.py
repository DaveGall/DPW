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
        self.taxes = float(g) * float(r)
        taxes = self.taxes
        return taxes

    def check_net(self, gross, taxes):
        self.net = float(gross) - float(taxes)
        net = self.net
        return net








class Payroll(object):#Stores Data
    def __init__(self):
        self.employee_name = ""
        self.employee_hours = 0
        self.employee_dependants = 0
        self.__hourly_pay = 0#Maybe change this to the hidden value.
        self.taxes = 0#undo as hidden value
        self.employee_check = 0#undo as hidden value


    @property
    def hourly_pay(self):
        return self.__hourly_pay

    @hourly_pay.setter
    def hourly_pay(self, hp):
        if hp < 0:
            print "Please put a valid wage in."
        else:
            self.hourly_pay = hp














