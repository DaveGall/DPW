'''
David Gall
04/13/15
DPW
Login Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''


        page_body = '''<form method="GET">
            <label>Name:</label> <input type="text" name="user"/>
            <label>Email:</label> <input type="text" name="email"/>
            <input type="submit" value="Submit"/>'''

        page_close = '''</form>
    </body>
</html>
        '''
        if self.request.GET:
            #storing the information from user.
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head+ user+' '+email+page_body+page_close)
        else:
            self.response.write(page_head+page_body+page_close)
        #print "Hello there."prints to console
        #self.response.write(page) prints the information out to the page.

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
