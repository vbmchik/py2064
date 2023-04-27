from pprint import pprint
import requests
from superclassapi import GetFromApi
#
# https://datausa.io/api/data?drilldowns=Nation&measures=Population

baseurl = 'https://datausa.io/api' 
method = 'data'
params = {'drilldown': 'State', 'measures': 'Population', 'year': '2018'}

g = GetFromApi(baseurl).setFullUrl(method, drilldowns='Nation', measures = 'Population')
r = g.GetDataFromApi().GetResultAsList()


pprint(r["data"])
