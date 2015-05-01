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



        if l.number == '24':
            k = self.response.write("Dave this is Kobe Bryant")
            return k
        elif l.number == '32':
            self.response.write("Dave this is Magic")
        elif l.number == '33':
            self.response.write("Dave this is Kareem")
        elif l.number == '22':
            self.response.write("Dave this is Elgin Baylor")
        elif l.number == '13':
            self.response.write("Dave this is Wilt Chamberlain")
        elif l.number == '34':
            self.response.write("Dave this is Shaquille O'Neal")
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
