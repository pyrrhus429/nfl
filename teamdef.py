import os, sys, urllib2, re
sys.path.insert(0, "/home/dthap/lib/python")
from BeautifulSoup import BeautifulSoup

url = "http://www.nfl.com/stats/categorystats?tabSeq=2&offensiveStatisticCategory=GAME_STATS&conference=ALL&role=TM&season=2011&seasonType=REG&d-447263-s=TOTAL_YARDS_GAME_AVG&d-447263-o=2&d-447263-n=1"

html = urllib2.urlopen(url)

soup = BeautifulSoup(html)


#  <tr class="odd">



#tmp=soup.table.findAll(attrs={'class':re.compile("odd|even")})
tr=soup.table.findAll('tr')

for i in tr:
    for j in i.contents:
        try:
            k=j.string.strip()
            if k=="Rk":
                print k, 
            else:
                print k,
        except:
            print(j.a.contents[0]),
            pass
    print ""
