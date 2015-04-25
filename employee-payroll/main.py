'''
David Gall
04/23/15
DPW
Reusable Library
'''
import webapp2#Don't touch we need it to use python.
from page import Page#imports Page from pages so that I can access the needed classes and code.
from page import FinalBody #Accesses the final body so that I can display the results
from lib import Payroll, EmployeeCheck#Brings in the EmployeeCheck class so that I can have access to the functional equations.

class MainHandler(webapp2.RequestHandler):#MainHandler
    def get(self):
        p = Page()#Brings up the Page class
        fb = FinalBody()#Final bod for my results page.
        money = Payroll()#Brings out the Payrol tax



        if self.request.GET:#Begins the if staement to decide which page to display.
            new = EmployeeCheck()#This brings in the class EmployeeCheck()
            name = self.request.GET["employee_name"]#This grabs the user input data for the input tag.
            hours = self.request.GET["employee_hours"]#Gets the hours the employee worked in that week.
            dependants = self.request.GET["employee_dependants"]#gets the dependants from the user and uses that info to help with some calculations.
            pay = self.request.GET["hourly_pay"]#Grabs the hourly pay that the user input into the system.
            gross = new.check_gross(hours, pay)#Calculates the gross pay using the functions from my library page.
            deductions = new.deductions(dependants)#Just grabs the amount of dependants input by the user
            tax = new.employee_taxes(gross, deductions)#total for the employees taxes that they paid. It uses a function and can be reused.
            net = new.check_net(gross, tax)#This uses the user input data to figure out the total net paycheck of the user.
            self.response.write(p.head()+fb.results_body()+fb.results_name()+name+" "+fb.results_hours()+hours+" "+fb.results_users()+" $"+pay+" per hour"+fb.results_gross()+" $"+str(gross)+fb.results_tax()+" $"+str(tax)+fb.results_net()+" $"+str(net)+fb.results_close()+p.close())#This is my string that will display the results as I want on the results page. Uses some of the Page, some of the results page to display the information.
        else:
            self.response.write(p.head()+p.body()+p.close())#This displays if you dont have anything in your input boxes.





app = webapp2.WSGIApplication([#Don't touch this either
    ('/', MainHandler)
], debug=True)
