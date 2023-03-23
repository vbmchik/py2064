from itertools import groupby


class  Textdata():
    
    def __init__(self) -> None:
        self.data=[]
        self.map = {}
        self.calendar={
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JLY": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
    def readfile(self, filename:str):
        try:
            with open(filename, "t+r") as file:
                for line in file.readlines():
                    l = []
                    for word in line.split():
                        l.append(''.join(filter(lambda q: q.isalnum(), word)))
                    self.data.append(l)
            self.data.sort(key=lambda x: x[2])
        except:
            print('file not found!')
        return self
    
    def sortmonths(self, l):
        l.sort(key = lambda x: self.calendar[x[1]])
        return l
    
    def createresult(self):
        self.map = dict(
            map(
                lambda y: ( int(y[0]), 
                           {t[1]: int(t[0]) for t in self.sortmonths(list(y[1]))}
                           ),
                groupby(self.data, key = lambda t: t[2])
            )
        )
        return self
    
    def maxmonth(self, year):
        #month = max(self.map[year], key=lambda x: self.map[year][x])
        month = max(self.map[year].items(), key=lambda x: x[1])
        return month
    
    def sumyear(self, year):
        sum = 0
        for _, y in self.map[year].items():
            sum += y
        return sum
    
    def maxyear(self):
        year = max(self.map, key=self.sumyear)
        return (year, self.sumyear(year))
    
    def maxincome(self):
        year = max(self.map,key=lambda x: self.maxmonth(x)[1])
        t = self.maxmonth(year)
        return (year, t[0], t[1])