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

            if self.request.GET('24'):
                self.response.write("Dave this is Kobe")
            elif self.request.GET('32'):
                self.response.write("Dave this is Magic")
            else:
                self.response.write(p.print_out())
        #p.links = d.loop()
        #self.response.write(d.players)
        #if l.number == 24:
         #   self.request.GET(d.players[1])
          #  self.response.write(l.name+str(l.number)+str(l.game_average)+str(l.career_points)+l.position)
        #else:
         #   self.response.write(p.print_out())



        #self.response.write(d.players[1])
        #p.body = d.loop()
        self.response.write(p.print_out())
        self.response.write(d.loop())
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
