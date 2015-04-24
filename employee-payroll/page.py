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
                    <label for="hours">Hours Worked:</label>
                    <input id="hours" type="text" name="employee_hours" placeholder="80"/>
                    <label for="dependants">Number of Dependants</label>
                    <input id="dependants type="text"
 name="employee_dependants" placeholder="2"/>
                    <label for="wage">Hourly Wage</label>
                    <input id="wage" type="text" name="hourly_pay" placeholder="9.25"/>

                    <input type="submit" value="Add" id="button"/>
                </form>

            </div>
        '''

        body = self.body
        return body
    def close(self):
        self.close = '''
            <footer>
                <ul>
                    <li></li>
                    <li></li>
                </ul>
            </footer>
        </div>
        '''
        close = self.close
        return close



class FinalResults(object):
    def __init__(self):
        pass
    def results_body(self):
        self.new_body = '''
            <div class="container">

            </div>
        '''


