from itertools import groupby
from pprint import pprint
import requests

url = 'http://universities.hipolabs.com/search'

headers = {"Accept": 'application/json'}

r = requests.get(url=url,headers=headers)

universities = list(r.json())

countries = list( map( lambda x: x['country'], universities) )

countries.sort()
countries = dict( 
                 map( lambda t: (t[0], len(list(t[1]))), groupby(countries))
                 )
pprint(countries)