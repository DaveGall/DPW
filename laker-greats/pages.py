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

            <ul method="GET">
                <li><a href="?number=24">Kobe Bryant</a></li>
                <li><a href="?number=33">Kareem Abdul Jabbar</a></li>
                <li><a href="?number=22">Elgin Baylor</a></li>
                <li><a href="?number=13">Wilt Chamberlain</a></li>
                <li><a href="?number=32">Magic Johnson</a></li>
                <li><a href="?number=34">Shaquille O'Neal</a></li>
            </ul>

        '''
        self.close = '''
        </div>
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
        self.div_open = '<div>'
        self.div_close = '</div>'
        self.__links = []
        self.place_stats = ''


   # @property
    #def links(self):
     #   pass

    #@links.setter
    #def links(self, arr):
     #   self.__links = arr
      #  for item in arr:
       #     self.place_stats += '<p'+item[0]+'</p>'


#        print self.place_stats


    def print_out(self):
        all = self.head+self.body+self.div_open+self.place_stats+self.div_close+self.close
        all = all.format(**locals())
        return all

