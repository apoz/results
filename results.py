# coding=utf-8

import urllib2
from bs4 import BeautifulSoup
from operator import itemgetter  # for sorting the dict

#Config
URL = "http://www.rtve.es/tve/teletexto/200/202_0001.htm"
teams = [
        'Celta',
        'Sevilla',
         'Betis',
         'R.Sociedad',
         'R.Vallecano',
         'Deportivo',
         'Valladolid',
         'Espanyol',
         'Zaragoza',
         'Getafe CF',
         'At. Madrid',
         'Málaga',
         'Athletic',
         'Osasuna',
         'Barcelona',
         'Real Madrid',
         'Levante',
         'Valencia',
         'Mallorca',
         'Granada CF'
]
team_order = {}

response = urllib2.urlopen(URL)
html = response.read()
#html = (response.read()).decode('cp1252')
print(html)

soup = BeautifulSoup(html)
img = soup.find_all(id='FABTTXImage')
print(img[0])
for item in teams:
        team_order[item] = str(img[0]).find(item)

for key, value in sorted(team_order.items(), key=itemgetter(1)):
        print(key, value)
#print(team_order)
#print(soup.prettify())

#alt_search = re.compile('FABTTXImage[^>]>')
#result = alt_search.match(html)

#print(result)

