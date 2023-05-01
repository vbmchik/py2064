import requests
import numpy
import matplotlib.pyplot as plt
import pandas as pd
from superclassapi import GetFromApi

# 'http://universities.hipolabs.com/search'

url = 'http://universities.hipolabs.com/search'
request = requests.get(url)
data = request.json()

country_counts = {}
for i in data:
    country = i['country']
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1
df = pd.DataFrame.from_dict(country_counts, orient='index', columns=['Number of universities'])

plt.bar(df.index, df['Number of universities'],linewidth=3)
plt.xlabel('Countries')
plt.ylabel('Number of universities')
plt.title(f'Number of universities in different countries ()')
        
plt.show()
url_regions = 'http://universities.hipolabs.com/search?country='
regions = {'Asia': ['India', 'Indonesia', 'Japan', 'China', 'South Korea'],
           'Europe': ['Germany', 'France', 'Italy', 'Spain', 'United Kingdom'],
           'Africa': ['Nigeria', 'Egypt', 'South Africa', 'Kenya', 'Tanzania']}
for region, countries in regions.items():
    region_counts = {}
    for country, count in country_counts.items():
        if country in countries:
            if region in region_counts:
                region_counts[region] += count
            else:
                region_counts[region] = count
    df = pd.DataFrame.from_dict(region_counts, orient='index', columns=['Number of universities'])

    plt.bar(df.index, df['Number of universities'],linewidth=3)
    plt.xlabel('Countries')
    plt.ylabel('Number of universities')
    plt.title(f'Number of universities in different countries ({region})')
        
plt.show()
    
