from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd
from superclassapi import GetFromApi

# 'http://universities.hipolabs.com/search'

baseurl = 'http://universities.hipolabs.com/'
restler = GetFromApi(baseurl)
alldata = restler.setFullUrl("search").GetDataFromApi().GetResultAsList()


regions = {'Asia': ['India', 'Indonesia', 'Japan', 'China', 'Korea, Republic of', "Korea, Democratic People's Republic of"],
           'Europe': ['Germany', 'France', 'Italy', 'Spain', 'United Kingdom'],
           'Africa': ['Nigeria', 'Egypt', 'South Africa', 'Kenya', 'Tanzania, United Republic of']}

#pprint(set(map(lambda x: x['country'], alldata)))
#for region in regions:
#    region_counts[region] = len(list(filter(lambda x: x['country'] in regions[region] ,alldata)))
for region in regions:
    ucounts = {}
    for country in regions[region]:
        ucounts[country] = len(list(
            filter(lambda x: x['country'] == country, alldata)
        ))    
    df = pd.DataFrame.from_dict(ucounts, orient='index', columns=['Number of universities'])
    plt.bar(df.index, df['Number of universities'],linewidth=3)
    plt.xlabel('Countries')
    plt.ylabel('Number of universities')
    plt.title(f'Number of universities in different countries ({region})')
    #plt.figure()
plt.show()

