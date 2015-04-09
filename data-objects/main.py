'''
David Gall
04/08/15
DPW
Data-Objects
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home_planet = "Alderan"

        yoda = Character()
        yoda.name = "Matser Yoda"
        yoda.profession = "Jedi Knight"
        yoda.age = 762
        yoda.home_planet = "Dagobah"

        chars = [luke, leia, yoda]
        print chars[0].profession+", "+chars[0].home_planet
        print chars[1].profession+", "+chars[1].home_planet

class Character(object):
    def __init__(self):#constructor function
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
