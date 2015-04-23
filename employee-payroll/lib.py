__author__ = 'davegall'

'''
Payroll class for my employee hours tracker.
'''

class Payroll(object):
    def __init__(self):
        self.employee_name = ""
        self.employee_hours = 0
        self.employee_dependants = 0
        self.hourly_pay = 0
        self.__employee_check = 0
