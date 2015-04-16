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
        self.page_body = '''<div id="form_container">
        <form method="GET">
        <label for="name">Name:</label><input id="name" type="text" name="user_name"/>
        <label for="address" >Address:</label><input id="address" type="text" name="address"/>
        <label for="city">City:</label><input id="city" type="text" name="city"/>
        <label class="state_label" for="state">State:</label>
        <select id="state" name="state" value="state">
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
        <p>Would you like to sign up for company discount emails?</p>
        <label for="yes" class="discount">Yes</label>
        <input type="radio" id="yes" name="coupon" value="yes"/>
        <label for="no" class="discount">No</label>
        <input type="radio" id="no" name="coupon" value="no"/>
        '''
        self.page_close = '''</form></div>
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
