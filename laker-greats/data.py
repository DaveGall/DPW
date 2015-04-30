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


