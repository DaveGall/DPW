'''
David Gall
04/29/2015
DPW
Dynamic Website
Laker Greats
'''
import webapp2
from pages import MainPage
from data import Lakers, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = MainPage()
        d = Data()
        print d.players[1].name+str(d.players[1].number)
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
