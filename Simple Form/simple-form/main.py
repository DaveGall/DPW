'''
David Gall
04/15/2015
DPW
Simple Login Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        display=Page()
        self.response.write(display.web_page())

class Page(object):
    def __init__(self):
        self.css = "css/style.css"
        self.page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>My Simple Form</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.page_body = '''<form method="GET">
        <label>Name:</label><input type="text" name="user_name"/>
        <label>Address:</label><input type="text" name="address"/>
        <label>City:</label><input type="text" name="city"
        '''
        self.page_close = '''</form>
    </body>
</html>
        '''
    def web_page(self):
        all = self.page_head+self.page_body+self.page_close
        all = all.format(**locals())
        return all




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
