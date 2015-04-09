'''
David Gall
04/08/15
DPW
Classes and HTML Video
'''
import webapp2
from pages import Page #From the page file import the Page class. Connects the two pages.

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Dave, you are awesome!!"
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
