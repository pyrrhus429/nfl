import sys, urllib2, re
from BeautifulSoup import BeautifulSoup

def get_url(
    team 
    , symbol 
    ):

    url = "http://www.nfl.com/teams/" + team +"/schedule?team="+ symbol
    return url

def get_data(url):

    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    table = soup.findAll(attrs={'class':re.compile("tbdy1")})
    data =[]
    
    return table

data = get_data(get_url("newyorkgiants","NYG"))

for j in data:
    try:
        row=[ k.contents for k in j.findAll("td")]
        week = row[0][0]
        x=row[2]
        team1 = x[1].string
        score1 =re.search('[0-9]+',x[2].string).group(0)
        team2 = x[3].string
        score2 =re.search('[0-9]+',x[4].string).group(0)
        if team1=='NYG':
            team_score = score1
            opp_score = score2
            opp = '@'+team2
    
        else:
            team_score = score2
            opp_score = score1
            opp = team1
        print team_score, opp_score, opp, week
    except:
        pass
