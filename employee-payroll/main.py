'''
David Gall
04/23/15
DPW
Reusable Library
'''
import webapp2
from page import Page
from page import FinalBody
from lib import Payroll

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        fb = FinalBody()
        money = Payroll()


        if self.request.GET:
            name = self.request.GET["employee_name"]
            hours = self.request.GET["employee_hours"]
            dependants = self.request.GET["employee_dependants"]
            pay = self.request.GET["hourly_pay"]
            hp = self.request.GET["hourly_pay"]
            eh = self.request.GET["employee_hours"]
            total = float(hp)*float(eh)
            self.response.write(p.head()+fb.results_body()+fb.results_name()+name+" "+fb.results_hours()+hours+" "+fb.results_users()+" $"+pay+" per hour"+fb.results_gross()+" $"+str(total)+fb.results_net()+p.close())
        else:
            self.response.write(p.head()+p.body()+p.close())





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
