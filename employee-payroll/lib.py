#__author__ = 'davegall'


#Payroll class for my employee hours tracker.


class Payroll(object):
    def __init__(self):
        self.employee_name = ""
        self.employee_hours = 0
        self.employee_dependants = 0
        self.hourly_pay = 0
        self.__taxes = 0
        self.__employee_check = 0




    def taxes(self):

        if self.employee_dependants < 4:

            rate = .23
            results = (self.employee_hours*self.hourly_pay)*rate
            print results
        else:
            rate = .20
            results = (self.employee_hours*self.hourly_pay)*rate
            print results

            return results






    @property
    def employee_check(self):
        return self.__employee_check

    #@employee_check.setter
    #def employee_check(self, new_paycheck):
     #   self.__employee_check = new_paycheck
    @employee_check.setter
    def employee_check(self, new_check):
        self.__employee_check = self.hourly_pay*self.employee_hours
        self.__employee_check = new_check












