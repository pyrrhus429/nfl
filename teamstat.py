import os, sys, urllib2, re
sys.path.insert(0, "/home/dthap/lib/python")
from BeautifulSoup import BeautifulSoup

conf="null" #null-->ALL
offense = "null" #e.g. GAME_STATS
defense = "null" #e.g. GAME_STATS
season = "REG" #POST --> Postseason

def get_url(conf="null"
            , offense = "null" 
            , defense = "null" 
            , season = "REG" 
            ):
    url = ("http://www.nfl.com/stats/categorystats?archive=false&conference=" +
           "null&role=OPP&offensiveStatisticCategory="+offense + 
           "&defensiveStatisticCategory="+defense+"&season=2011&seasonType="+
           season +"&tabSeq=2&qualified=true&Submit=Go")
    return url 

html = urllib2.urlopen(get_url(defense="RUSHING"))

soup = BeautifulSoup(html)

#tmp=soup.table.findAll(attrs={'class':re.compile("odd|even")})
tr=soup.table.findAll('tr')
data =[]
for i in tr:
    r =[]
    for j in i.contents:
        try:
            k=j.string.strip()
        except Exception as e:
            k=j.a.contents[0]
        if k!='':
            r.append(k)
    data.append(r)

for i in data:
    print ", ".join(i)

