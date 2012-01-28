import sys, urllib2, re
from BeautifulSoup import BeautifulSoup

def get_url(
    symbol
    , team = None
    ):
    if team == None:
        team = get_team_name(symbol=symbol).replace(' ', '').lower()

    url = "http://www.nfl.com/teams/" + team +"/schedule?team="+ symbol
    return url

def get_data(symbol
             ,team=None):

    html = urllib2.urlopen(get_url(symbol,team))
    soup = BeautifulSoup(html)
    table = soup.findAll(attrs={'class':re.compile("tbdy1")})
    data =[['TeamScore','OppScore','Opp','Week']]
    for j in table:
        try:
            row=[ k.contents for k in j.findAll("td")]
            week = row[0][0]
            x=row[2]
            team1 = x[1].string
            score1 =re.search('[0-9]+',x[2].string).group(0)
            team2 = x[3].string
            score2 =re.search('[0-9]+',x[4].string).group(0)
            if team1==symbol:
                team_score = score1
                opp_score = score2
                opp = '@'+team2

            else:
                team_score = score2
                opp_score = score1
                opp = team1
            data.append([int(team_score), int(opp_score), str(opp), str(week)])
        except:
            pass
    
    return data

def get_team_name(symbol=None,
                  team=None):
    team_dict ={ 'MIN':'Minnesota Vikings'
            , 'IND':'Indianapolis Colts'
            , 'CAR':'Carolina Panthers'
            , 'TB':'Tampa Bay Buccaneers'
            , 'DEN':'Denver Broncos'
            , 'SD':'San Diego Chargers'
            , 'BUF':'Buffalo Bills'
            , 'DAL':'Dallas Cowboys'
            , 'WAS':'Washington Redskins'
            , 'STL':'St.Lous Rams'
            , 'NO':'New Orlean Saints'
            , 'NE':'New England Patriots'
            , 'NYG':'New York Giants'
            , 'PHI':'Philadelphia Eagles'
            , 'TEN':'Tennessee Titans'
            , 'CIN':'Cincinnati Bengals'
            , 'JAC':'Jacksonville Jaguars'
            , 'MIA':'Miami Dolphins'
            , 'ATL':'Atlanta Falcons'
            , 'ARI':'Arizona Cardinals'
            , 'DET':'Detroit Lions'
            , 'OAK':'Oakland Raiders'
            , 'CLE':'Cleveland Browns'
            , 'GB':'Green Bay Packers'
            , 'CHI':'Chicago Bears'
            , 'KC':'Kansas City Chiefs'
            , 'SEA':'Seattle Seahawks'
            , 'SF':'San Francisco 49ers'
            , 'PIT':'Pittsburgh Steelers'
            , 'NYJ':'New York Jets'
            , 'HOU':'Houston Texans'
            , 'BAL':'Baltimore Ravens'
            }
    if symbol != None:
        return team_dict[symbol]
    else:
        inv_team_dict = dict([(j,i) for i,j in team_dict.items()])
        return inv_team_dict[team]

if __name__ == "__main__":

    for i in get_data("NYG", "newyorkgiants"):
        print i

    for i in get_data("NE"):
        print i

    print get_team_name('NYG')
    print get_team_name(team='New York Giants')
