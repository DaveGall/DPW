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
            <a href="?name=elgin">Elgin Baylor</a></br>
            <a href="?name=magic">Magic Johnson</a></br>
            <a href="?name=wilt">Wilt Chamberlain</a></br>
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

class ResultsPage(MainPage):
    def __init__(self):
        MainPage.__init__(self)
        self.div_open = '<div method="GET">'
        self.div_close = '</div>'
        self.__links = []
        self.place_stats = ''

    @property
    def links(self):
        pass

    @links.setter
    def links(self, arr):
        self.__links = arr
        for item in arr:
            self.place_stats += '<a href="?'+item[0]
            try:
                self.place_stats += '"name="'+item[0]+'">'+item[0]

            except:
                self.place_stats +='"</a>'

        print self.place_stats

    def print_out(self):
        all = self.head+self.body+self.div_open+self.place_stats+self.div_close+self.close
        all = all.format(**locals())
        return all

