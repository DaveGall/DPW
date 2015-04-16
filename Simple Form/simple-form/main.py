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
        p=Page()
        self.response.write(p.print_out())

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
        self.page_body = 'Just getting everything set up.'
        self.page_close = '''
    </body>
</html>
        '''
    def print_out(self):
        all = self.page_head+self.page_body+self.page_close
        all = all.format(**locals())
        return all




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
