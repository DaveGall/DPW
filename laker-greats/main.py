'''
David Gall
04/29/2015
DPW
Dynamic Website
Laker Greats
'''
import webapp2
from pages import MainPage, ResultsPage
from data import Lakers, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = ResultsPage()
        l = Lakers()
        d = Data()

        if self.request.GET:

            if l.number == '24':
                self.response.write("Dave this is Kobe")
            elif l.number == '32':
                self.response.write("Dave this is Magic")
            elif l.number == '33':
                self.response.write("Dave this is Kareem")
            else:
                self.response.write(p.print_out())


        #self.response.write(p.print_out())
        #self.response.write(d.loop())
        #print p.links


'''
        if self.request.GET:
            d = Data()
            d.number24 = self.request.GET['number=24']
            self.response.write(d.number24)
        else:
            self.response.write(p.print_out())
'''
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
