'''
Dave Gall
Inheritance Practice
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = FormPage()
        p.inputs = [['first_name', 'text','First Name'], ['last_name', 'text','Last Name'], ['Submit', 'submit']]
        self.response.write(p.print_out())


class Page(object): #borrowing stuff from the object class
    def __init__(self):#constructor
        self._head = '''
<!DOCTYPE HTML>
 <html>
    <head>
        <title></title>
    </head>
    <body>
        '''

        self._body = 'Filler'
        self._close = '''
    </body>
 </html>'''


    def print_out(self):
        return self._head+self._body+self._close


class FormPage(Page):
    def __init__(self):
        #constructor function for the super class
        Page.__init__(self) #One way to run it
        #super(FormPage,self).__init__() another way. I like the first one better.

        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''
        #<input type="text" value="" name="first_name" placeholder="First Name"/>['first_name', 'text','last_name']
        #<input type="text" value="" name="last_name" placeholder="Last Name"/>
        #<input type="submit" value="Submit"/>

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change the privates input variable.
        self.__inputs = arr
        #Sort through the mega array and create html based on what is there.
        for item in arr:
            self._form_inputs += '<input type="'+item[1]+'" name="'+item[0]
            #if there is a third item add it in
          #  if len(item)>2:
           #     self._form_inputs +='" placeholder="'+item[2]+'" />'
            #otherwise end the tag
            #else:
             #   self._form_inputs += '"/>'
        #or you can use the try method.
            try:
                self._form_inputs +='" placeholder="'+item[2]+'" />'
            except:
                self._form_inputs += '"/>'

        print self._form_inputs


    #Using polymorphism here - method overriding
    def print_out(self):
        return self._head+self._body+self._form_open+self._form_inputs+self._form_close+self._close









app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
