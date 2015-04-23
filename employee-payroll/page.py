#__author__ = 'davegall'


#Page class for my employee hours tracker.


class Page(object):
    def __init__(self):
        pass
    def head(self):
        self.css = "css/style.css"
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Employee Payroll</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <h2>Your Payroll</h2>
        '''

        header = self.head
        header = header.format(**locals())
        return header



    def body(self):
        self.body = '''

        '''


    def close(self):
        self.close = '''

        '''


