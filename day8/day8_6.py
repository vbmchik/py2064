from pprint import pprint
from day8_5 import Textdata

t = Textdata().readfile('input.txt').createresult()
pprint(t.maxincome())
pprint(t.map)