'''
David Gall
04/23/15
DPW
Reusable Library
'''
import webapp2
from page import Page
from lib import Payroll

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.head())

        money = Payroll()
        self.response.write(money.taxes())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
