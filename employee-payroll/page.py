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
        <div class="container">
            <h2>Your Payroll Entry</h2>


        '''

        header = self.head
        header = header.format(**locals())
        return header



    def body(self):
        self.body = '''
            <div class="myForm">
                <form method="GET">
                    <label for="name">Employee Name:</label>
                    <input id="name" type="text" name="employee_name" placeholder="Jim"/>

                </form>

            </div>
        '''

        body = self.body
        return body
    def close(self):
        self.close = '''
        </div>
        '''

