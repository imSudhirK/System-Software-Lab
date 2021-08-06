import sqlite3
import csv
if __name__ == "__main__":
    ipldb =sqlite3.connect("ipl.db")
    cur = ipldb.cursor()
    with open('team.csv','rU') as data:
        dr=csv.DictReader(data)
        to_db=[(i['team_id'], i['team_name']) for i in dr]
    cur.executemany('''INSERT INTO TEAM ('team_id', 'team_name') VALUES (?, ?)''', to_db)
    ipldb.commit()
    with open('player.csv','rU') as data1:
        dr1=csv.DictReader(data1)
        to_db1=[(i['player_id'], i['player_name'], i['dob'], i['batting_hand'], i['bowling_skill'], i['country_name']) for i in dr1]
    cur.executemany('''INSERT INTO PLAYER ('player_id', 'player_name', 'dob','batting_hand','bowling_skill','country_name') VALUES (?, ?, ?, ?, ?, ?)''', to_db1)
    ipldb.commit()
    with open('match.csv','rU') as data2:
        dr2=csv.DictReader(data2)
        to_db2=[(i['match_id'], i['season_year'], i['team1'], i['team2'], i['battedfirst'], i['battedsecond'], i['venue_name'], i['city_name'], i['country_name'], i['toss_winner'], i['match_winner'], i['toss_name'], i['win_type'], i['man_of_match'], i['win_margin']) for i in dr2]
    cur.executemany('''INSERT INTO MATCH ('match_id', 'season_year', 'team1', 'team2', 'battedfirst', 'battedsecond', 'venue_name', 'city_name', 'country_name', 'toss_winner', 'match_winner', 'toss_name', 'win_type', 'man_of_match', 'win_margin') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', to_db2)
    ipldb.commit()
    with open('player_match.csv','rU') as data3:
        dr3=csv.DictReader(data3)
        to_db3=[(i['playermatch_key'], i['match_id'], i['player_id'], i['batting_hand'], i['bowling_skill'], i['role_desc'], i['team_id']) for i in dr3]
    cur.executemany('''INSERT INTO PLAYER_MATCH ('playermatch_key', 'match_id', 'player_id', 'batting_hand', 'bowling_skill', 'role_desc', 'team_id') VALUES (?, ?, ?, ?, ?, ?, ?)''', to_db3)
    ipldb.commit()
    with open('ball_by_ball.csv','rU') as data4:
        dr4=csv.DictReader(data4)
        to_db4=[(i['match_id'], i['innings_no'], i['over_id'], i['ball_id'], i['striker_batting_position'], i['runs_scored'], i['extra_runs'], i['out_type'], i['striker'], i['non_striker'], i['bowler']) for i in dr4]
    cur.executemany('''INSERT INTO BALL_BY_BALL ('match_id', 'innings_no', 'over_id', 'ball_id', 'striker_batting_position', 'runs_scored', 'extra_runs', 'out_type', 'striker', 'non_striker', 'bowler') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', to_db4)
    ipldb.commit()
    ipldb.close()


