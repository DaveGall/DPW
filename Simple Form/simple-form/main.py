'''
David Gall
04/15/2015
DPW
Simple Login Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        display = Page() #This variable grabs the Page class and turns it into an easy to use variable


        if self.request.GET:#This begins the conditional statement that will determine which string to load.
            user = self.request.GET['user_name'] #This gets the information typed into the name field and puts it into an easy to use variable
            address = self.request.GET['address'] #This grabs the address typed in and puts it into the address variable for use later
            city = self.request.GET['city']#This line grabs the city input by the user and places into the variable city for easier use later.
            state = self.request.GET['state']#This line takes the state chosen by the user and places into the easy to use state variable.
            zip = self.request.GET['zip']#This grabs the zipcode input by the user and places it into an easy to use variable called zip
            mail = self.request.GET['coupon']#Takes the result of the users choice on whether to receive coupons in the mail.
            self.response.write(display.head()+display.result_body()+display.dis_person()+' '+user+display.house()+' '+address+'</br>'+city+', '+state+'</br>'+zip+display.savings()+mail+display.add_ending()+display.close())
        #The line above is what will display if the user has input information into the fields or if the user clicks the submit button.
        else:
            self.response.write(display.head()+display.body()+display.close())#This line right here will display anytime a new user comes along and needs to use the form.





class Page(object):#This line starts the Page class which holds all the attributes to create the displayed page the way it is.
    def head(self):#This begins the head attribute which houses all the critical information to get started.
        self.css = "css/style.css"#This imports the css style sheet from the css folder to the page to display all your pretty work.
        #This begins the actual head part of the html page.
        self.page_head ='''
<!DOCTYPE HTML>
<html>
    <head>
        <title>My Simple Form</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div class="title">
            <h3>Thank you for ordering a new computer with us today</h3>
            <p>We hope you enjoy it.</p>
            <p>Please contact us at 1-800-555-1234 if you need assistance.</p>
        </div>
        <hr>
        '''
        #I added some h3 and p tags that will display a nice little header at the top of the page.
        top = self.page_head#This takes the whole page_head section and puts it into a one word variable
        top = top.format(**locals())#This line allows us to take {self.css} and run our own stylesheet on the web page.
        return top#This returns the result of page_head for use in our display.


    def body(self):#This line begins the main body of the html page. It houses the form and all it's parts.
        #I have put a state selector in there because I like the way they look and they are very common.
        self.page_body = '''<div id="form_container">
        <form method="GET">
            <label for="name">Name:</label><input id="name" type="text" name="user_name" placeholder="John Smith"/>
            <label for="address" >Address:</label><input id="address" type="text" name="address" placeholder="123 old st."/>
            <label for="city">City:</label><input id="city" type="text" name="city" placeholder="Your Town"/>
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
            </select><br>
            <label for="zip">ZipCode:</label><input type="text" id="zip" name="zip" placeholder="12345">
            <p>Would you like to sign up for company discount emails?</p>
            <label for="yes" class="discount">Yes</label>
            <input type="radio" id="yes" name="coupon" value="Yes"/>
            <label for="no" class="discount">No</label>
            <input type="radio" id="no" name="coupon" value="No"/>
            <input type="submit" value="Submit" id="button"/>
        </form>
        '''
        main = self.page_body#This takes the information in page_body and places it into main variable
        return main#This returns the variable main as an output so that we can use it later in our code.

    def close(self):#This begins our closing section of code. All the main closing tags are housed here.
        self.page_close = '''
        </div>
        <hr>
        <footer>
            <ul>
                <li>Contact</li>
                <li>Legal</li>
                <li>Address</li>
                <li>Jobs</li>
            </ul>
        </footer>
    </body>
</html>
        '''
        end = self.page_close#This line takes the page_close and creates a variable named end
        return end#This returns that end variable for use in the code when needed.

    def result_body(self):#This begins the attributes that we will use after the user has typed in their information.
        self.finished_body = '''
        <div id="new_container">'''
        fb = self.finished_body#This takes the opening div tag section and puts it into a tidy variable
        return fb#This returns that variable for use later in the code.

    def dis_person(self):#This is not gangster, I was shortening display but did not realize what it came out like until now. This will display the sentence prior to the users name being displayed.
        self.person = '''<p>Thank you for your order: '''
        np = self.person#This takes that person and puts it into a variable for later use.
        return np#This returns our little sentence into reusable code.

    def house(self):#This begins the section that will display just above the address to let the user know where their order is going.
        self.add = '''</p><p>Your order will be shipped to: </p>'''
        home = self.add#This puts that sentence into a nice little variable
        return home#This line helps return our sentence so that it may be placed in our string for display purposes.

    def savings(self):#This begins the section that will display on the same line as the answer to whether or not the person wants to receive coupons.
        self.coup = '''<p>Would you like to receive coupons? '''
        email_savings = self.coup#This line places that sentence into a tidy variable
        return email_savings#This line returns that variable for use in the string when we display the users information.

    def add_ending(self):#This is just a closing paragraph tag. I wanted the answer to the yes or no question to be displayed on the same line as the question so I put the closing tag in a separate attribute.
        ending = '''</p>'''
        return ending#This returns the tag for use in the results after the user inputs their information.












app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
