#__author__ = 'davegall'

class MainPage(object):
    def __init__(self):
        self.css = 'css/style.css'
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Laker Greats</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.body = 'The Lakers are Great'
        self.close = '''
    </body
</html>
        '''

    def print_out(self):
        page = self.head+self.body+self.close
        page = page.format(**locals())
        return page

