__author__ = 'davegall'

'''
Payroll class for my employee hours tracker.
'''

class Payroll(object):
    def __init__(self):
        self.employee_name = ""
        self.employee_hours = 0
        self.employee_dependants = 6
        self.hourly_pay = 0
        self.__taxes = 0
        self.__employee_check = 0

    def gross_pay(self):
        gp = self.employee_hours*self.hourly_pay
        return gp

    def taxes(self):
        #results = self.employee_dependants*.023
        #return results
        if self.employee_dependants <= 2:
            results = .23
            print results
        else:
            results = .20
            print results



    @property
    def employee_check(self):
        return self.__employee_check

    @employee_check.setter
    def employee_check(self, new_paycheck):
        self.__employee_check = new_paycheck

    def net_pay(self):
        self.__employee_check = self.taxes()*self.gross_pay()
        return self.__employee_check










