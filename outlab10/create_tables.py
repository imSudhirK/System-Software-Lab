import sqlite3
ipldb = sqlite3.connect('ipl.db')
cur = ipldb.cursor()
cur.execute(
    '''CREATE TABLE TEAM (team_id INT NOT NULL, team_name TEXT, PRIMARY KEY (team_id)) ''')
cur.execute('''CREATE TABLE PLAYER (player_id INT NOT NULL, player_name TEXT, dob TIMESTAMP, batting_hand TEXT, bowling_skill TEXT, country_name TEXT, PRIMARY KEY (player_id))''')
cur.execute(
    '''CREATE TABLE MATCH (match_id int NOT NULL, season_year int, team1 int, team2 int, battedfirst int, battedsecond int, venue_name text, city_name text, country_name text, toss_winner int, match_winner int, toss_name text, win_type text, man_of_match int, win_margin int,
    			PRIMARY KEY(match_id),
    			FOREIGN KEY(team1) REFERENCES TEAM(team_id),
    			FOREIGN KEY(team2) REFERENCES TEAM(team_id),
    			FOREIGN KEY(battedfirst) REFERENCES TEAM(team_id),
    			FOREIGN KEY(battedsecond) REFERENCES TEAM(team_id),
    			FOREIGN KEY(toss_winner) REFERENCES TEAM(team_id),
    			FOREIGN KEY(match_winner) REFERENCES TEAM(team_id),
    			FOREIGN KEY(man_of_match) REFERENCES PLAYER(player_id))''')
cur.execute('''CREATE TABLE PLAYER_MATCH (playermatch_key int NOT NULL, match_id int, player_id int, batting_hand text, bowling_skill text, role_desc text, team_id int,
				FOREIGN KEY(match_id) REFERENCES MATCH(match_id),
				FOREIGN KEY(team_id) REFERENCES TEAM(team_id),
				FOREIGN KEY(player_id) REFERENCES PLAYER(player_id),
				PRIMARY KEY(playermatch_key))''')
cur.execute('''CREATE TABLE BALL_BY_BALL (match_id int, innings_no int, over_id int, ball_id int, striker_batting_position int, runs_scored int, extra_runs int, out_type text, striker int, non_striker int, bowler int,
				FOREIGN KEY(striker) REFERENCES PLAYER(player_id),
				FOREIGN KEY(non_striker) REFERENCES PLAYER(player_id),
				FOREIGN KEY(bowler) REFERENCES PLAYER(player_id),
				FOREIGN KEY(match_id) REFERENCES MATCH(match_id),
				PRIMARY KEY (match_id, innings_no, over_id, ball_id))''')
ipldb.commit()
ipldb.close()
