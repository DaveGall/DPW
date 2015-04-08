'''
Name:
Date:
Class:
Assignment:
'''
import webapp2# uses the webapp2 library

class MainHandler(webapp2.RequestHandler): #Declaring a class
    def get(self):# Function that starts everything. Catalyst.
        self.response.write('Hello world!')
        #code goes here

    def additional_functions(selfself):
        pass
        #code goes here


#Leave this alone, don't touch it.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
