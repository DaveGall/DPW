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
        <label>State</label>
        <select name="state">
            <option>Alabama</option>
            <option>Alaska</option>
            <option>Arizona</option>
            <option>Arkansas</option>
            <option>California</option>
            <option>Colorado</option>
            <option>Connecticut</option>
            <option>Delaware</option>
            <option>Florida</option>
            <option>Georgia</option>
            <option>Hawaii</option>
            <option>Idaho</option>
            <option>Illinois</option>
            <option>Indiana</option>
            <option>Iowa</option>
            <option>Kansas</option>
            <option>Kentucky</option>
            <option>Louisiana</option>
            <option>Maine</option>
            <option>Maryland</option>
            <option>Massachusetts</option>
            <option>Michigan</option>
            <option>Minnesota</option>
            <option>Mississippi</option>
            <option>Missouri</option>
            <option>Montana</option>
            <option>Nebraska</option>
            <option>Nevada</option>
            <option>New Hampshire</option>
            <option>New Jersey</option>
            <option>New Mexico</option>
            <option>New York</option>
            <option>North Carolina</option>
            <option>North Dakota</option>
            <option>Ohio</option>
            <option>Oklahoma</option>
            <option>Oregon</option>
            <option>Pennsylvania</option>
            <option>Rhode Island</option>
            <option>South Carolina</option>
            <option>South Dakota</option>
            <option>Tennessee</option>
            <option>Texas</option>
            <option>Utah</option>
            <option>Vermont</option>
            <option>Virginia</option>
            <option>Washington</option>
            <option>West Virginia</option>
            <option>Wisconsin</option>
            <option>Wyoming</option>
        </select>
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
