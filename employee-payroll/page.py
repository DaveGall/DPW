#__author__ = 'davegall'


#Page class for my employee hours tracker.


class Page(object):#This creates my Page class which houses all my html and my css
    def __init__(self):
        pass        #I passed this because it didn't seem to work right with it.
    def head(self):
        self.css = "css/style.css"#This imports the css into my html page. The self.head creates the header for my html and gives my page a title.
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

        header = self.head #This puts the self.head into a variable that can be returned.
        header = header.format(**locals())
        return header#This is the returned header to be used in my code.



    def body(self):#This begins my body code and houses my form and the GET method.
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

        body = self.body #This will put my body into a variable that will be returned and used in my html.
        return body#This is the return statement that will display when called in the mainhandler.
    def close(self):#This begins my page close which will close out my html page.
        self.close = '''

        </div>
        '''
        close = self.close#This is the variable that self.close gets put into
        return close#This returns the code to be used in the final html.



class FinalBody(object):#This class wil help display the results from the user input into a nice formatted display.
    def __init__(self):
        pass
    def results_body(self):#This starts the body of the results page.
        self.new_body = '''
            '''
        new_body = self.new_body
        return new_body #Again these are the returned values that will display when called in the mainhandler
    def results_name(self):#This section will display with the users name.
        self.new_name = '''
                <p>Employee:
                '''
        new_name = self.new_name
        return new_name#This is what helps display this section in the proper place.
    def results_hours(self):#This will help display the hours that the user worked during the time in question.
        self.new_hours = '''
                </p><hr><p>Hours Worked:
                '''
        new_hours = self.new_hours
        return new_hours#returns the value that will be used in the final results page.
    def results_users(self):#I don't know why I named this users because it is for the users pay rate for the selected pay period.
        self.rate = '''
                </p><hr><p>Pay Rate:
                '''
        rate = self.rate
        return rate#This again will return the value of the html held in this variable.
    def results_gross(self):#This returns the gross section for the user.
        self.new_gross = '''
                </p><hr><p>Gross Pay:
                '''
        new_gross = self.new_gross
        return new_gross#This is the results that are displayed in the html. Works better if the values are passed through in a return value.
    def results_tax(self):#This is the section that will come before the amount of taxes paid by the user.
        self.tax_amount = '''
                </p><hr><p>Taxes Paid:
        '''
        tax_amount = self.tax_amount
        return tax_amount#This returns the selected statement above.
    def results_net(self):#This will display before the net pay is displayed.
        self.new_net = '''
                </p><hr><p>Net Pay:
        '''
        new_net = self.new_net
        return new_net#this will return the paragraph to describe what the results on the page are for.

    def results_close(self):#This just closes off the <p> tag because if I close it off in the results_net it will not display correctly.
        self.new_close = '''
                </p></hr>
        '''
        new_close = self.new_close
        return new_close#This displays the results of the close section which just closes off the page.



