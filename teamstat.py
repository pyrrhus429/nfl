import os, sys, urllib2, re
#sys.path.insert(0, "/home/dthap/lib/python")
from BeautifulSoup import BeautifulSoup
from numpy import *

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

def get_data(url):

    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
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
    return data

def get_stat(data, var):
    return [float(i) for i in array(data)[1:,data[0].index(var)]] 

if __name__ == "__main__":
    for i in get_data(get_url(defense="PASSING")):
        print ", ".join(i)

    data = get_data(get_url(defense="PASSING"))

    print average(get_stat(data,"Pts/G"))
