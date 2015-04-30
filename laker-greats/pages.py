#__author__ = 'davegall'

class MainPage(object):
    def __init__(self):
        self.css = 'css/style.css'
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Laker Greats</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        '''
        self.body = '''
        <div class="container">
            <h2>The Greatest team of all time!!</h2>
            <p>Although the Lakers have not always been in Los Angeles it is where I remember them from.
             Coming from Minneapolis in 1960 they kept the Laker name and have had their great years and had some bad years,
             this season in particular. </p>
        </div>
        <div>
            <a href="?name=kobe">Kobe Bryant</a></br>
            <a href="?name=shaq">Shaquille O'Neal</a></br>
            <a href="?name=kareem">Kareem Abdul Jabbar</a></br>
        </div>
        '''
        self.close = '''
    </body
</html>
        '''

    def print_out(self):
        page = self.head+self.body+self.close
        page = page.format(**locals())
        return page

