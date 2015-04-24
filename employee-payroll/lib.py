#__author__ = 'davegall'


#Payroll class for my employee hours tracker.

class EmployeeCheck(object):
    def __init__(self):
        pass

    def deductions(self, d):
        if d < 4:
            rate = .23
            return rate
        else:
            rate = .28
            return rate

    def check_gross(self, hours, pay):
        self.gross = float(hours) * float(pay)
        gross = self.gross
        return gross

    def employee_taxes(self, g, r):
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














