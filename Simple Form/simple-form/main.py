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
        self.response.write(p.page_head+p.page_body+p.page_close)

class Page(object):
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>My Simple Form</title>
    </head>
    <body>
        '''
        page_body = 'Just getting everything set up.'
        page_close = '''
    </body>
</html>
        '''



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
