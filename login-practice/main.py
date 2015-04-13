'''
David Gall
04/13/15
DPW
Login Form
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET">
            <label>Name:</label> <input type="text" name="user"/>
            <label>Email:</label> <input type="text" name="email"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
</html>
        '''
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
