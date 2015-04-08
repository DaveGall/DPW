'''
Name:
Date:
Class:
Assignment:
'''
import webapp2# uses the webapp2 library

class MainHandler(webapp2.RequestHandler): #Declaring a class
    def get(self):# Function that starts everything. Catalyst.
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()
        #code goes here

class Button(object):
    def __init__(self):
        self.label = "" # Public attribute.
        self.__size = 60 # Private attribute.
        self._color = "000000" #Protected attribute
        #self.on_roll_over("Hello.")
    def click(self):#self is equivalent to this in javascript.
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button" + message

    def show_label(self):
        print "My label is "+self.label


#Leave this alone, don't touch it.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
