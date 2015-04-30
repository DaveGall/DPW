#__author__ = 'davegall'

class Lakers(object):
    def __init__(self):
        self.number = 0
        self.name = ''
        self.game_average = 0
        self.career_points = 0
        self.position = ''
        self.year_drafted = 0


class Data(object):
    def __init__(self):
        kareem = Lakers()
        kareem.number = 33
        kareem.name = 'Kareem Abdul-Jabbar'
        kareem.game_average = 24.6
        kareem.career_points = 38,387
        kareem.position = 'Center'
        kareem.year_drafted = 1976

        elgin = Lakers()
        elgin.number = 22
        elgin.name = 'Elgin Baylor'
        elgin.game_average = 27.4
        elgin.career_points = 23,149
        elgin.position = 'Forward'
        elgin.year_drafted = 1959

        wilt = Lakers()
        wilt.number = 13
        wilt.name = 'Wilt Chamberlain'
        wilt.game_average = 30.1
        wilt.career_points = 31,419
        wilt.position = 'Center'
        wilt.year_drafted = 1968

        magic = Lakers()
        magic.number = 32
        magic.name = 'Magic Johnson'
        magic.game_average = 19.5
        magic.career_points = 17,707
        magic.position = 'Guard'
        magic.year_drafted = 1979

        kobe = Lakers()
        kobe.number = 24
        kobe.name = 'Kobe Bryant'
        kobe.game_average = 25.4
        kobe.career_points = 32,482
        kobe.position = 'Guard'
        kobe.year_drafted = 1996

        shaq = Lakers()
        shaq.number = 34
        shaq.name = "Shaquille O'Neal"
        shaq.game_average = 23.7
        shaq.career_points = 28,596
        shaq.position = 'Center'
        shaq.year_drafted = 1996

        self.players = [kareem, elgin, wilt, magic, kobe, shaq]



