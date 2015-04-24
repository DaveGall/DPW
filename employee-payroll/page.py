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
            <h2>Employee Payroll</h2>
            <hr>

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

                    <input type="submit" value="Submit" id="button"/>
                </form>

            </div>
        '''

        body = self.body
        return body
    def close(self):
        self.close = '''

        </div>
        '''
        close = self.close
        return close



class FinalBody(object):
    def __init__(self):
        pass
    def results_body(self):
        self.new_body = '''
            '''
        new_body = self.new_body
        return new_body
    def results_name(self):
        self.new_name = '''
                <p>Employee:
                '''
        new_name = self.new_name
        return new_name
    def results_hours(self):
        self.new_hours = '''
                </p><hr><p>Hours Worked:
                '''
        new_hours = self.new_hours
        return new_hours
    def results_users(self):
        self.rate = '''
                </p><hr><p>Pay Rate:
                '''
        rate = self.rate
        return rate
    def results_gross(self):
        self.new_gross = '''
                </p><hr><p>Gross Pay:
                '''
        new_gross = self.new_gross
        return new_gross
    def results_tax(self):
        self.tax_amount = '''
                </p><hr><p>Taxes Paid:
        '''
        tax_amount = self.tax_amount
        return tax_amount
    def results_net(self):
        self.new_net = '''
                </p><hr><p>Net Pay:
        '''
        new_net = self.new_net
        return new_net

    def results_close(self):
        self.new_close = '''
                </p></hr>
        '''
        new_close = self.new_close
        return new_close
        #new_body = self.new_body+self.new_name+self.new_hours+self.rate+self.new_gross+self.new_net
        #return new_body


