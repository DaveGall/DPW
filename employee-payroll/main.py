'''
David Gall
04/23/15
DPW
Reusable Library
'''
import webapp2
from page import Page
from page import FinalBody
from lib import Payroll, EmployeeCheck

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        fb = FinalBody()
        money = Payroll()
        pay = EmployeeCheck()
        deductions = pay.deductions(5)
        #gross = pay.check_gross(80,10)
        #tax = pay.employee_taxes(800, deductions)
        #net = pay.check_net(gross, tax)
        print deductions



        if self.request.GET:
            new = EmployeeCheck()
            name = self.request.GET["employee_name"]
            hours = self.request.GET["employee_hours"]
            dependants = self.request.GET["employee_dependants"]
            pay = self.request.GET["hourly_pay"]
            gross = new.check_gross(hours, pay)
            deductions = new.deductions(dependants)
            tax = new.employee_taxes(gross, deductions)
            self.response.write(p.head()+fb.results_body()+fb.results_name()+name+" "+fb.results_hours()+hours+" "+fb.results_users()+" $"+pay+" per hour"+fb.results_gross()+" $"+str(gross)+fb.results_net()+" "+str(gross)+" "+str(tax)+p.close())
        else:
            self.response.write(p.head()+p.body()+p.close())





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
